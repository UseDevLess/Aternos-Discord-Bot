from python_aternos import Client
from discord.ext import commands
import os, discord

### CHANGE THESE VARIABLES ###
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"
TOKEN = "BOT TOKEN"
SERVER_NUM = 1
PRESENCE_TYPE = ""
PRESENCE_NAME = ""
STREAM_URL = ""
START_COMMAND = "!start"
START_SUCCESS = "The server is starting right up, {author.name}!"
START_FAIL = "The server is already up or is starting up, {author.name}!"
### CHANGE THESE VARIABLES ###

at = Client.from_credentials(username, password)
server = at.list_servers()[SERVER_NUM-1]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")
    if PRESENCE_TYPE.lower() == "playing":
      await client.change_presence(activity=discord.Game(PRESENCE_NAME))
    elif PRESENCE_TYPE.lower() == "streaming":
      await client.change_presence(activity=discord.Streaming(name=PRESENCE_NAME, url=STREAM_URL))
    elif PRESENCE_TYPE.lower() == "watching":
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=PRESENCE_NAME))
    elif PRESENCE_TYPE.lower() == "listening":
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=PRESENCE_NAME))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == START_COMMAND:
        try:
            server.start()
            await message.channel.send(format(START_SUCCESS.replace("{author}", "{message.author}").replace("{author.name}", "message.author.name").replace("{author.id}", "{message.author.id}")))
        except:
            await message.channel.send(format(START_FAIL.replace("{author}", "{message.author}").replace("{author.name}", "message.author.name").replace("{author.id}", "{message.author.id}")))

client.run(TOKEN)
