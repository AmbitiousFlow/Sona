import sys

sys.dont_write_bytecode = True
import disnake
import asyncio


async def stop(interaction: disnake.ApplicationCommandInteraction):
    voice = interaction.guild.voice_client

    if not voice:
        await interaction.response.send_message("I'm not connected to a voice channel.", ephemeral=True)
        return

    if not voice.is_playing():
        await interaction.response.send_message("There's no music playing right now.", ephemeral=True)
        return

    voice.stop()
    await voice.disconnect()

    await interaction.response.send_message("Music stopped and disconnected from the voice channel.")
