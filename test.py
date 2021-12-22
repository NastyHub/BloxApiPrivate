import discord
import os
import json
from discord.ext import commands, tasks
from discord_components import DiscordComponents, ComponentsBot, Button, component, interaction
from function import search as s

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True

client = ComponentsBot(command_prefix = '!', intents=intents)
client.remove_command('help')

##########################################################################
@client.event
async def on_ready():
    game = discord.Game(name = "판매 돕는 중")
    await client.change_presence(activity = game)

    print("Ready to Run")


@client.command()
async def what(ctx, what=None):
    await ctx.send(s.smart_user_algorithm(what))



client.run("OTIzMjAwMzc0MzkzOTYyNTE2.YcMjWQ.3u8aweRZ0ug8E5BJNu16yAbFaEw")