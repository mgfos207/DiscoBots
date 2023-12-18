# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WELCOME_CHID = int(os.getenv('WELCOME_CHID'))

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    for ch in guild.channels:
       print(ch.name, ch.id)

@client.event
async def on_member_join(member):
  print(member.name, "This person has joined!!")
  channel = client.get_channel(WELCOME_CHID) # replace id with the welcome channel's id
  await channel.send(f"Welcome {member.mention} to scire-kila-kitu!")
#   await member.send(f"Thank you for joining {member.guild.name}!")

client.run(TOKEN)