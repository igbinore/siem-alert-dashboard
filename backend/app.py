from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os, json

app = FastAPI(title="SIEM Alert Dashboard API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample_alerts.json")

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/alerts")
def list_alerts():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return JSONResponse(data)

@app.get("/summary")
def summary():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    by_sev, by_vendor = {}, {}
    for a in data:
        by_sev[a["severity"]] = by_sev.get(a["severity"], 0) + 1
        by_vendor[a["vendor"]] = by_vendor.get(a["vendor"], 0) + 1
    return {"total": len(data), "by_severity": by_sev, "by_vendor": by_vendor}
