from fastapi.testclient import TestClient
from src.main import app

def test_chat():
    c = TestClient(app)
    r = c.post("/chat", json={"message":"Summarize Q3 revenue trends"})
    assert r.status_code == 200
    assert "answer" in r.json()
