import discord
from discord.ext import commands
import asyncio
import json
import os

class Eco(commands.Cog):

#########################

def setup(wolfie):
	wolfie.add_cog(Eco(wolfie))
