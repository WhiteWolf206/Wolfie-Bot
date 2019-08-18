import discord
from discord.ext import commands
import asyncio
import random

class Fun(commands.Cog):
    def __init__(self, wolfie):
        self.wolfie = wolfie

    @commands.command()
    async def dance(self, ctx):
        embed=discord.Embed()
        embed.set_image(url="https://media.discordapp.net/attachments/462497054430593035/493287977552969735/Konosuba_dbab24_6194110.gif")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def avatar(self, ctx, user : discord.Member = None):
        user = user or ctx.message.author
        embed = discord.Embed()
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)
      
    @commands.command(aliases=['yt'])
    async def youtube(self, ctx, link = None):
        if link == None:
            await ctx.send("Please Specify The link")
            return
        x = f"https://www.youtube.com/watch?v={link}"
        await ctx.send(x)

    @commands.command(aliases=['cf'])
    async def coinflip(self, ctx):

        random_number = random.randint(1, 1000)
        if random_number >= 500:
            text = 'It comes up tails'
        else:
            text = 'It comes up heads'

            header = 'Bot has flipped a coin...'

        embed = discord.Embed()
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
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")

    @commands.command()
    async def weight(self, ctx, weight, typp):
        if typp == "L":
            wei = weight / 0.45
        elif typp == "K":
            wei = weight * 0.45
        else:
            pass
        await ctx.send(wei)

def setup(wolfie):
	wolfie.add_cog(Fun(wolfie))