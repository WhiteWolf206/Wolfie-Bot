import discord
from discord.ext import commands
import asyncio
import json
import os

async def update_data(self, ecc, member, amount):
    member_id = str(member.id)
    ecc.setdefault(member_id, {"Name": member.name, "Geld": 0})
    ecc[member_id]["Geld"] += amount

class Eco(commands.Cog):

#eco module still being worked on, give, take, trade, check.

    os.chdir(r'C:\Users\ASUS\Desktop\coding\cogs')

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def addg(self, ctx, member:discord.Member = None, amount = None):
        if member is None:
            await ctx.send("**Please Specify a User.**")
            return
        if amount is None:
        	await ctx.send("**How Much Geld would you like to Add?**")
        member_id = str(member.id)
        with open('eco.json', 'r') as f:
            ecc = json.load(f)
            await update_data(self, ecc, member, amount)

        with open('eco.json', 'w') as f:
            json.dump(ecc, f)

        await ctx.send("✅ **Geld Added**")

def setup(wolfie):
	wolfie.add_cog(Eco(wolfie))