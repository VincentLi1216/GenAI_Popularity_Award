import discord
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
intents.message_content = True

async def send_message(message_content):
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'我們已經登入為 {client.user}')
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(message_content)
        await client.close()

    await client.start(TOKEN)

# 如果想測試傳送訊息，可以使用以下的方式
if __name__ == "__main__":
    asyncio.run(send_message('testing'))
