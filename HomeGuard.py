class HomeGuard:
    def __init__(self):
        self.mode = "home"
        self.min_temp = 65
        self.max_temp = 75

    def set_mode(self, mode):
        self.mode = mode.lower()
        print(f"System mode is now {self.mode}")

    def process_sensors(self, motion, door, temperature, smoke):
        alerts = []

        # Check security
        if self.mode == "away":
            if motion:
                alerts.append("Alert: Motion detected while away.")
            if door:
                alerts.append("Alert: Door opened while away.")

        if motion and door:
            alerts.append("Alert: Possible break-in.")

        # Check safety
        if temperature < 35:
            alerts.append("Alert: Temperature is too low.")
        elif temperature > 95:
            alerts.append("Alert: Temperature is too high.")

        if smoke:
            alerts.append("Alert: Smoke detected.")

        # Check comfort
        if self.mode == "home":
            if temperature < self.min_temp or temperature > self.max_temp:
                alerts.append("Notice: Temperature is outside comfort range.")

        return alerts


# Run the program
system = HomeGuard()
system.set_mode("away")

alerts = system.process_sensors(
    motion=True,
    door=True,
    temperature=30,
    smoke=False
)

for alert in alerts:
    print(alert)
    