import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the .env file
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Create a new instance of the bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Command registration details
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event listener for when the bot receives a command
@client.event
async def on_interaction(interaction):
    if interaction.type == discord.InteractionType.application_command:
        if interaction.data['name'] == 'ping':
            # Respond with bot's ping (latency)
            await interaction.response.send_message(f'Pong! 🏓 Latency is {round(client.latency * 1000)}ms')

# Register the slash commands
@client.event
async def on_application_command(command):
    if command.name == 'ping':
        await command.response.send_message(f'Pong! 🏓 Latency is {round(client.latency * 1000)}ms')

# Run the bot using the token from .env
client.run(BOT_TOKEN)
