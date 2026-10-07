import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib




def train_prediction_model():
    df = pd.read_csv('system_metrics.csv')
    X = np.arange(len(df)).reshape(-1, 1)
    y = df['cpu']
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, 'predict_cpu.pkl')



def predict_cpu(steps=10):
    model = joblib.load('predict_cpu.pkl')
    future = np.arange(steps).reshape(-1, 1)
    return model.predict(future)