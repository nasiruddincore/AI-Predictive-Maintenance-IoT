import pandas as pd
import numpy as np
import os

def generate_iot_data():
    print("⚙️ Generating Virtual IoT Sensor Data...")
    np.random.seed(42)
    rows = 2000
    
    # Simulate realistic machine telemetry
    temp = np.random.normal(45, 5, rows)
    vibration = np.random.normal(2.5, 0.5, rows)
    current = np.random.normal(10, 1, rows)
    
    # Determine failure rules (High temp + High vibration = Failure)
    failure = np.where((temp > 55) & (vibration > 3.5), 1, 0)
    random_failures = np.random.choice([0, 1], size=rows, p=[0.95, 0.05])
    failure = np.maximum(failure, random_failures)
    
    df = pd.DataFrame({'temperature': temp, 'vibration': vibration, 'current': current, 'failure': failure})
    
    # Save safely
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/sensor_telemetry.csv', index=False)
    print("✅ Success: 2,000 rows saved to data/sensor_telemetry.csv")

if __name__ == "__main__":
    generate_iot_data()