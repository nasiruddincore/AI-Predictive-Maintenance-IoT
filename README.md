# 🏭 AI-Powered Predictive Maintenance System for IoT Devices

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Frontend](https://img.shields.io/badge/UI-Streamlit-FF4B4B)

An industry-aligned AI platform that simulates industrial IoT sensor telemetry and utilizes a Random Forest classification model to predict machinery failures before they cause operational downtime.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [System Objectives](#-system-objectives)
- [Industry Relevance & Use Cases](#-industry-relevance--use-cases)
- [Architecture & Data Flow](#-architecture--data-flow)
- [Folder Structure](#-folder-structure)
- [Installation & Setup](#-installation--setup)
- [How to Run (Execution Workflow)](#-how-to-run-execution-workflow)
- [Author & License](#-author--license)

---

## 📌 Project Overview
Traditional maintenance is reactive (fixing machines after they break). This project shifts the paradigm to proactive monitoring by analyzing real-time sensor data to catch mechanical anomalies early. It uses a virtual simulation engine to generate realistic telemetry, processes it through a machine learning classifier, and displays actionable alerts on an interactive dashboard.

---

## ⚠️ Problem Statement
* **Unplanned Downtime:** Machine failures halt production lines, costing factories thousands of dollars per hour.
* **Routine Maintenance Waste:** Scheduled maintenance often replaces healthy parts prematurely, wasting resources and labor.
* **Hardware Barriers:** Developing and testing industrial IoT algorithms typically requires access to expensive, heavy machinery and proprietary sensor arrays. 

---

## 🎯 System Objectives
1. **Virtual Telemetry Generation:** Simulate realistic time-series data for motor temperature, vibration, and current.
2. **Machine Learning Classification:** Train a Random Forest model to accurately classify healthy operations versus impending failures based on multi-variable thresholds.
3. **Real-Time Monitoring UI:** Provide an interactive Streamlit dashboard for visual analytics and immediate failure alerts.
4. **Hardware-Free Execution:** Ensure the entire pipeline runs locally on any standard computer without physical IoT components.

---

## 🏭 Industry Relevance & Use Cases
* **Smart Manufacturing (Industry 4.0):** Used by factories to monitor CNC machines, conveyor belts, and robotic arms.
* **Power Plants & Energy:** Tracks turbine and generator health to prevent catastrophic energy grid failures.
* **Aviation & Automotive:** Monitors engine and chassis telemetry to schedule preventative maintenance before transit breakdowns.

---

## 📐 Architecture & Data Flow

```text
[ Virtual Sensor Engine ] ──(Generates Telemetry)──► [ data/sensor_telemetry.csv ]
                                                              │
                                                        (Trains Model)
                                                              ▼
[ Streamlit Dashboard UI ] ◄──(Real-Time Inference)── [ Random Forest ML Model ]
