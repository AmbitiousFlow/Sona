import sys
sys.dont_write_bytecode = True
import disnake
import yt_dlp
import asyncio
from app.embeds.media import media_embed

yt_options = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

async def play(interaction: disnake.ApplicationCommandInteraction , song : str):
    """Play a song from YouTube in the user's voice channel."""
    await interaction.response.defer()

    if not interaction.user.voice or not interaction.user.voice.channel:
        await interaction.followup.send("You need to be in a voice channel to play music!", ephemeral=True)
        return

    voice_channel = interaction.user.voice.channel

    voice_client = interaction.guild.voice_client
    if not voice_client:
        try:
            voice_client = await voice_channel.connect()
        except Exception as e:
            await interaction.followup.send(f"Failed to connect to voice channel: {str(e)}", ephemeral=True)
            return

    # Search for the song using yt-dlp
    try:
        with yt_dlp.YoutubeDL(yt_options) as ydl:
            info = ydl.extract_info(f"ytsearch:{song}", download=False)
            if 'entries' in info:
                info = info['entries'][0]
            url = info['url']
            
    except Exception as e:
        await interaction.followup.send(f"Error finding song: {str(e)}", ephemeral=True)
        return
    
    try:
        source = disnake.FFmpegPCMAudio(url, **ffmpeg_options , executable="D:\\Projects\\Sona\\utils\\ffmpeg\\bin\\ffmpeg.exe")
    except Exception as e:
        await interaction.followup.send(f"Error creating audio source: {str(e)}", ephemeral=True)
        return

    # Play the audio
    try:
        if voice_client.is_playing():
            voice_client.stop() 
        voice_client.play(source, after=lambda e: print(f"🎶Player error: {e}") if e else None)
        await interaction.followup.send(embed=media_embed(interaction , info))
    except Exception as e:
        await interaction.followup.send(f"Error playing song: {str(e)}", ephemeral=True)
        return
    ...
