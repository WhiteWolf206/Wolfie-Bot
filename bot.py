import discord
from discord.ext import commands
import asyncio
import random
import logging
import time
import os

wolfie = commands.Bot(command_prefix="w!")
logging.basicConfig(level="INFO")
wolfie.remove_command("help")

wolfie.load_extension("cogs.mod")
wolfie.load_extension("cogs.fun")
wolfie.load_extension("cogs.eco")

@wolfie.listen()
async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("**Permission Denied**")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**That is not a Command**")

        raise error

@wolfie.listen()
async def on_member_join(self, member):
    if member.wolfie == False:
        embed = discord.Embed(title=f"{member.name}#{member.discriminator}",color=0x009933)
        embed.add_field(name=f"Creation Date",value=f" {member.created_at.strftime('%B %d, %Y')}",inline=True)
        embed.add_field(name=f"Join Date", value=f" {member.joined_at.strftime('%B %d, %Y')}",inline=True)
        embed.add_field(name=f"Member Count", value=f" {member.guild.member_count}")
        embed.set_author(name="Member Joined",icon_url=member.avatar_url)
        try:
            channel = discord.utils.get(member.guild.channels, name="")
            await channel.send(embed=embed)
            role = discord.utils.get(member.guild.roles, name="")
            await member.add_roles(role)
        except:
            channel = discord.utils.get(member.guild.channels, name="")
            await channel.send(embed=embed)
            role = discord.utils.get(member.guild.roles, name="")
            await member.add_roles(role)
    else:
        embed = discord.Embed(title=f"BOT {member.name}#{member.discriminator}",color=0x009933)
        embed.add_field(name=f"Creation Date",value=f" {member.created_at.strftime('%B %d, %Y')}",inline=True)
        embed.add_field(name=f"Join Date", value=f" {member.joined_at.strftime('%B %d, %Y')}",inline=True)
        embed.set_author(name="Member Joined",icon_url=member.avatar_url)
        try:
            channel = discord.utils.get(member.guild.channels, name="")
            await channel.send(embed=embed)
        except:
            channel = discord.utils.get(member.guild.channels, name="")
            await channel.send(embed=embed)
    
@wolfie.listen()
async def on_member_remove(self, member):
    now = datetime.now()
    if member.wolfie == False:
        embed = discord.Embed(title=f"{member.name}#{member.discriminator}",color=0xff0000)
        embed.add_field(name=f"Join Date", value=f" {member.joined_at.strftime('%B %d, %Y')}",inline=True)
        embed.add_field(name=f"Leave Date", value=f" {now.strftime('%B %d, %Y')}",inline=True)
        embed.add_field(name=f"Member Count", value=f" {member.guild.member_count}")
        embed.set_author(name="Member Left",icon_url=member.avatar_url)
        try:
            channel = discord.utils.get(member.guild.channels, name="")
            await channel.send(embed=embed)
        except:
            pass


@wolfie.listen()
async def on_ready():
    print(f"Bot ready!")
    game = discord.Game(f" Starting out Strong! | User Count: {len(wolfie.guilds)}")
    await wolfie.change_presence(status=discord.Status.online,activity=game)
    print(f"Playing {game}")

#✅

@wolfie.command(aliases=['latency'])
async def ping(ctx):
    ping_ = wolfie.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send(f"**Ping Value is {ping}ms**")

@wolfie.command(aliases=['git'])
async def github(ctx):
    embed = discord.Embed(title="Github Link",description="(https://github.com/WhiteWolf206/Wolfie-DB)",color=0x00FF00)
    await ctx.send(embed=embed)

@wolfie.command(aliases=['info'])
async def user(ctx, member:discord.Member):
    name = f"{member.name}#{member.discriminator}"
    status = member.status
    joined = member.joined_at
    role = member.top_role

    embed = discord.Embed(
        title=f'{name}', colour=discord.Colour.blue(
            )
        )
    embed.set_thumbnail(url=f'{member.avatar_url}')
    embed.add_field(name=f"Status", value=f"{status}",inline=True)
    embed.add_field(name=f"Joined at", value=f"{joined}",inline=True)
    embed.add_field(name=f"Highest Role", value=f"{role}",inline=True)
    await ctx.send(embed=embed)

@wolfie.command(aliases=['sinfo', 'si'])
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(
        title=f'{guild.name}', colour=discord.Colour.blue(
            )
        )
    embed.set_thumbnail(url=f'{guild.icon_url}')
    embed.add_field(name="Server Created in :", value=f'''  {guild.created_at.strftime('%B %d, %Y at %I:%M %p')}''', inline=False)
    embed.add_field(name="Created by :", value=f'''{guild.owner.mention}''',inline=False)
    embed.add_field(name='Region :', value=f'''  {guild.region}''',inline=False)
    embed.add_field(name='Server ID :', value=f'''{guild.id}''',inline=False)
    embed.add_field(name='Server Members :', value=f'''  {len(guild.members)}''', inline=False)
    embed.add_field(name='Online Members :',value=f'''{len([I for I in guild.members if I.status is discord.Status.online])}''',inline=False)
    await ctx.send(embed=embed)

@wolfie.command()
async def owner(ctx):
    await ctx.send(f"{ctx.guild.owner.mention} **Is the Owner of this Guild/Server**"
        )

@wolfie.command()
async def help(ctx):
    member = ctx.message.author
    embed = discord.Embed(
        title=f'Help', colour=discord.Colour.blue(
            )
        )
    embed.add_field(name=f"Ping", value=f"Returns the bots latency",inline=False)
    embed.add_field(name=f"Github", value=f"Returns the bots Github Page",inline=False)
    embed.add_field(name=f"User", value=f"Returns Information about specified User",inline=False)
    embed.add_field(name=f"Serverinfo", value=f"Returns Information about the Server the Message is sent in",inline=False)
    embed.add_field(name=f"Owner", value=f"Mentions the Owner",inline=False)
    embed.add_field(name=f"Avatar", value=f"Returns a Picture of the user's Avatar (Not the movie lol)",inline=False)
    embed.add_field(name=f"Dance", value=f"Returns a Dancing GIF",inline=False)
    embed.add_field(name=f"Slot", value=f"Roll a Slot Machine",inline=False)
    embed.add_field(name=f"Youtube", value=f"Returns the Youtube video specfied",inline=False)
    embed.add_field(name=f"Youtube Usage", value=f"In your Browser Link there should Letters after ``watch?v=``, copy them as the link",inline=False)        
    embed.add_field(name=f"Coinflip", value=f"Well, It does as it says, Returns an outcome of a random coinflip",inline=False)
    await member.send(embed=embed)
    await ctx.send("**A List of all the commands has been Sent to your DMs**")

wolfie.run("No No")
