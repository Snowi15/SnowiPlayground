from telethon import TelegramClient, events
import pandas as pd  # Import pandas for handling CSV files

# Replace with your details
API_ID = '22941664'
API_HASH = '2ee02d39b9a6dae9434689d46e0863ca'
PHONE_NUMBER = '+918618221717'

# Create a client session
client = TelegramClient('session_name', API_ID, API_HASH)

async def send_message():
    # Use a raw string for the file path to avoid unicode escape errors
    client_data = pd.read_excel(r"C:\Users\user\Desktop\CheetiClient.csv")
    # Iterate through each row in the DataFrame
    for index, row in client_data.iterrows():
        message = row['Message']  # Assuming there is a 'Message' column for personalized messages
        await client.send_message(830726191, "Hi!Beautiful")

@client.on(events.NewMessage)
async def auto_reply(event):
    if event.is_private:  # Only reply to private messages
        await event.reply('This is an auto-reply message!')

# Start the client
with client:
    client.loop.run_until_complete(send_message())
    client.run_until_disconnected()
