from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse
from typing import Optional
import os, json, io, csv

app = FastAPI(title="SIEM Alert Dashboard API", version="0.2.0")

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

def load_alerts():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def apply_filters(data,
                  vendor: Optional[str],
                  severity: Optional[str],
                  detection_type: Optional[str],
                  status: Optional[str],
                  q: Optional[str]):
    def match(a):
        if vendor and a.get("vendor") != vendor: return False
        if severity and a.get("severity") != severity: return False
        if detection_type and a.get("detection_type") != detection_type: return False
        if status and a.get("status") != status: return False
        if q:
            needle = q.lower()
            hay = f"{a.get('summary','')} {a.get('username','')} {' '.join(a.get('tags',[]))}".lower()
            if needle not in hay: return False
        return True
    return [a for a in data if match(a)]

@app.get("/alerts")
def list_alerts(
    vendor: Optional[str] = None,
    severity: Optional[str] = None,
    detection_type: Optional[str] = None,
    status: Optional[str] = None,
    q: Optional[str] = None,
):
    data = load_alerts()
    return JSONResponse(apply_filters(data, vendor, severity, detection_type, status, q))

@app.get("/summary")
def summary():
    data = load_alerts()
    by_sev, by_vendor = {}, {}
    for a in data:
        by_sev[a["severity"]] = by_sev.get(a["severity"], 0) + 1
        by_vendor[a["vendor"]] = by_vendor.get(a["vendor"], 0) + 1
    return {"total": len(data), "by_severity": by_sev, "by_vendor": by_vendor}

@app.get("/export")
def export_alerts_csv(
    vendor: Optional[str] = None,
    severity: Optional[str] = None,
    detection_type: Optional[str] = None,
    status: Optional[str] = None,
    q: Optional[str] = None,
):
    data = load_alerts()
    rows = apply_filters(data, vendor, severity, detection_type, status, q)

    def gen():
        buf = io.StringIO()
        fieldnames = list(rows[0].keys()) if rows else [
            "id","timestamp","vendor","severity","detection_type","src_ip","dst_ip",
            "username","geo","status","summary","tags"
        ]
        writer = csv.DictWriter(buf, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            r = dict(r)
            if isinstance(r.get("tags"), list):
                r["tags"] = ";".join(r["tags"])
            writer.writerow(r)
        buf.seek(0)
        yield buf.read()

    headers = {"Content-Disposition": 'attachment; filename="alerts.csv"'}
    return StreamingResponse(gen(), media_type="text/csv", headers=headers)
