import os
import discord
import datetime
from dotenv import load_dotenv
from plugins import game_dev

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')
DEVELOPER = os.getenv('DEVELOPER_NAME')
PROJECT = os.getenv('PROJECT_NAME')
DEV_PHASE = os.getenv('DEVELOPMENT_PHASE')
LOG_PATH = os.getenv('LOG_PATH')

client = discord.Client()


@client.event
async def on_ready():
    for server in client.guilds:
        if server.name == SERVER:
            break

    print(f'The bot user: {client.user} \nConnected to: {server.name}')
    game_dev.plugin_ready(client)


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

    try:
        message_string = message.content
        message_author = message.author
        plugin_response = loaded_plugins.plugin_on_message(
            message_string, message_author
        )
        if plugin_response is not None:
            print(command_log(message.author, message_string))
            await message.channel.send(plugin_response)
    except:
        pass


def command_log(author, command):
    time = datetime.datetime.now()
    time = time.strftime("%d/%m/%y %H:%M:%S")
    log_path = LOG_PATH + "discord_log.log"
    message = f"{time} Served {command} command to: {author}"
    with open(str(log_path), "a") as fw:
        fw.write(str(message) + "\n") 
    return message


client.run(TOKEN)
