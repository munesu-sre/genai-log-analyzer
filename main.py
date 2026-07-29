from fastapi import FastAPI

# Initialize our application
app = FastAPI(
    title="GenAI Log Analyzer Engine",
    description="Backend microservice for processing enterprise logs and AI root-cause analysis.",
    version="0.1.0"
)

@app.get("/")
def read_root():
    """Simple root endpoint to confirm API is reachable."""
    return {
        "service": "GenAI Log Analyzer API",
        "environment": "Local Development",
        "status": "active"
    }

@app.get("/healthz")
def health_check():
    """
    SRE Principle: Liveness / Readiness Health Check Endpoint.
    Orchestrators (Kubernetes/ECS) and Load Balancers call this endpoint 
    periodically. If this returns an HTTP error or times out, the system 
    knows the container is unhealthy and automatically replaces it.
    """
    return {
        "status": "UP",
        "database": "Disconnected (Phase 1)",
        "ai_engine": "Local Mock",
        "version": "0.1.0"
    }