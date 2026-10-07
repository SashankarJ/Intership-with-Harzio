import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "system_metrics.csv")

def load_data():
    return pd.read_csv(DATA_FILE)