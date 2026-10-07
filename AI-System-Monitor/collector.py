import psutil
import time
import csv
from datetime import datetime
import os

FILE_PATH = "system_metrics.csv"

def collect_metrics():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net = psutil.net_io_counters().bytes_sent
    timestamp = datetime.now()
    return [timestamp, cpu, ram, disk, net]

# Create file with header if not exists
if not os.path.exists(FILE_PATH):
    os.makedirs("data", exist_ok=True)
    with open(FILE_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "cpu", "ram", "disk", "net"])

with open(FILE_PATH, "a", newline="") as file:
    writer = csv.writer(file)
    while True:
        data = collect_metrics()
        writer.writerow(data)
        print(data)
        time.sleep(5)