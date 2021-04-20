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
feedback_tokens = []


@client.event
async def on_ready():
    """Writes to console which server the bot has connected to."""
    for server in client.guilds:
        if server.name == SERVER:
            break

    print(f'The bot user: {client.user} \nConnected to: {server.name}')
    game_dev.plugin_ready(client)


@client.event
async def on_message(message):
    if not isinstance(message.channel, discord.DMChannel):
        """Each if block is a command that the bot listens for."""
        if message.content == '!getouttahere':
            response = """Ey, get outta here: \n
    https://www.youtube.com/watch?v=a440-jN8drc"""
            print(command_log(message.content, message))
            await message.channel.send(response)

        if message.content == "!updates":
            response = f"""Currently working on: {PROJECT}\n
    The next phase is: {DEV_PHASE} \n"""
            print(command_log(message.content, message))
            await message.channel.send(response)

        if message.content == "!contact":
            response = f"""Contact @{DEVELOPER} for more assistance"""
            print(command_log(message.content, message))
            await message.channel.send(response)

        if message.content == "!feedback":
            print(command_log(message.content, message))
            await message.author.send(
                "Hi, please leave your feedback. Cancel with !cancel: "
            )
            feedback_tokens.append(FeedbackHandler(message.author))

    if isinstance(message.channel, discord.DMChannel):
        for token in feedback_tokens:
            if token.author == message.author and message.content[0] != "!":
                print(command_log("feedback-recieved", message))
                register_feedback(message.content)
                FeedbackHandler.delete_self(token)
                await message.author.send(
                    "Thank you, your feedback has been received!"
                )
            elif token.author == message.author and message.content == "!cancel":
                print(command_log("feedback-cancelled", message))
                FeedbackHandler.delete_self(token)
                await message.author.send(
                    "Feedback session successfully cancelled."
                    )

    try:
        message_string = message.content
        message_author = message.author
        plugin_response = loaded_plugins.plugin_on_message(
            message_string, message_author
        )
        if plugin_response is not None:
            print(command_log(message_string, message))
            await message.channel.send(plugin_response)
    except Exception:
        pass


def command_log(command, message):
    """Logs which command was used and if it was in a server/channel, or DM."""
    author = message.author
    time = datetime.datetime.now()
    time = time.strftime("%d/%m/%y %H:%M:%S")
    log_path = LOG_PATH + "discord_log.log"
    if isinstance(message.channel, discord.DMChannel):
        message = f"""{time} Served {command} command to: {author} in a DM"""
    else:
        channel = message.channel.name
        server = message.guild.name
        message = f"""{time} Served {command} command to: {author} on {server}, #{channel}"""  # noqa
    with open(str(log_path), "a") as fw:
        fw.write(str(message) + "\n")
    return message

def register_feedback(message):
    """Logs feedback anonymously with datetime."""
    time = datetime.datetime.now()
    time = time.strftime("%d/%m/%y %H:%M:%S")
    log_path = LOG_PATH + "feedback.log"
    message = f"""{time} || {message}"""
    with open(str(log_path), "a") as fw:
        fw.write(str(message) + "\n")


class FeedbackHandler():
    def __init__(self, author):
        self.author = author

    def delete_self(token):
        feedback_tokens.remove(token)
        print("Removed from feedback_tokens")

client.run(TOKEN)
