# Smart Subway Safety System — Python Simulation

A Python extension of an engineering design concept for a sensor-assisted subway safety alert system. The original presentation proposed IR, ultrasonic, and bioimpedance sensors, a microcontroller, and green/yellow/red LED alerts with notifications to station staff.

## What this repository does

- Simulates human presence (IR), distance (ultrasonic), and an abnormal bio-signal flag.
- Uses illustrative rules to categorize simulated conditions as GREEN, YELLOW, or RED.
- Prints simulated station-security notifications for warning and critical alerts.
- Stores alert results in memory and includes automated unit tests.

**Limitations:** No physical sensors, Arduino, LED hardware, TTC data, real-time feeds, actual security integrations, or medically validated detection are included. A single distance threshold cannot reliably detect falls. Bioimpedance-based injury detection is a concept from the presentation, not an established capability of this simulation. This project must not be used for real-world safety decisions.

## Run

From the project root:

```bash
python3 main.py
python3 -m unittest discover -s tests -v
```

## Files

- `subway.py`: data structures, alert rules, and history
- `main.py`: example sensor readings
- `tests/test_subway.py`: unit tests

## Background

This is a **subsequent software simulation** based on the original Smart Subway Safety System presentation, not evidence that this Python implementation existed during the original workshop.
