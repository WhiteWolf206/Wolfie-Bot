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
###wolfie.load_extension("cogs.eco")

@wolfie.listen()
async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("**Access not Granted, Whoops!**")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**That Command isn't part of my Code.**")

        raise error

'''@wolfie.listen()
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
            pass'''


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
    embed = discord.Embed(
        title=f'The ping is {ping}ms', colour=discord.Colour.blue(
            )
        )
    await ctx.send(embed=embed) 

@wolfie.command(aliases=['git'])
async def github(ctx):
    embed = discord.Embed(title="Github Link",description="(https://github.com/WhiteWolf206/Wolfie-DB)",colour=discord.Colour.blue)
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
async def avatar(ctx, user : discord.Member = None):
    user = user or ctx.message.author
    embed = discord.Embed(colour=discord.Colour.blue)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)

@wolfie.command()
async def owner(ctx):
    embed = discord.Embed(
        title=f'{ctx.guild.owner} is the Owner of this Server', colour=discord.Colour.blue(
            )
        )
    await ctx.send(embed=embed)

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
    embed.add_field(name=f"Mod Commands", value=f"If you are a Member of Staff, You Will Be Told a Secret Command for Mod Commands, If you are not a Members of Staff, Stop Trying",inline=False)
    await member.send(embed=embed)
    await ctx.send("✅**A List of all the commands has been Sent to your DMs**")

@wolfie.command()
async def modhelp(ctx):
    member = ctx.message.author
    embed = discord.Embed(
        title=f'Mod Commands', colour=discord.Colour.blue(
            )
        )
    embed.add_field(name=f"kick", value=f"Syntax: w!kick (member) (reason) // no '()' needed for this AND ALL OTHER COMMANDS ",inline=False)
    embed.add_field(name=f"ban", value=f"Syntax: w!ban (member) (reason) //",inline=False)
    embed.add_field(name=f"unban", value=f"Syntax: w!unban (member) //",inline=False)
    embed.add_field(name=f"addrole", value=f"Syntax: w!addrole (member) (role) //",inline=False)
    embed.add_field(name=f"removerole", value=f"Syntax: w!removerole (member) (role) //",inline=False)
    embed.add_field(name=f"mute", value=f"Syntax: w!mute (member) //",inline=False)
    embed.add_field(name=f"unmute", value=f"Syntax: w!unmute (member) //",inline=False)
    embed.add_field(name=f"clear", value=f"Syntax: w!clear (amount) // Amount as in Number of Messages cleared",inline=False)
    embed.add_field(name=f"warn", value=f"Syntax: w!warn (member) // warn: Warns a member, when a member gets 3 warns they automaticly get Muted until they are unmuted",inline=False)
    embed.add_field(name=f"cwarns", value=f"Syntax: w!cwarns (member) // cwarns: Clears the Selected Members' Warns",inline=False)
    embed.add_field(name=f"warns", value=f"Syntax: w!warns (member) // warns: Check a Members' Warns (Normal Members should be able to use This Command)",inline=False)
    await member.send(embed=embed)
    await ctx.send("✅**List of all the Mod commands has been Sent to your DMs**")

wolfie.run("Token")
