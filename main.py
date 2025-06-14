import sys

sys.dont_write_bytecode = True
from app.configuration.settings import load_discord_settings
from app.app import app
import disnake
from rich.console import Console

import time

LOGO = r"""[blue]

   _____                     ____                  _ _      
  / ____|                   |  _ \                | | |     
 | (___   ___  _ __   __ _  | |_) |_   ___   _____| | | ___ 
  \___ \ / _ \| '_ \ / _` | |  _ <| | | \ \ / / _ \ | |/ _ \
  ____) | (_) | | | | (_| | | |_) | |_| |\ V /  __/ | |  __/
 |_____/ \___/|_| |_|\__,_| |____/ \__,_| \_/ \___|_|_|\___|
                                                                                     
[/]
By     : AmbitiousFlow
Github : https://github.com/ambitiousflow
"""


def main():
    console = Console()
    """
    Main entry point for the Discord bot application.
    Initializes the bot and starts it with the provided token.
    """
    settings = load_discord_settings()

    @app.slash_command(name="play" , description="Play a music from youtube")
    async def play(interaction , song:str):
        """
        
        """
        from app.commands.play_command import play_command
        await play_command(interaction , song)

    @app.slash_command(name="profile", description="View your profile")
    async def profile(interaction, user: disnake.User = None):
        """
        Handles the profile command interaction.
        Returns the user's profile embed.
        """
        from app.commands.profile_command import profile_command
        

        await profile_command(interaction, user)

    console.clear()
    console.print(LOGO)

    @app.event
    async def on_ready():
        console.log("[green]Discord Client Started ![/]")

    time.sleep(2)

    app.run(settings.get("token"))


if __name__ == "__main__":
    main()
