import discord

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

from app.config.config import Config

config = Config()

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(config.get_guild_id))
    print(f'Logged in as {client.user} (ID: {client.user.id})')

@tree.command(name="ping", description=" with Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("!")

def run():
    client.run(config.get_discord_token)