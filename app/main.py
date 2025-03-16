import threading
from app.services.scheduler import start_scheduler

if __name__ == "__main__":
    print("Starting Telegram Automation...")
    scheduler_thread = threading.Thread(target=start_scheduler)
    scheduler_thread.daemon = True  # This makes the thread exit with the main thread
    scheduler_thread.start()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Shutting down...")
        
