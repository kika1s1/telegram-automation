import schedule
import asyncio
from app.usecases.telegram_tasks import TelegramTasks
import datetime

tasks = TelegramTasks()

async def run_checkin_coro():
    await tasks.checkin()

async def run_checkout_coro():
    await tasks.checkout()

def schedule_weekday_jobs(loop):
    # Monday to Friday jobs
    for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',"sunday"]:
        # Checkin at 13:00 (1:00 PM)
        getattr(schedule.every(), day).at("13:00").do(
            lambda: asyncio.run_coroutine_threadsafe(run_checkin_coro(), loop)
        )
        # Checkout at 20:00 (8:00 PM)
        getattr(schedule.every(), day).at("20:00").do(
            lambda: asyncio.run_coroutine_threadsafe(run_checkout_coro(), loop)
        )

def schedule_saturday_jobs(loop):
    # Saturday jobs
    schedule.every().saturday.at("08:00").do(
        lambda: asyncio.run_coroutine_threadsafe(run_checkin_coro(), loop)
    )
    schedule.every().saturday.at("13:00").do(
        lambda: asyncio.run_coroutine_threadsafe(run_checkout_coro(), loop)
    )
def schedule_sunday_jobs(loop):
    # Sunday jobs: Checkin at 18:42 (6:42 PM) and Checkout at 18:45 (6:45 PM)
    schedule.every().sunday.at("19:45").do(
        lambda: asyncio.run_coroutine_threadsafe(run_checkin_coro(), loop)
    )
    schedule.every().sunday.at("19:46").do(
        lambda: asyncio.run_coroutine_threadsafe(run_checkout_coro(), loop)
    )

def start_scheduler():
    print("Scheduler started!")
    # Create and set a dedicated event loop for this thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    schedule_weekday_jobs(loop)
    schedule_saturday_jobs(loop)
    schedule_sunday_jobs(loop)

    while True:
        schedule.run_pending()
        # Let the loop run pending tasks briefly
        loop.run_until_complete(asyncio.sleep(1))
