# 🌊 FLOODCAST RESPONSE AI

### AI-Based Flood Impact Assessment & Emergency Resource Recommendation System

**FLOODCAST RESPONSE AI** is a web-based flood impact assessment and emergency resource recommendation system designed to support faster and more informed disaster response decisions.

The system evaluates flood conditions using multiple risk factors, calculates an overall flood impact score, classifies the emergency priority level, and recommends essential emergency resources such as ambulances, rescue boats, rescue personnel, and emergency shelters.

By combining an interactive web interface with a FastAPI backend, the platform provides a simple and accessible way to assess flood situations and support emergency response planning.

---

## 🚀 Live Demo

| Component               | Deployment Link                                        |
| ----------------------- | ------------------------------------------------------ |
| 🌐 Frontend Application | https://floodcast-response-ai.onrender.com             |
| ⚙️ Backend API          | https://floodcast-response-backend.onrender.com        |
| 📘 API Documentation    | https://floodcast-response-backend.onrender.com/docs   |
| ❤️ Backend Health Check | https://floodcast-response-backend.onrender.com/health |

---

## 🎯 Project Objectives

* Assess flood impact based on multiple environmental and social risk factors.
* Calculate an overall flood impact score.
* Automatically classify flood situations into priority levels.
* Identify potential risks to vulnerable populations and critical infrastructure.
* Recommend emergency resources based on the calculated priority.
* Provide a user-friendly interface for flood assessment.
* Support faster and more structured emergency response planning.

---

## ✨ Key Features

### 1. Flood Impact Assessment

Evaluates flood conditions using the following parameters:

* Flood Severity
* Flood Depth
* Population Density
* Population Vulnerability
* Critical Infrastructure Risk
* Road Accessibility

### 2. Impact Score Calculation

Calculates a numerical impact score between 0 and 100 using a weighted scoring methodology.

### 3. Emergency Priority Classification

Automatically classifies the flood situation into four priority levels:

| Impact Score | Priority Level |
| ------------ | -------------- |
| 0–40         | 🟢 LOW         |
| 41–60        | 🟡 MEDIUM      |
| 61–80        | 🟠 HIGH        |
| 81–100       | 🔴 CRITICAL    |

### 4. Risk Explanation

Provides explanations for detected risk factors, helping users understand why a particular priority level was assigned.

### 5. Emergency Resource Recommendation

Recommends essential emergency resources according to the calculated priority level.

| Priority | Ambulance | Rescue Boats | Rescue Personnel | Emergency Shelter |
| -------- | --------: | -----------: | ---------------: | ----------------- |
| LOW      |         0 |            0 |                1 | No                |
| MEDIUM   |         1 |            0 |                2 | No                |
| HIGH     |         1 |            1 |                3 | Yes               |
| CRITICAL |         1 |            1 |                5 | Yes               |

*These are prototype recommendations based on predefined rules, not real-time resource availability.*

### 6. Web-Based Interface

Provides an interactive frontend where users can enter flood information, submit assessments, and view results.

### 7. REST API Integration

Uses a FastAPI backend to process flood assessment requests and return structured JSON responses.

---

## 🧠 System Workflow

The system follows a structured assessment process:

**Step 1 – Input Collection**

The user enters the affected zone and flood-related parameters.

**Step 2 – Risk Evaluation**

The backend evaluates the submitted parameters using predefined weights.

**Step 3 – Impact Score Calculation**

The system calculates the overall impact score.

**Step 4 – Priority Classification**

The impact score is classified as LOW, MEDIUM, HIGH, or CRITICAL.

**Step 5 – Risk Explanation**

The system identifies and displays important risk factors.

**Step 6 – Resource Recommendation**

Emergency resource requirements are recommended according to the priority level.

**Step 7 – Result Display**

The frontend displays the assessment results to the user.

---

## 📊 Impact Calculation Methodology

The system uses a weighted scoring approach.

### Impact Score Formula

```text
Road Risk = 100 - Road Accessibility

Impact Score =

(Flood Severity × 0.25) +
(Flood Depth × 0.20) +
(Population Density × 0.15) +
(Vulnerability × 0.15) +
(Critical Infrastructure × 0.15) +
(Road Risk × 0.10)
```

The final score is restricted to a range of 0–100.

### Weight Distribution

| Risk Parameter          |   Weight |
| ----------------------- | -------: |
| Flood Severity          |      25% |
| Flood Depth             |      20% |
| Population Density      |      15% |
| Vulnerability           |      15% |
| Critical Infrastructure |      15% |
| Road Accessibility Risk |      10% |
| **Total**               | **100%** |

The system uses predefined thresholds to determine the emergency priority level.

---

## 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Fetch API

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

### API Communication

