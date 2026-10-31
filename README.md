# 🚇 Smart Subway Safety System
### Python-Based Sensor Monitoring & Emergency Alert Simulation

A Python-based safety monitoring system designed to explore how sensor-assisted technologies can improve passenger safety in public transit environments.

The project originated from an engineering design concept focused on detecting potentially dangerous situations in subway stations and supporting faster emergency response. It was subsequently extended into a Python simulation demonstrating **object-oriented software design, sensor-data processing, automated alert classification, and unit testing**.

## Project Overview

Public transit stations experience high passenger volumes, making it challenging for security personnel to identify emergencies immediately.

The Smart Subway Safety System explores a modular approach to automated safety monitoring using simulated sensor readings and rule-based decision-making.

The system evaluates environmental and safety indicators, assigns an appropriate alert severity, and generates simulated notifications for station personnel.

### Key Features

**1. Sensor-Based Monitoring**

The simulation models inputs from three proposed sensor technologies:

- **Infrared (IR):** Represents human presence detection.
- **Ultrasonic:** Represents distance measurements used to identify potential falls or sudden changes in position.
- **Bioimpedance:** Represents an abnormal sensor-signal indicator for exploring potential distress scenarios.

An additional emergency-button input allows critical alerts to be triggered manually.

**2. Automated Emergency Classification**

A rule-based monitoring system categorizes simulated station conditions into three severity levels:

| Status | Classification | System Response |
|---|---|---|
| 🟢 GREEN | Normal | No emergency notification |
| 🟡 YELLOW | Warning | Potential safety concern detected |
| 🔴 RED | Critical | High-priority emergency alert generated |

Critical conditions take priority when multiple indicators are detected.

**3. Emergency Alert Generation**

When the monitoring system identifies a warning or critical condition, it generates an alert containing the station name, severity, and reason for detection.

The application demonstrates a notification workflow through terminal output, representing how information could be communicated to transit security personnel.

**4. Object-Oriented Software Architecture**

The application uses Python classes and structured data models to separate sensor inputs, alert classification, and monitoring responsibilities.

Key software engineering concepts include:

- Object-oriented programming (OOP)
- Python dataclasses and enumerations
- Input validation
- Rule-based decision-making
- Modular software architecture
- Alert history tracking
- Automated unit testing

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python 3 |
| Software Design | Object-Oriented Programming, Dataclasses, Enums |
| Testing | Python `unittest` |
| Development Tools | Visual Studio Code, Git, GitHub |
| System Concepts | Sensor Simulation, Safety Monitoring, Alert Classification |

## Example Simulation Results

The application demonstrates four example station-monitoring scenarios using predefined sensor readings.

| Subway Station | Status | Detected Condition |
|---|---|---|
| Union | 🟢 GREEN | Normal simulated conditions |
| Bloor-Yonge | 🟡 YELLOW | Possible fall detected |
| St George | 🔴 RED | Possible fall with abnormal sensor signal |
| Kipling | 🔴 RED | Emergency button activated |

The station names are illustrative; the program does not access live TTC data.

### Example Terminal Output

```text
Union: [GREEN] Normal simulated conditions

Bloor-Yonge: [YELLOW] Possible fall detected
  -> Simulated notification to station security

St George: [RED] Possible fall with abnormal sensor signal
  -> Simulated notification to station security

Kipling: [RED] Emergency button activated
  -> Simulated notification to station security

Total readings logged: 4
```

## Getting Started

### Prerequisites

- Python 3
- Visual Studio Code or another Python-compatible editor

### Installation

Clone the repository:

```bash
git clone https://github.com/Melina-Nazari/Smart-Subway-Safety-System.git
```

Navigate to the project directory:

```bash
cd Smart-Subway-Safety-System
```

### Run the Simulation

```bash
python3 main.py
```

The program processes predefined sensor readings and displays the corresponding safety classifications and simulated notifications.

## Automated Testing

The project includes unit tests using Python's built-in `unittest` framework.

The test suite evaluates monitoring behaviour, including normal conditions, emergency classifications, and input validation.

Run the tests using:

```bash
python3 -m unittest discover -s tests -v
```

The tests help verify that the software behaves consistently across the implemented scenarios.

## Project Structure

```text
Smart-Subway-Safety-System/
│
├── main.py
├── subway.py
├── README.md
│
└── tests/
    └── test_subway.py
```

**main.py** — Runs predefined station-monitoring scenarios and displays results.

**subway.py** — Contains sensor data models, severity classifications, monitoring logic, and alert handling.

**tests/test_subway.py** — Contains automated tests for the monitoring system.

## Engineering Design Background

The original Smart Subway Safety System concept explored the integration of infrared, ultrasonic, and bioimpedance sensing technologies with a microcontroller and LED-based warning indicators.

The proposed system followed a four-stage process:

1. Collect sensor measurements in high-risk transit areas.
2. Analyze incoming signals using a microcontroller.
3. Categorize potential safety concerns using green, yellow, and red indicators.
4. Communicate alerts to station personnel.

The Python implementation extends this concept by providing a software environment for exploring monitoring rules, simulated emergency scenarios, and automated testing.

## Future Improvements

Potential extensions include:

- **Arduino integration
