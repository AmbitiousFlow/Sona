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
    """
    Main entry point for the Discord bot application.\n
    Initializes the bot and starts it with the provided token.
    """
    console = Console()
    settings = load_discord_settings()
    @app.slash_command(name="play" , description="Play a music from youtube")
    async def play_command(interaction , song:str):
        """ 
        
        """
        from app.commands.play import play
        await play(interaction , song)

    @app.slash_command(name="profile", description="View your profile")
    async def profile_command(interaction, user: disnake.User = None):
        """
        
        """
        from app.commands.profile import profile
        await profile(interaction, user)

    @app.slash_command(name="stop", description="Stop Music")
    async def stop_command(interaction, user: disnake.User = None):
        """
        
        """
        from app.commands.stop import stop
        await stop(interaction)

    console.clear()
    console.print(LOGO)

    @app.event
    async def on_ready():
        console.log(f"[green] 📦 Loaded {len(app.application_commands)} commands [/]")

    time.sleep(2)

    app.run(settings.get("token"))


if __name__ == "__main__":
    main()
