import sys
sys.dont_write_bytecode = True
from app.configuration.settings import load_discord_settings
from app.app import app
import disnake
from rich.console import Console



def main():
    console = Console()
    """
    Main entry point for the Discord bot application.
    Initializes the bot and starts it with the provided token.
    """
    settings = load_discord_settings()

    @app.slash_command(name="profile", description="View your profile")
    async def profile(interaction , user : disnake.User = None):
        """
        Handles the profile command interaction.
        Returns the user's profile embed.
        """
        from app.commands.profile_command import profile_command
        await profile_command(interaction , user)

    console.log("[green]Started discord client[/]")

    app.run(settings.get('token'))
    
if __name__ == "__main__":
    main()