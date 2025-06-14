from datetime import datetime
from disnake import Embed, ApplicationCommandInteraction
import disnake
import os


def profile_embed(
    interaction: ApplicationCommandInteraction, user: disnake.User = None
) -> Embed:

    if user is None:
        author = interaction.author
    else:
        author = user

    profile_embed = Embed(
        title="User's Profile",
        description='_"Art is something everyone can share."_',
        colour=0x00B7FF,
        timestamp=datetime.now(),
    )

    profile_embed.set_author(
        name="Ambitious Flow",
        icon_url=os.getenv("DISCORD_BOT_AVATAR"),
    )

    profile_embed.add_field(name="**Username**", value=author.name, inline=True)
    profile_embed.add_field(
        name="**Display Name**", value=author.display_name, inline=True
    )
    profile_embed.add_field(name="Is Bot", value=author.bot, inline=True)
    profile_embed.add_field(name="Joined Discord", value=author.joined_at, inline=True)

    profile_embed.set_thumbnail(url=author.display_avatar.url)

    profile_embed.set_footer(
        text='"A wrong note is just...a happy little accident."',
        icon_url="https://slate.dan.onl/slate.png",
    )

    return profile_embed