* REST API
* JSON
* HTTP POST Requests
* CORS Middleware

### Deployment

* GitHub – Source Code Management
* Render – Frontend and Backend Hosting

---

## 🏗️ System Architecture

```text
              USER
                |
                v
       FRONTEND APPLICATION
          HTML / CSS / JS
                |
                v
          FETCH API REQUEST
                |
                v
          FASTAPI BACKEND
                |
                v
       FLOOD IMPACT ENGINE
                |
        +-------+-------+
        |       |       |
        v       v       v
      SCORE  PRIORITY  RISK
    CALCULATION LEVEL  ANALYSIS
        |       |       |
        +-------+-------+
                |
                v
      RESOURCE RECOMMENDATION
                |
                v
         JSON RESPONSE
                |
                v
       FRONTEND RESULT DISPLAY
```

---

## 📁 Project Structure

```text
FLOODCAST_RESPONSE_AI/
│
├── backend/
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
│
├── docs/
│
├── model/
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

---

## ⚙️ Installation and Setup

### Prerequisites

Install the following before running the project:

* Python 3.10 or above
* Visual Studio Code
* Git
* Web Browser

### Step 1 – Clone the Repository

```bash
git clone https://github.com/dineshrajasujithra04/FLOODCAST_RESPONSE_AI.git
```

### Step 2 – Navigate to the Project

```bash
cd FLOODCAST_RESPONSE_AI
```

### Step 3 – Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4 – Activate the Virtual Environment

For Windows CMD:

```bash
venv\Scripts\activate.bat
```

### Step 5 – Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6 – Start the Backend

```bash
uvicorn backend.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### Step 7 – Open the Frontend

Open `frontend/index.html` using Live Server in Visual Studio Code.

The frontend will communicate with the backend API.

---

## 🔗 API Documentation

The project provides REST API endpoints through FastAPI.

### 1. Root Endpoint

**Method:** GET

```text
/
```

Returns the backend application status.

### 2. Health Check Endpoint

**Method:** GET

```text
/health
```

Checks whether the backend is running.

### 3. Flood Prediction Endpoint

**Method:** POST

```text
/predict
```

Accepts flood-related parameters and returns an impact assessment with priority classification and recommended emergency resources.

### Sample Request

```json
{
    "zone": "Zone A",
    "flood_severity": 90,
    "flood_depth": 80,
    "population_density": 85,
    "vulnerability": 90,
    "critical_infrastructure": 80,
    "road_accessibility": 30
}
```

### Sample Response

```json
{
    "zone": "Zone A",
    "impact_score": 83.75,
    "priority": "CRITICAL",
    "explanation": [
        "High flood severity detected.",
        "High flood water depth detected.",
        "High population density in the affected zone.",
        "Vulnerable population requires additional support.",
        "Critical infrastructure is at risk.",
        "Poor road accessibility may affect rescue operations."
    ],
    "recommended_resources": {
        "ambulance": 1,
        "rescue_boat": 1,
        "rescue_personnel": 5,
        "emergency_shelter": true
    }
}
```

### Interactive API Testing

Visit the Swagger documentation to test the API:

https://floodcast-response-backend.onrender.com/docs

---

## 🌍 Real-World Applications

FLOODCAST RESPONSE AI can support:

* Disaster management departments
* Emergency response teams
* Flood monitoring organizations
* Local government authorities
* Rescue and relief coordination teams
* Community-level disaster preparedness

**Note:** This project is a prototype decision-support system. Its scoring rules and resource recommendations should be validated against real-world data and expert guidance before operational use. It does not provide live flood detection, verified resource availability, or automatic emergency dispatch.

---

## 🔮 Future Enhancements

* Integration with real-time weather APIs.
* Satellite imagery-based flood detection.
* Machine learning-based flood prediction.
* GIS-based flood zone visualization.
* Interactive maps showing affected locations.
* Real-time emergency alerts and notifications.
* Database integration for historical flood records.
* Live emergency resource tracking.
* Multilingual support for regional communities.

---

## 💡 Project Highlights

* Full-stack web application.
* Python-based FastAPI backend.
* Interactive HTML, CSS, and JavaScript frontend.
* Weighted flood impact assessment methodology.
* Automated emergency priority classification.
* Rule-based emergency resource recommendations.
* REST API integration.
* Separate frontend and backend deployment.
* Live deployment using Render.

---

## 👩‍💻 Developer

**Sujithra D**

B.Tech – Artificial Intelligence and Data Science

Interested in Artificial Intelligence, Data Science, Web Development, and Industry-Oriented Technology Solutions.

---

## 📜 License

This project is developed for educational, learning, and demonstration purposes.

---

### 🌊 FLOODCAST RESPONSE AI

**Assess the Impact. Identify the Risk. Recommend the Response.**
