from datetime import datetime

class Attendance:
    def __init__(self):
        self.checkin_time = None
        self.checkout_time = None

    def checkin(self):
        self.checkin_time = datetime.now()
        return f"Checked in at {self.checkin_time.strftime('%H:%M:%S')}"

    def checkout(self):
        self.checkout_time = datetime.now()
        return f"Checked out at {self.checkout_time.strftime('%H:%M:%S')}"
