import os
import discord
import datetime
from dotenv import load_dotenv

load_dotenv()
# TODO: Turn into function and call only when needed.
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')
DEVELOPER = os.getenv('DEVELOPER_NAME')
PROJECT = os.getenv('PROJECT_NAME')
DEV_PHASE = os.getenv('DEVELOPMENT_PHASE')

client = discord.Client()

@client.event
async def on_ready():
    for server in client.guilds:
        if server.name == SERVER:
            break

    print(f'The bot user: {client.user} \nConnected to: {server.name}')

@client.event
async def on_message(message):
    if message.content == '!getouttahere':
        response = """Ey, get outta here: \n
https://www.youtube.com/watch?v=a440-jN8drc"""
        print(command_log(message.author, message.content))
        await message.channel.send(response)

    if message.content == "!updates":
        response = f"""Currently working on: {PROJECT}\n
The next phase is: {DEV_PHASE} \n"""
        print(command_log(message.author, message.content))
        await message.channel.send(response)

    if message.content == "!contact":
        response = f"""Contact @{DEVELOPER} for more assistance"""
        print(command_log(message.author, message.content))
        await message.channel.send(response)

def command_log(author, command):
    time = datetime.datetime.now()
    time = time.strftime("%d/%m/%y %H:%M:%S")
    message = f"{time} Served {command} command to: {author}"
    return message

client.run(TOKEN)
