import pytest
from app.usecases.telegram_tasks import TelegramTasks

@pytest.mark.asyncio
async def test_checkin():
    tasks = TelegramTasks()
    response = await tasks.checkin()
    assert "Checked in at" in response

@pytest.mark.asyncio
async def test_checkout():
    tasks = TelegramTasks()
    response = await tasks.checkout()
    assert "Checked out at" in response
