# AI-System-Monitor
To check systme usage using ai benifits 

✅ Prerequisites

Make sure you have:

Python 3.9+

pip

Git

Docker

Kubernetes (Minikube or Docker Desktop Kubernetes)

🛠️ STEP 1: Clone or Set Up Project
git clone https://github.com/your-username/AI-System-Monitoring.git
cd AI-System-Monitoring


If you don’t have Git, just create the folder structure and copy the files.

📦 STEP 2: Install Python Dependencies
pip install -r requirements.txt

📊 STEP 3: Start System Metrics Collection

Open a terminal:

python backend/collector.py


This will continuously log system metrics to data/system_metrics.csv.

🧠 STEP 4: Train AI Models

In a new terminal:

python ml_models/train_models.py

🌐 STEP 5: Start Backend API

uvicorn backend.app:app --reload

📈 STEP 6: Launch Dashboard

streamlit run dashboard/dashboard.py
