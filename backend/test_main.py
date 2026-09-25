from fastapi.testclient import TestClient
from main import app  # Imports your FastAPI app instance

client = TestClient(app)

def test_read_root():
    # Sends a fake GET request to your root endpoint "/" or your health check endpoint
    response = client.get("/")
    
    # Asserts that the server responds successfully (status code 200)
    assert response.status_code == 200