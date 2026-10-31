"""Simulation of the sensor/alert concept in the Smart Subway Safety presentation.

This is a teaching prototype, NOT a validated safety or medical device.
"""
from dataclasses import dataclass
from enum import Enum


class Severity(str, Enum):
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"


@dataclass(frozen=True)
class SensorReading:
    station: str
    ir_presence: bool
    distance_cm: float
    abnormal_bio_signal: bool = False
    emergency_button: bool = False


@dataclass(frozen=True)
class Alert:
    station: str
    severity: Severity
    message: str
    notify_security: bool


class SafetyMonitor:
    """Simple, illustrative threshold rules for simulated sensor inputs."""

    def __init__(self, fall_distance_cm: float = 30.0):
        if fall_distance_cm <= 0:
            raise ValueError("fall_distance_cm must be positive")
        self.fall_distance_cm = fall_distance_cm
        self.history: list[Alert] = []

    def evaluate(self, reading: SensorReading) -> Alert:
        if not reading.station.strip():
            raise ValueError("station must not be empty")
        if reading.distance_cm < 0:
            raise ValueError("distance_cm cannot be negative")

        # A real fall detector requires time-series sensor fusion and validation.
        # This threshold is only a simplified simulation assumption.
        possible_fall = reading.ir_presence and reading.distance_cm < self.fall_distance_cm

        if reading.emergency_button:
            result = Alert(reading.station, Severity.RED, "Emergency button activated", True)
        elif possible_fall and reading.abnormal_bio_signal:
            result = Alert(reading.station, Severity.RED, "Possible fall with abnormal sensor signal", True)
        elif possible_fall:
            result = Alert(reading.station, Severity.YELLOW, "Possible fall detected", True)
        elif reading.abnormal_bio_signal:
            result = Alert(reading.station, Severity.YELLOW, "Abnormal sensor signal", True)
        else:
            result = Alert(reading.station, Severity.GREEN, "Normal simulated conditions", False)

        self.history.append(result)
        return result
