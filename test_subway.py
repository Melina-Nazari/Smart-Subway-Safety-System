import unittest
from subway import SafetyMonitor, SensorReading, Severity


class SafetyMonitorTests(unittest.TestCase):
    def setUp(self):
        self.monitor = SafetyMonitor(fall_distance_cm=30)

    def test_normal_conditions(self):
        result = self.monitor.evaluate(SensorReading("Union", True, 100))
        self.assertEqual(result.severity, Severity.GREEN)
        self.assertFalse(result.notify_security)

    def test_possible_fall(self):
        result = self.monitor.evaluate(SensorReading("Union", True, 20))
        self.assertEqual(result.severity, Severity.YELLOW)

    def test_combined_signals(self):
        result = self.monitor.evaluate(SensorReading("Union", True, 20, True))
        self.assertEqual(result.severity, Severity.RED)

    def test_emergency_button(self):
        result = self.monitor.evaluate(SensorReading("Union", False, 100, emergency_button=True))
        self.assertEqual(result.severity, Severity.RED)

    def test_no_presence_no_fall(self):
        result = self.monitor.evaluate(SensorReading("Union", False, 10))
        self.assertEqual(result.severity, Severity.GREEN)

    def test_invalid_distance(self):
        with self.assertRaises(ValueError):
            self.monitor.evaluate(SensorReading("Union", True, -1))

    def test_history(self):
        self.monitor.evaluate(SensorReading("Union", True, 100))
        self.assertEqual(len(self.monitor.history), 1)


if __name__ == "__main__":
    unittest.main()
