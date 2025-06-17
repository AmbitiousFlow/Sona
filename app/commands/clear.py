import sys
sys.dont_write_bytecode = True
import disnake
from disnake.ext import commands

@commands.has_permissions(manage_messages=True)
async def clear(interaction: disnake.ApplicationCommandInteraction,amount: int = commands.Param(description="Number of messages to delete (1-100)")):
    if amount < 1 or amount > 100:
        await interaction.response.send_message("Please enter a number between 1 and 100.", ephemeral=True)
        return

    await interaction.response.defer(ephemeral=True)  # Defer before bulk action
    deleted = await interaction.channel.purge(limit=amount)
    await interaction.followup.send(f"🧹 Deleted {len(deleted)} messages.", ephemeral=True)
