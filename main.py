from discord.ext import commands
from AntiScam import AntiScam

whitelist = [652487170380267520]
logs_channel =915619809272692836

bot = commands.Bot(command_prefix='>')
bot.remove_command('help') # Remove this line if you want to use the help command.

@bot.listen()
async def on_message(message):
    await AntiScam(message, bot = bot, whitelist = whitelist, muted_role='Muted', verified_role='Verified', logs_channel=logs_channel) # Here you can change the names of the roles.

bot.run('OTE1NjE2Njc3MTE3NDU2NDA0.YaeMew.iOuyQolIB2mJdsULf9JV_uB56E8')
