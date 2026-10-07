from fastapi import FastAPI
from database import load_data

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI System Monitoring API is running!"}

@app.get("/metrics")
def get_metrics():
    df = load_data()
    return df.tail(100).to_dict(orient="records")