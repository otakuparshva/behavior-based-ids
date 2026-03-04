# Behavior-Based Intrusion Detection System (BIDS)

A Python-based intrusion detection system that monitors authentication logs and detects anomalous login behavior using machine learning.

This project simulates login activity, brute-force attacks, and performs real-time behavioral analysis to identify suspicious authentication patterns.

---

## Overview

Traditional intrusion detection often relies on static rules.
This project demonstrates a **behavior-based approach** where login patterns are analyzed to detect anomalies.

The system:

1. Simulates a login system (GUI)
2. Generates brute-force attack attempts
3. Extracts behavioral features from authentication logs
4. Trains a machine-learning model
5. Detects anomalies in real time

---

## Key Features

* Login system simulation using a GUI
* Brute-force attack simulation
* Authentication log monitoring
* Feature extraction from login behavior
* Isolation Forest anomaly detection
* Real-time intrusion detection alerts
* Visualization of anomaly scores

---


## Machine Learning Approach

The system uses **Isolation Forest**, an unsupervised anomaly detection algorithm.

Behavioral features extracted from authentication logs include:

* total login attempts
* failed login attempts
* failure ratio
* rate of login attempts over time

The model is trained on these features and then used to detect abnormal login behavior.

---

## Example Detection Output

```
🚨 ATTACK DETECTED

IP: 192.168.1.140
Attempts: 40
Failed Ratio: 1.0
Rate Change: 6
```

---

## Installation

Clone the repository:

```
git clone https://github.com/otakuparshva/behavior-based-ids.git
cd behavior-based-ids
```

Create virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the System

Start the full system:

```
python run.py
```

The script will:

1. Launch the login GUI
2. Run the attack simulation
3. Train the ML model
4. Start the real-time IDS monitor

---

## Technologies Used

* Python
* Tkinter (GUI)
* Pandas
* Scikit-learn
* Joblib
* Git

---

## Future Improvements

Possible extensions include:

* integration with real system authentication logs
* attack severity classification
* automated IP blocking
* real-time monitoring dashboard

---

## Author

Parshva Shah

GitHub: https://github.com/otakuparshva
