\# SIEM Alert Dashboard



A lightweight dashboard that aggregates and visualizes security alerts from multiple SIEM sources (e.g., Microsoft Defender, Elastic, Splunk).  

Built with \*\*FastAPI\*\* for the backend and \*\*Bootstrap + Chart.js\*\* for the frontend.



---



\## Features

\- Filterable alert feed by vendor, severity, status, and keywords

\- Summary KPIs for total alerts, top severity, and top vendor

\- Charts: Alerts by Severity (doughnut) \& Vendor (bar)

\- Simple HTML frontend (no build tools needed)



---



\## Tech Stack

\*\*Backend:\*\* Python (FastAPI, Uvicorn)  

\*\*Frontend:\*\* HTML, Bootstrap, Chart.js  

\*\*Data:\*\* Static JSON (demo), replaceable with live SIEM API



---



\## Getting Started

1\. \*\*Clone the repo\*\*

&nbsp;  ```bash

&nbsp;  git clone https://github.com/<your-username>/siem-alert-dashboard.git

&nbsp;  cd siem-alert-dashboard

Set up Python environment



bash

Copy

Edit

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

Run backend API



bash

Copy

Edit

cd backend

python -m uvicorn app:app --reload --port 8000

Test:



http://127.0.0.1:8000/health



http://127.0.0.1:8000/alerts



http://127.0.0.1:8000/summary



Open frontend

With API running, open:



bash

Copy

Edit

frontend/index.html

API Endpoints

GET /health – API status



GET /alerts – List alerts with filters:

vendor, severity, status, q (search text)



GET /summary – Returns alert counts by severity and vendor



Roadmap

Export alerts to CSV



Role-based views (Analyst / Manager)



Live WebSocket updates

