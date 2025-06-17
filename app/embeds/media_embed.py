from disnake import Embed
from disnake import ApplicationCommandInteraction
from datetime import datetime

def media_embed(interaction: ApplicationCommandInteraction, video: dict):
    media_embed = Embed(
        title=video.get("title", "Unknown Title"),
        url=video.get("webpage_url", "https://www.youtube.com"),
        colour=0x00B0F4,
        timestamp=datetime.now(),
    )

    media_embed.set_author(name=video.get("uploader", "Unknown Uploader"))
    
    # Set thumbnail if available
    thumbnail_url = video.get("thumbnail")
    if thumbnail_url:
        media_embed.set_thumbnail(url=thumbnail_url)
    
    # Add video info as fields
    duration = video.get("duration")
    if duration:
        mins, secs = divmod(duration, 60)
        media_embed.add_field(name="Duration", value=f"{mins}:{secs:02d}", inline=True)

    media_embed.add_field(name="Channel", value=video.get("channel", "N/A"), inline=True)
    media_embed.add_field(name="Views", value=f"{video.get('view_count', 0):,}", inline=True)

    # Optional: description or tags
    if video.get("description"):
        media_embed.description = video["description"][:200] + "..." if len(video["description"]) > 200 else video["description"]

    media_embed.set_footer(text=f"Requested by {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)

    return media_embed
