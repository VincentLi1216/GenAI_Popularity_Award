import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from main import rank_msg_generator

import os

# 載入環境變數
load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

# 設定指令前綴符號
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'我們已經登入為 {bot.user}')

# 新增 $show_vote 指令
@bot.command(name='show_vote')
async def show_vote(ctx):
    # 假設你想要顯示投票結果的訊息
    vote_result_message = rank_msg_generator()
    await ctx.send(vote_result_message)

# 如果要在某個頻道傳送訊息
async def send_message(message_content):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(message_content)

# 啟動 Bot
if __name__ == "__main__":
    bot.run(TOKEN)
