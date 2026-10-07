import streamlit as st
import pandas as pd
import joblib


st.set_page_config(page_title="AI System Monitor", layout="wide")


st.title("AI-Powered Real-Time System Monitoring Dashboard")


@st.cache_data
def load_data():
    return pd.read_csv('system_metrics.csv')




data = load_data()


st.subheader("Live System Metrics")
st.line_chart(data[['cpu', 'ram', 'disk']])


st.subheader("Anomaly Detection")
model = joblib.load('anomaly_model.pkl')
preds = model.predict(data[['cpu', 'ram', 'disk']])
data['Anomaly'] = preds
st.dataframe(data.tail(20))


st.subheader("CPU Usage Prediction")
pred_model = joblib.load('predict_cpu.pkl')
import numpy as np
future = np.arange(len(data), len(data)+10).reshape(-1, 1)
predictions = pred_model.predict(future)
st.line_chart(predictions)