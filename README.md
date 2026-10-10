# 🏭 AI-Powered Predictive Maintenance System for IoT
An industry-aligned AI platform that simulates industrial IoT sensor telemetry and utilizes a Random Forest classification model to predict machine failures before they cause operational downtime.

### Features
* **Virtual Sensor Engine:** Generates synthetic temperature, current, and vibration data.
* **Machine Learning:** Scikit-learn predictive model trained for anomaly classification.
* **Real-Time Dashboard:** Streamlit UI for visual analytics and simulated hardware threshold alerts.

### Quick Start
1. `pip install -r requirements.txt`
2. `python src/simulate_sensors.py` && `python src/train_model.py`
3. `streamlit run dashboard/app.py`