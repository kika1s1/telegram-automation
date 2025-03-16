from telethon import TelegramClient
from app.config import Config
from app.domain.attendance import Attendance
import asyncio

class TelegramTasks:
    def __init__(self):
        self.client = TelegramClient("session", Config.API_ID, Config.API_HASH)
        self.attendance = Attendance()

    async def start(self):
        """Initialize Telegram connection"""
        if not self.client.is_connected():
            await self.client.start(phone=Config.PHONE)
            print("✓ Telegram connection established")

    async def send_message(self, message):
        """Send message to bot"""
        await self.client.send_message(Config.BOT_USERNAME, message)

    async def click_inline_button(self, target_text):
        """Improved button clicking with grid handling"""
        try:
            # Wait for bot to generate buttons
            await asyncio.sleep(4)
            
            async for message in self.client.iter_messages(
                Config.BOT_USERNAME,
                limit=5
            ):
                if message.buttons:
                    print(f"\nFound button message: {message.text}")
                    
                    # Display full button layout
                    for row_num, row in enumerate(message.buttons):
                        print(f"Row {row_num}: {[btn.text for btn in row]}")
                    
                    # Search through all buttons
                    for row_idx, row in enumerate(message.buttons):
                        for col_idx, btn in enumerate(row):
                            if btn.text.strip() == target_text.strip():
                                print(f"Attempting click at ({row_idx}, {col_idx})")
                                
                                # Add visual confirmation of click
                                await asyncio.sleep(1)
                                result = await message.click(row_idx, col_idx)
                                print("✓ Simulated button press")
                                
                                # Verify click success
                                await asyncio.sleep(2)
                                return result
            print("✗ Button grid not found")
            return None
            
        except Exception as e:
            print(f"⚠️ Critical error: {str(e)}")
            return None

    async def checkin(self):
        """Complete checkin workflow with 6-button handling"""
        await self.start()
        
        # Trigger checkin process
        await self.send_message("/checkin")
        print("✓ Check-in command sent")
        
        # Handle 6-button selection
        button_response = await self.click_inline_button("ASTU In Person")
        
        if not button_response:
            return "❌ Failed to select location"
            
        # Finalize checkin
        await asyncio.sleep(3)  # Wait for bot confirmation
        return self.attendance.checkin()

    async def checkout(self):
        """Checkout process"""
        await self.start()
        await self.send_message("/checkout")
        result = self.attendance.checkout()
        print(result)
        return self.attendance.checkout()

    async def close(self):
        """Cleanup connection"""
        await self.client.disconnect()

