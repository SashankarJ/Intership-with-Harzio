from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib




def train_anomaly_model():
    df = pd.read_csv('system_metrics.csv')
    X = df[['cpu', 'ram', 'disk']]
    model = IsolationForest(contamination=0.05)
    model.fit(X)
    joblib.dump(model, 'anomaly_model.pkl')


def detect_anomalies(data):
    model = joblib.load('anomaly_model.pkl')
    predictions = model.predict(data)
    return predictions