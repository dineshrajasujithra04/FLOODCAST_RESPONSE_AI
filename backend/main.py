from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(
    title="FloodCast Response AI",
    description="Flood Impact Assessment and Emergency Resource Recommendation System",
    version="1.0.0"
)

origins = [
    "https://floodcast-response-ai.onrender.com",
    "http://localhost:5500",
    "http://localhost:5501",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)


class FloodInput(BaseModel):
    zone: str
    flood_severity: float = Field(ge=0, le=100)
    flood_depth: float = Field(ge=0, le=100)
    population_density: float = Field(ge=0, le=100)
    vulnerability: float = Field(ge=0, le=100)
    critical_infrastructure: float = Field(ge=0, le=100)
    road_accessibility: float = Field(ge=0, le=100)


def calculate_impact(data: FloodInput):

    road_risk = 100 - data.road_accessibility

    impact_score = (
        data.flood_severity * 0.25 +
        data.flood_depth * 0.20 +
        data.population_density * 0.15 +
        data.vulnerability * 0.15 +
        data.critical_infrastructure * 0.15 +
        road_risk * 0.10
    )

    impact_score = round(max(0, min(100, impact_score)), 2)

    if impact_score <= 40:
        priority = "LOW"
    elif impact_score <= 60:
        priority = "MEDIUM"
    elif impact_score <= 80:
        priority = "HIGH"
    else:
        priority = "CRITICAL"

    explanation = []

    if data.flood_severity >= 70:
        explanation.append("High flood severity detected.")

    if data.flood_depth >= 70:
        explanation.append("High flood water depth detected.")

    if data.population_density >= 70:
        explanation.append("High population density in the affected zone.")

    if data.vulnerability >= 70:
        explanation.append("Vulnerable population requires additional support.")

    if data.critical_infrastructure >= 70:
        explanation.append("Critical infrastructure is at risk.")

    if data.road_accessibility <= 40:
        explanation.append("Poor road accessibility may affect rescue operations.")

    if not explanation:
        explanation.append("Flood conditions are currently moderate.")

    if priority == "CRITICAL":
        resources = {
            "ambulance": 1,
            "rescue_boat": 1,
            "rescue_personnel": 5,
            "emergency_shelter": True
        }

    elif priority == "HIGH":
        resources = {
            "ambulance": 1,
            "rescue_boat": 1,
            "rescue_personnel": 3,
            "emergency_shelter": True
        }

    elif priority == "MEDIUM":
        resources = {
            "ambulance": 1,
            "rescue_boat": 0,
            "rescue_personnel": 2,
            "emergency_shelter": False
        }

    else:
        resources = {
            "ambulance": 0,
            "rescue_boat": 0,
            "rescue_personnel": 1,
            "emergency_shelter": False
        }

    return {
        "zone": data.zone,
        "impact_score": impact_score,
        "priority": priority,
        "explanation": explanation,
        "recommended_resources": resources
    }


@app.get("/")
def home():
    return {
        "message": "FloodCast Response AI API is running",
        "status": "online"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict_flood(data: FloodInput):
    return calculate_impact(data)