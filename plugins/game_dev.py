import discord

def plugin_ready(client):
    main_client = client
    print(f'Plugins loaded.')


def plugin_message(message):
    print("in plugin_message: " + str(message) )
    if str(message) == "!plugins":
        response = f"Plugins are loaded."
        return response

    if str(message) == "!help":
        response = f"""These are the supported commands:\n
!contact - Details of a contactable developer\n
!help - Displays this list\n
!updates - Current project details\n
"""
        return response
