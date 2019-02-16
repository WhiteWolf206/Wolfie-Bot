import discord
from discord.ext import commands
import datetime
from datetime import datetime
import asyncio
import logging
import random
import time
import sqlite3

bot = commands.Bot(command_prefix="w!")
logging.basicConfig(level='INFO')
bot.remove_command("help")

@bot.listen()
async def on_ready():
    print(f"Bot ready!")
    game = discord.Game(f" Starting out Strong! | User Count: {len(bot.guilds)}")
    await bot.change_presence(status=discord.Status.online,activity=game)
    print(f"Playing {game}")

@bot.listen()
async def on_error():
    error = error
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Permission Denied")

@bot.listen()
async def on_member_join(member):
    if member.bot == False:
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

@bot.listen()
async def on_member_remove(member):
    now = datetime.now()
    if member.bot == False:
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

class User:

 @bot.command()
 async def ping(ctx):
     ping_ = bot.latency
     ping = round(ping_ * 1000)
     await ctx.channel.send(f"Ping Value is {ping}ms")

 @bot.command()
 async def github(ctx):
     embed = discord.Embed(title="Github Link",description="(https://github.com/WhiteWolf206/Wolfie-DB)",color=0x00FF00)
     await ctx.send(embed=embed)

 @bot.command()
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

 @bot.command()
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

 @bot.command()
 async def owner(ctx):
     await ctx.send(f"{ctx.guild.owner.mention} ***Is the Owner of this Guild/Server***"
        )

 @bot.command()
 async def xhelp(ctx):
     embed = discord.Embed(
        title=f'Help', colour=discord.Colour.blue(
            )
        )
     embed.add_field(name=f"Ping", value=f"Returns the bots latency",inline=False)
     embed.add_field(name=f"Github", value=f"Returns the bots Github Page",inline=False)
     embed.add_field(name=f"User", value=f"Returns Information about specified User",inline=False)
     embed.add_field(name=f"Serverinfo", value=f"Returns Information about the Server the Message is sent in",inline=False)
     embed.add_field(name=f"Owner", value=f"Mentions the Owner",inline=False)
     embed.add_field(name=f"Mod Commands:", value=f"Kick, Ban, Unban, Promote, Demote, Pmute, Unmute, Purge, Warn",inline=False)
     await ctx.send(embed=embed)

class Moderator:

 @bot.command()
 @commands.has_permissions(kick_members=True)
 async def kick(ctx, member:discord.User = None, reason = None):
     if member == None  or member == ctx.message.author:
         await ctx.channel.send("You Can't Kick yourself!!")
         return
     if reason == None:
         reason = "No Reason... AT ALL."
     message = f"You have been Kicked from {ctx.guild.name} for {reason}"
     await member.send(message)
     await ctx.guild.kick(member)
     await ctx.channel.send(f"{member} has Been KICKED! ~~in the arse~~")

 @bot.command()
 @commands.has_permissions(ban_members=True)
 async def ban(ctx, member:discord.User = None, reason = None):
     if member == None or member == ctx.message.author:
         await ctx.channel.send("You Can't Ban yourself!!")
         return
     if reason == None:
         reason = "No Reason... AT ALL."
     message = f"You have been Thor Hammered (Banned) from {ctx.guild.name} for {reason}"
     await member.send(message)
     await ctx.guild.ban(member)
     await ctx.channel.send(f"{member} has been BANNED!")

 @bot.command()
 @commands.has_permissions(ban_members=True)
 async def unban(ctx, user:discord.User):
     await ctx.guild.unban(user)
     await ctx.send(embed = discord.Embed(title="User Unbanned",description="{0.name} was Unbanned by {1.name}.".format(user, ctx.message.author)))

 @bot.command()
 @commands.has_permissions(manage_roles=True)
 async def promote(ctx, member:discord.Member, xrole:discord.Role):
     await member.add_roles(xrole)
     await ctx.send("Role Added!")

 @bot.command()
 @commands.has_permissions(manage_roles=True)
 async def demote(ctx, member:discord.Member, xrole:discord.Role):
     await member.remove_roles(xrole)
     await ctx.send("Role Removed!")

 @bot.command()
 @commands.has_permissions(view_audit_log=True)
 async def pmute(ctx, member:discord.Member, reason = None):
     if member is None or member == ctx.message.author:
         await ctx.send("You Can't Mute yourself!!")
         return
     if reason is None:
         reason = "No Reason... AT ALL"
         await member.add_roles(discord.utils.get(member.guild.roles, name="Muted"))
         embed = discord.Embed(title=f'Mute Completed.', description=f"{member} has been Muted by {ctx.message.author} for {reason}" colour=discord.Colour.blue())
         await ctx.send(embed=embed)


 @bot.command()
 @commands.has_permissions(view_audit_log=True)
 async def unmute(ctx, member:discord.Member):
    await member.remove_roles(discord.utils.get(member.guild.roles, name="Muted"))

 @bot.command()
 @commands.has_permissions(manage_messages=True)
 async def purge(ctx, amount: int):
     await ctx.channel.purge(limit=amount + 1)

 @bot.command()
 @commands.has_permissions(view_audit_log=True)
 async def warn(ctx, member:discord.Member):
    pass

bot.run("TOKEN")
