import dotenv

class Configuration:
    """
    Configuration class for loading and accessing Discord-related environment variables.
    This class loads environment variables from a `.env` file using the `dotenv` package.
    It provides properties to access the Discord bot token and guild ID.
    Attributes:
        __DISCORD_TOKEN (str or None): The Discord bot token loaded from the `.env` file.
        __DISCORD_GUILD_ID (str or None): The Discord guild ID loaded from the `.env` file.
    Methods:
        get_discord_token (property): Returns the Discord bot token if available, otherwise None.
        get_guild_id (property): Returns the Discord guild ID if available, otherwise None.
    """
    dotenv.load_dotenv()

    __DISCORD_TOKEN    = None
    __DISCORD_GUILD_ID = None

    def __init__(self):
        self.__DISCORD_TOKEN    = dotenv.get_key('.env', 'DISCORD_TOKEN')
        self.__DISCORD_GUILD_ID = dotenv.get_key('.env', 'DISCORD_GUILD_ID')
    
    @property
    def get_discord_token(self):
        return self.__DISCORD_TOKEN if self.__DISCORD_TOKEN else None
    
    @property
    def get_guild_id(self):
        return self.__DISCORD_GUILD_ID if self.__DISCORD_GUILD_ID else None
