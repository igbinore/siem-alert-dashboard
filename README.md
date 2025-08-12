\# SIEM Alert Dashboard



A centralized dashboard for viewing, filtering, and analyzing SIEM alerts from multiple sources such as Microsoft Defender, Elastic, and Splunk.  

Built as part of a cybersecurity project portfolio.



---



\## 📌 Overview

The SIEM Alert Dashboard provides:

\- A backend API (FastAPI) to serve alert data

\- A simple HTML + Bootstrap + Chart.js frontend

\- Filtering by vendor, severity, status, and keywords

\- Summary metrics and charts for quick analysis



---



\## 📂 Project Structure

siem-alert-dashboard/

├── backend/ # FastAPI application

│ └── app.py

├── data/ # Sample alert data (JSON)

│ └── sample\_alerts.json

├── frontend/ # HTML dashboard

│ └── index.html

├── requirements.txt # Python dependencies

└── README.md



yaml

Copy

Edit



---



\## ⚙️ Tech Stack

\*\*Backend:\*\* Python, FastAPI, Uvicorn  

\*\*Frontend:\*\* HTML, Bootstrap 5, Chart.js  

\*\*Data:\*\* Static JSON (replaceable with live SIEM API feeds)



---



\## 🚀 Getting Started



\### 1. Clone the Repository

```bash

git clone https://github.com/<your-username>/siem-alert-dashboard.git

cd siem-alert-dashboard

2\. Set Up Virtual Environment

bash

Copy

Edit

python -m venv venv

venv\\Scripts\\activate   # Windows

\# or: source venv/bin/activate  # Mac/Linux

3\. Install Dependencies

bash

Copy

Edit

pip install -r requirements.txt

4\. Run the Backend

bash

Copy

Edit

cd backend

python -m uvicorn app:app --reload --port 8000

API Health Check: http://127.0.0.1:8000/health



Alerts Endpoint: http://127.0.0.1:8000/alerts



Summary Endpoint: http://127.0.0.1:8000/summary



5\. Open the Frontend

With the API running, open:



bash

Copy

Edit

frontend/index.html

📊 API Endpoints

GET /health

Returns API status:



json

Copy

Edit

{"ok": true}

GET /alerts

Returns alert list with optional filters:



vendor



severity



status



q (search in summary, username, tags)



Example:



bash

Copy

Edit

/alerts?vendor=Elastic\&severity=High

GET /summary

Returns:



json

Copy

Edit

{

&nbsp; "total": 3,

&nbsp; "by\_severity": { "High": 1, "Medium": 1, "Low": 1 },

&nbsp; "by\_vendor": { "Microsoft Defender": 1, "Elastic": 1, "Splunk": 1 }

}

🔮 Future Improvements

CSV export for filtered alerts



Role-based views (Analyst / Manager)



Live WebSocket updates



GeoIP map for source IPs





