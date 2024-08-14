from telethon import TelegramClient, events
import time

api_id = 24933371  # Your API ID
api_hash = '194530766421e5b1db470d2efd93b5f5'  # Your API Hash

# Create the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# স্ক্রিপ্ট শুরু হওয়ার সময় সেভ করুন
start_time = time.time()

# আপটাইম চেক করার জন্য হ্যান্ডলার
@client.on(events.NewMessage(pattern='(?i)uptime'))
async def uptime(event):
    current_time = time.time()
    uptime_seconds = int(current_time - start_time)
    
    # সেকেন্ড থেকে ঘন্টা, মিনিট এবং সেকেন্ডে কনভার্ট করুন
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # ফলাফল দেখান
    uptime_message = f"Uptime: {hours}h {minutes}m {seconds}s"
    await event.reply(uptime_message)

# ক্লায়েন্ট রান করুন
with client:
    client.run_until_disconnected()
  
