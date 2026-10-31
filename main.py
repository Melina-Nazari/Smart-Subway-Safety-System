"""Run example simulated subway sensor readings."""
from subway import SafetyMonitor, SensorReading


def main():
    monitor = SafetyMonitor(fall_distance_cm=30)
    scenarios = [
        SensorReading("Union", True, 100),
        SensorReading("Bloor-Yonge", True, 20),
        SensorReading("St George", True, 15, abnormal_bio_signal=True),
        SensorReading("Kipling", True, 100, emergency_button=True),
    ]
    for reading in scenarios:
        alert = monitor.evaluate(reading)
        print(f"{alert.station}: [{alert.severity.value}] {alert.message}")
        if alert.notify_security:
            print("  -> Simulated notification to station security")
    print(f"\nTotal readings logged: {len(monitor.history)}")


if __name__ == "__main__":
    main()
