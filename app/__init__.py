from .configuration.config import Configuration
from .configuration.tree import Tree
from .lib.console import console
from .client import Sona
import discord

__all__ = [
    "Configuration",
    "Tree",
    "console",
    "Sona"
]

app  = Sona(configuration=Configuration())
tree = Tree(app)

from .services.ping import ping

@tree.command(name="ping", description="Responds with 'Pong!'")
async def ping_command(interaction):
    await ping(interaction)

@app.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=app.configuration.get_guild_id))
    console.log("[bold green]Application commands synced![/bold green]")