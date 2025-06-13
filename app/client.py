from .configuration.config import Configuration
from discord import Client
from discord import Intents


class Sona(Client):
    """
    Custom Discord client class that extends the discord.Client.
    This class can be used to add additional functionality or override methods as needed.
    """
    def __init__(self, configuration : Configuration , *args, **kwargs):
        super().__init__(*args, **kwargs , intents=Intents.all())
        self.configuration = configuration

    def run_app(self):
        self.run(self.configuration.get_discord_token)