import sys
sys.dont_write_bytecode = True
from disnake.ext import commands
from app.configuration.settings import load_discord_settings


command_sync_flag = commands.CommandSyncFlags.default()
command_sync_flag.sync_commands_debug = False

settings = load_discord_settings()
app = commands.InteractionBot(test_guilds=[settings.get('guild_id')], command_sync_flags=command_sync_flag)

