import discord


def plugin_ready(client):
    active_client = client
    print('Plugins loaded.')


def plugin_on_message(message, author):
    """Plugins for GameDevBot sit here,
    Use the pattern below to make a plugin."""
    if str(message) == "!plugins":
        response = "Plugins are loaded."
        return response

    if str(message) == "!help":
        response = """These are the supported commands:\n
!contact - Details of a contactable developer\n
!help - Displays this list\n
!updates - Current project details\n
"""
        return response

    if str(message) == "!ashwasere":
        response = """Are you sure?\n
                    Are you certain?
                    It's foobar'd!!!🤖"""
        return response
        
    if str(message) == "!reactme":
        response = """This is a command that is reacted to"""
        return response

    if str(message) == "!play":
        response = "Game coming soon..?"
        return response
