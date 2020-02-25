import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = '')

@bot.event
async def on_ready():
	print( 'BOT working...' )


async def on_member_join(member):
    channel = bot.get_channel(681139895418355791)

    role = discord.utils.get(member.guild.roles, id = 679769580222021660)

    await member.add_roles(role)
    await channel.send(f'Поприветствуем ``{member.name}``!')



token = open('config.txt',"r").readline()
bot.run(token)
