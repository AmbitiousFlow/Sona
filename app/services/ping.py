from discord.ext import commands
from app.embeds.embed_ping import embed_ping
import discord

async def ping(ctx: discord.Interaction):
    """
    Command to respond with 'Pong!' when invoked.
    Args:
        ctx (commands.Context): The context in which the command was invoked.
    """
    embed_ping.set_footer(icon_url=ctx.user.display_avatar.url , text=f"Requested by {ctx.user.name}")
    await ctx.response.send_message(embed=embed_ping, ephemeral=True)
