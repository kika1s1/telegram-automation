import pytest
import asyncio
from app.usecases.telegram_tasks import TelegramTasks
from datetime import datetime

# A dummy client to simulate Telethon behavior
class DummyClient:
    def __init__(self):
        self.connected = True

    async def start(self, phone):
        self.connected = True

    def is_connected(self):
        return self.connected

    async def send_message(self, recipient, message):
        # Simulate sending a message; simply return True
        return True

    async def iter_messages(self, recipient, limit):
        # Yield a dummy message that contains an inline button with the expected text.
        class DummyButton:
            def __init__(self, text):
                self.text = text

        class DummyMessage:
            def __init__(self):
                self.buttons = [[DummyButton("ASTU In Person")]]
            async def click(self, row_index, col_index):
                return f"Dummy click: row {row_index} col {col_index}"
        yield DummyMessage()

# A fixture to inject the dummy client into TelegramTasks
@pytest.fixture
def tasks_with_dummy_client():
    tasks = TelegramTasks()
    tasks.client = DummyClient()  # override the real client
    return tasks

@pytest.mark.asyncio
async def test_checkin(tasks_with_dummy_client):
    # Call checkin and verify the returned message contains a valid checkin time stamp.
    result = await tasks_with_dummy_client.checkin()
    assert "Checked in at" in result

@pytest.mark.asyncio
async def test_checkout(tasks_with_dummy_client):
    # Call checkout and verify the returned message contains a valid checkout time stamp.
    result = await tasks_with_dummy_client.checkout()
    assert "Checked out at" in result

# Optionally, you can add additional tests to simulate consecutive actions:
@pytest.mark.asyncio
async def test_consecutive_checkin_checkout(tasks_with_dummy_client):
    # Simulate a full cycle: checkin then checkout.
    checkin_result = await tasks_with_dummy_client.checkin()
    checkout_result = await tasks_with_dummy_client.checkout()
    # Verify both results contain the expected strings.
    assert "Checked in at" in checkin_result
    assert "Checked out at" in checkout_result
    # Optionally, compare timestamps (if needed)
    checkin_time_str = checkin_result.split("Checked in at ")[1]
    checkout_time_str = checkout_result.split("Checked out at ")[1]
    # Convert the time strings to datetime objects for further assertions if needed.
    checkin_time = datetime.strptime(checkin_time_str, "%H:%M:%S")
    checkout_time = datetime.strptime(checkout_time_str, "%H:%M:%S")
    # Here we simply print them. You can compare or validate time ordering based on your logic.
    print("Checkin:", checkin_time, "Checkout:", checkout_time)