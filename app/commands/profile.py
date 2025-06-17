import sys
sys.dont_write_bytecode = True
from app.embeds.profile_embed import profile_embed
import disnake


async def profile(interaction: disnake.ApplicationCommandInteraction , user:disnake.User=None):
    """
    Handles the profile command interaction.
    Returns the user's profile embed.
    """
    embed = profile_embed(interaction , user)
    await interaction.response.send_message(embed=embed)