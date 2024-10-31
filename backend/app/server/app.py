from fastapi import FastAPI
from app.server.routes.employee import router as EmployeeRouter

app = FastAPI(
    title="My Custom App",
    description="A customized version of the original Flask app",
    version="1.0.1",
)

# Include the employee router
app.include_router(EmployeeRouter, tags=["Employee"], prefix="/employee")

# Enhanced root route
@app.get("/", tags=["Root"])
async def read_root():
    return {
        "message": "🚀 Welcome to this fantastic app! 🚀",
        "description": (
            "This application allows you to manage employees efficiently and explore various features. "
            "Feel free to browse around and check out the `/employee` routes for more details."
        ),
        "features": [
            "🔍 Search and filter employees",
            "🗂️ Add, update, and delete employee records",
            "📊 View statistics and insights",
        ],
        "note": "📘 Check out the documentation at /docs for a complete list of endpoints and their usage.",
        "cta": "Let's get started! 💪"
    }

# Endpoint for readiness probe
@app.get("/health/ready", tags=["Health"])
async def readiness_probe():
    return {"status": "Ready"}

# Endpoint for liveness probe
@app.get("/health/live", tags=["Health"])
async def liveness_probe():
    return {"status": "Alive"}
