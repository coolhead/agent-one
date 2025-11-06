from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv, find_dotenv
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())  

from fastapi import FastAPI, Body
from prometheus_client import Counter, Histogram, make_asgi_app
from .agent import run_agent

app = FastAPI(title="Agent ONE API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501", "http://127.0.0.1:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REQS = Counter("agent_requests_total", "Total agent calls")
LAT = Histogram("agent_latency_seconds", "Agent end-to-end latency")

@app.post("/chat")
def chat(q: dict = Body(...)):
    REQS.inc()
    with LAT.time():
        answer, trace = run_agent(q.get("message",""), q.get("context",{}))
    return {"answer": answer, "trace": trace}

# /metrics
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)
