import discord
from discord.ext import commands
import asyncio
import random

class Fun(commands.Cog):
    def __init__(self, wolfie):
        self.wolfie = wolfie

    @commands.command()
    async def dance(self, ctx):
        embed=discord.Embed(colour=discord.Colour.blue)
        embed.set_image(url="https://media.discordapp.net/attachments/462497054430593035/493287977552969735/Konosuba_dbab24_6194110.gif")
        await ctx.send(embed=embed)

    @commands.command(aliases=['cf'])
    async def coinflip(self, ctx):

        random_number = random.randint(1, 1000)
        if random_number >= 500:
            text = 'It comes up tails'
        else:
            text = 'It comes up heads'

            header = 'Bot has flipped a coin...'

        embed = discord.Embed(colour=discord.Colour.blue)
        embed.add_field(name=header, value=text, inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['slots'])
    async def slot(self, ctx):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(embed=discord.Embed(title=f"{slotmachine} All matching, you won! 🎉"))
            await ctx.send(embed=embed1)
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(embed=discord.Embed(title=f"{slotmachine} 2 in a row, you won! 🎉"))
        else:
            await ctx.send(embed=discord.Embed(title=f"{slotmachine} No match, you lost 😢"))

    @commands.command()
    async def weight(self, ctx, weight, typp):
        if typp == "Kilograms":
            wei = weight / 0.45
            await ctx.send(embed=discord.Embed(title=f"{wei}Kgs", colour=discord.Colour.blue))
        elif typp == "Pounds":
            wei = weight * 0.45
            await ctx.send(embed=discord.Embed(title=f"{wei}Lbs", colour=discord.Colour.blue))
        else:
            pass

def setup(wolfie):
	wolfie.add_cog(Fun(wolfie))
