from discord.app_commands import CommandTree
from discord import Client

class Tree(CommandTree):
    def __init__(self , client : Client):
        super().__init__(client)