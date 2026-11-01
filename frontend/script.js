const analyzeBtn = document.getElementById("analyzeBtn");

analyzeBtn.addEventListener("click", analyzeFlood);


async function analyzeFlood() {

    const errorMessage = document.getElementById("errorMessage");

    errorMessage.textContent = "";

    const data = {

        zone: document.getElementById("zone").value,

        flood_severity:
            Number(document.getElementById("flood_severity").value),

        flood_depth:
            Number(document.getElementById("flood_depth").value),

        population_density:
            Number(document.getElementById("population_density").value),

        vulnerability:
            Number(document.getElementById("vulnerability").value),

        critical_infrastructure:
            Number(document.getElementById("critical_infrastructure").value),

        road_accessibility:
            Number(document.getElementById("road_accessibility").value)
    };


    try {

        analyzeBtn.textContent = "⏳ ANALYZING...";

        analyzeBtn.disabled = true;


        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)
            }
        );


        if (!response.ok) {
            throw new Error("Backend request failed");
        }


        const result = await response.json();


        // Show result section
        document
            .getElementById("resultSection")
            .classList.remove("hidden");


        // Impact score
        document.getElementById("impactScore")
            .textContent = result.impact_score;


        // Priority
        const priorityElement =
            document.getElementById("priority");

        priorityElement.textContent =
            result.priority;


        // Priority appearance
        if (result.priority === "CRITICAL") {

            priorityElement.style.color = "#d62828";

        } else if (result.priority === "HIGH") {

            priorityElement.style.color = "#e76f00";

        } else if (result.priority === "MEDIUM") {

            priorityElement.style.color = "#c99700";

        } else {

            priorityElement.style.color = "#198754";
        }


        // Explanation
        const explanation =
            document.getElementById("explanation");

        explanation.innerHTML = "";

        result.explanation.forEach(reason => {

            const li = document.createElement("li");

            li.textContent = "✓ " + reason;

            explanation.appendChild(li);
        });


        // Resources
        document.getElementById("ambulance")
            .textContent =
            result.recommended_resources.ambulance;


        document.getElementById("rescueBoat")
            .textContent =
            result.recommended_resources.rescue_boat;


        document.getElementById("personnel")
            .textContent =
            result.recommended_resources.rescue_personnel;


        document.getElementById("shelter")
            .textContent =
            result.recommended_resources.emergency_shelter
                ? "REQUIRED"
                : "Not Required";


        // Scroll to results
        document
            .getElementById("resultSection")
            .scrollIntoView({
                behavior: "smooth"
            });

    }

    catch (error) {

        console.error(error);

        errorMessage.textContent =
            "❌ Cannot connect to FloodCast backend. Make sure FastAPI is running.";

    }

    finally {

        analyzeBtn.textContent = "🔍 ANALYZE FLOOD";

        analyzeBtn.disabled = false;
    }
}