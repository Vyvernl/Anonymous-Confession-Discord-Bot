import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
intents.typing = True
intents.presences = False

Settings = {
    'Token': 'Enter Token',
    'Activity Text': 'dingleberry',
    'Prefix': '.'
}
Client = commands.Bot(command_prefix=Settings['Prefix'], intents=intents)

@Client.event
async def on_ready():
    await Client.change_presence(activity=discord.Game(name=Settings['Activity Text']))
    print(f'Launched')

@Client.command(name='setchannel')
async def setchannel(ctx, channel: discord.TextChannel):
    if ctx.author.guild_permissions.administrator:
        global confessionChannel
        confessionChannel = channel
        await ctx.send(f"We've set the anonymous confession channel to {channel}.")
    else:
        response = await ctx.send('You are not allowed to use this command.')
        await response.delete()

@Client.command(name='confess')
async def confess(ctx, type, *confession):
    global confessionChannel
    await ctx.message.delete()
    response = await ctx.send('Sent your confession!')
    confession_text = ' '.join(confession)
    if type == "no" or type == "No":
        await confessionChannel.send(f"Confession by: Anonymous\n**{confession_text}**")
    else:
        await confessionChannel.send(f"Confession by: {ctx.author.user}\n**{confession_text}**")
    await asyncio.sleep(5)
    await response.delete()

Client.run(Settings['Token'])
    
