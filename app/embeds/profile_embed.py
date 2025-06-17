from disnake import Embed, ApplicationCommandInteraction, User
from datetime import datetime
import os

def profile_embed(interaction: ApplicationCommandInteraction, user: User = None) -> Embed:
    author = user or interaction.author

    profile_embed = Embed(
        title=f"{author.display_name}'s Profile 🎭",
        description="> _“Art is something everyone can share.”_",
        colour=0x00B7FF,
        timestamp=datetime.now(),
    )

    profile_embed.set_author(
        name="Ambitious Flow",
        icon_url=os.getenv("DISCORD_BOT_AVATAR"),
    )

    profile_embed.set_thumbnail(url=author.display_avatar.url)

    # Basic Identity
    profile_embed.add_field(name="👤 Username", value=f"`{author.name}`", inline=True)
    profile_embed.add_field(name="📛 Display Name", value=f"`{author.display_name}`", inline=True)
    profile_embed.add_field(name="🤖 Bot", value="Yes" if author.bot else "No", inline=True)

    # Join Date
    if hasattr(author, "joined_at") and author.joined_at:
        joined_date = author.joined_at.strftime("%B %d, %Y")
        profile_embed.add_field(name="📅 Joined Discord", value=joined_date, inline=False)

    # Footer with personality
    profile_embed.set_footer(
        text="🎨 “A wrong note is just... a happy little accident.”",
    )

    return profile_embed
