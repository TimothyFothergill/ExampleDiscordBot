# Discord Bot Example
A simple example Discord bot that can read a string on Discord and return a string.
Once a command has been issued, print 

# .env
A dotenv (`.env`) file is required to make this work with the following parameters:
`DISCORD_TOKEN=[[TOKEN HERE]]`
`DISCORD_SERVER=[[SERVER NAME HERE]]`
Further environment variables can be provided and passed in, depending on what functionality you desire the bot to provide.

# Libraries used
Python default libraries: `os`, `datetime`
To run this locally, you'll need to install the following: `discord` and `python-dotenv`.
`pip install -U discord python-dotenv`

# Dockerised Setup
If you have Docker installed, you don't need to get the libraries above. Instead, run these commands once you have setup a .env file in the src/ folder:

Docker Build
`docker build -t discordbot .`
Docker Run
`docker run discordbot` - You may want to append the `-d` flag after "run" (`docker run -d discordbot`) for detached mode, if you don't want to have a terminal dedicated to running the bot. If this is the case, you can shut down the Dockerised container with `docker stop ` and providing it the container id, followed by `docker rm ` and providing it the container id.

# Plugins
