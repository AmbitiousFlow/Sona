import dotenv

class Config:
    """
    Base configuration class.
    """
    __DISCORD_TOKEN    = None
    __DISCORD_GUILD_ID = None
    def __init__(self):
        dotenv.load_dotenv()
        self.__DISCORD_TOKEN = dotenv.get_key('.env', 'DISCORD_TOKEN')
        self.__DISCORD_GUILD_ID = dotenv.get_key('.env', 'DISCORD_GUILD_ID')
    
    @property
    def get_discord_token(self):
        """
        Returns the Discord token.
        """
        return self.__DISCORD_TOKEN if self.__DISCORD_TOKEN else None
    
    @property
    def get_guild_id(self):
        """
        Returns the Discord guild ID.
        """
        return self.__DISCORD_GUILD_ID if self.__DISCORD_GUILD_ID else None
    