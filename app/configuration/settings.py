import dotenv


def load_discord_settings():
    dotenv.load_dotenv()
    """
    Load Discord settings from the environment variables.
    """
    import os

    return {
        "token": os.getenv("DISCORD_TOKEN"),
        "guild_id": int(os.getenv("DISCORD_GUILD_ID", 0)),
    }

