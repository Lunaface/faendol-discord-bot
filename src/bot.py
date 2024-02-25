import os
import discord
from dotenv import load_dotenv
from handlers.messages import handle_message

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents= discord.Intents(guilds=True, guild_messages=True, message_content=True))

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    await handle_message(message)

client.run(TOKEN)