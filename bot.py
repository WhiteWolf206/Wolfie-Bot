import discord
from discord.ext import commands
import asyncio
import logging
import random 
import time 
import datetime
from datetime import datetime
import sqilte3

wolf = commands.Bot(command_prefix = "w!")
TOKEN = "Nope"
now = datetime.now()

logging.basicConfig(level="INFO")

@wolf.listen()
async def on_ready():
    print("Wolfie is ready.")
    game = discord.Game(f" Starting out Strong! | User Count: {len(bot.guilds)}")
    await wolf.change_presence(status=discord.Status.online,activity=game)
    print(f"Playing {game}")

@wolf.listen()
async def on_member_join(member):
    if member.bot == False:
        embed = discord.Embed(title=f"{member.name}#{member.discriminator}",color=0x009933)
        embed.add_field(name=f"Creation Date",value=f" {member.created_at.strftime('%B %d, %Y')}",inline=True)
        embed.add_field(name=f"Join Date", value=f" {member.joined_at.strftime('%B %d, %Y')}",inline=True)
        embed.add_field(name=f"Member Count", value=f" {member.guild.member_count}")
        embed.set_author(name="Member Joined",icon_url=member.avatar_url)
        try:
            channel = discord.utils.get(member.guild.channels, name="logs")
            await channel.send(embed=embed)
            role = discord.utils.get(member.guild.roles, name="Test Subject")
            await member.add_roles(role)
        except:
            channel = discord.utils.get(member.guild.channels, name="testingtesting-123")
            await channel.send(embed=embed)
            role = discord.utils.get(member.guild.roles, name="Test Subject")
            await member.add_roles(role)
    else:
        embed = discord.Embed(title=f"BOT {member.name}#{member.discriminator}",color=0x009933)
        embed.add_field(name=f"Creation Date",value=f" {member.created_at.strftime('%B %d, %Y')}",inline=True)
        embed.add_field(name=f"Join Date", value=f" {member.joined_at.strftime('%B %d, %Y')}",inline=True)
        embed.set_author(name="Member Joined",icon_url=member.avatar_url)
        try:
            channel = discord.utils.get(member.guild.channels, name="logs")
            await channel.send(embed=embed)
        except:
            channel = discord.utils.get(member.guild.channels, name="testingtesting-123")
            await channel.send(embed=embed)

@wolf.listen()
async def on_member_remove(member):
        if member.bot == False:
            embed = discord.Embed(title=f"{member.name}#{member.discriminator}",color=0xff0000)
            embed.add_field(name=f"Join Date", value=f" {member.joined_at.strftime('%B %d, %Y')}",inline=True)
            embed.add_field(name=f"Leave Date", value=f" {now.strftime('%B %d, %Y')}",inline=True)
            embed.add_field(name=f"Member Count", value=f" {member.guild.member_count}")
            embed.set_author(name="Member Left",icon_url=member.avatar_url)
            try:
                channel = discord.utils.get(member.guild.channels, name="logs")
                await channel.send(embed=embed)
            except:

class User:

 @wolf.command()
 async def ping(ctx):
     ping_ = wolf.latency
     ping = round(ping_ * 1000)
     await ctx.channel.send(f"Ping Value is {ping}ms")

 @wolf.command()
 async def github(ctx):
     embed = discord.Embed(title=f"Github", colour=discord.Colour.blue())
     embed.add_field(name="Link:", value=f"https://github.com/WhiteWolf206/Wolfie-DB")
     await ctx.send(embed=embed)

 @wolf.command()
 async def owner(ctx):
 	guild = ctx.guild
     await ctx.send(f"{ctx.guild.owner.mention} is the Owner of {guild}")
     await ctx.send(f"and my Developer/Owner is PaladinWolfenstein#4860")

 @wolf.command(pass_context=True)
 async def serverinfo(ctx):
     guild = ctx.guild
     embed = discord.Embed(title=f'{guild.name}', colour=discord.Colour.blue())
     embed.set_thumbnail(url=f'{guild.icon_url}')
     embed.add_field(name="Server Created in :", value=f'''  {guild.created_at.strftime('%B %d, %Y at %I:%M %p')}''', inline=False)
     embed.add_field(name="Created by :", value=f'''{guild.owner.mention}''',inline=False)
     embed.add_field(name='Region :', value=f'''  {guild.region}''',inline=False)
     embed.add_field(name='Server ID :', value=f'''{guild.id}''',inline=False)
     embed.add_field(name='Server Members :', value=f'''  {len(guild.members)}''', inline=False)
     embed.add_field(name='Online Members :',value=f'''{len([I for I in guild.members if I.status is discord.Status.online])}''',inline=False)
     await ctx.send(embed=embed)

 @wolf.command()
 async def user(ctx, member:discord.Member = None):
     if member == ctx.message.author or None:
     	membera = ctx.message.author
     	namea = f"{membera.name}#{membera.discriminator}"
        statusa = membera.status
        joineda = membera.joined_at
        rolea = membera.top_role
 	    embeda = discord.Embed(title=f'{membera.name}', colour=discord.Colour.purple())
        embeda.set_thumbnail(url=f'{membera.avatar_url}')
        embeda.add_field(name=" Name", value=f"{namea}", inline=True)
        embeda.add_field(name=" Status", value=f"{statusa}", inline=True)
        embeda.add_field(name=" Join at", value=f"{joineda: %B %d, %Y}", inline=False)
        embeda.add_field(name=" Highest Role", value=f"{rolea}", inline=True)
     else:
     	name = f"{member.name}#{member.discriminator}"
        status = member.status
        joined = member.joined_at
        role = member.top_role     	
 	    embed = discord.Embed(title=f'{member.name}', colour=discord.Colour.purple())
        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.add_field(name=" Name", value=f"{name}", inline=True)
        embed.add_field(name=" Status", value=f"{status}", inline=True)
        embed.add_field(name=" Join at", value=f"{joined: %B %d, %Y}", inline=False)
        embed.add_field(name=" Highest Role", value=f"{role}", inline=True)

class Moderator:

 @wolf.command()
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

 @kick.error
 async def kick_error(ctx, error):
     if isinstance(error, commands.MissingPermissions):
         await ctx.send("Permission Denied")

 @wolf.command()
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

 @ban.error
 async def ban_error(ctx, error):
     if isinstance(error, commands.MissingPermissions):
         await ctx.send("Permission Denied")

 @wolf.command()
 @commands.has_permissions(ban_members=True)
 async def unban(ctx, user:discord.User):
     await ctx.guild.unban(user)
     await ctx.send(embed = discord.Embed(title="User Unbanned",description="{0.name} was Unbanned by {1.name}.".format(user, ctx.message.author)))

 @unban.error
 async def unban_error(ctx, error):
     if isinstance(error, commands.MissingPermissions):
         await ctx.send("Permission Denied")

 @wolf.command()
 @commands.has_permissions(manage_roles=True)
 async def roleplus(ctx, member:discord.Member, xrole:discord.Role):
     await member.add_roles(xrole)
     await ctx.send("Role Added!")

 @roleplus.error
 async def roleplus_error(ctx, error):
     if isinstance(error, commands.MissingPermissions):
         await ctx.send("Permission Denied")

 @wolf.command()
 @commands.has_permissions(manage_roles=True)
 async def roleminus(ctx, member:discord.Member, xrole:discord.Role):
     await member.remove_roles(xrole)
     await ctx.send("Role Removed!")

 @roleminus.error
 async def roleminus_error(ctx, error):
     if isinstance(error, commands.MissingPermissions):
         await ctx.send("Permission Denied")

 @wolf.command()
 @commands.has_permissions(view_audit_log=True)
 async def pmute(ctx, member:discord.Member, reason = None):
     if member is None or member == ctx.message.author:
         await ctx.send("You Can't Mute yourself!!")
         return
     if reason == None:
         result = "No reason... AT ALL"
     await member.add_roles(discord.utils.get(member.guild.roles, name="Muted"))
     await ctx.send(f"{member} has been Muted by {ctx.message.author} for {reason}")

 @pmute.error
 async def pmute_error(ctx, error):
     if isinstance(error, commands.MissingPermissions):
         await ctx.send("Permission Denied")

 @wolf.command()
 @commands.has_permissions(view_audit_log=True)
 async def unmute(ctx, member:discord.Member):
    await member.remove_roles(discord.utils.get(member.guild.roles, name="Muted"))

 @unmute.error
 async def unmute_error(ctx, error):
     if isinstance(error, commands.MissingPermissions):
         await ctx.send("Permission Denied")

 @wolf.command(pass_context=True)
 @commands.has_permissions(manage_messages=True)
 async def purgef(ctx, limit: int):
 	 await ctx.channel.purge(limit=limit)
 	 await ctx.message.delete()
     await ctx.send("Messages Deleted!")

 @clear.error
 async def clear_error(ctx, error):
	 if isinstance(error, commands.MissingPermissions):
		 await ctx.send("Permission Denied")

class Voice:

 @wolf.command()
 async def vcjoin():
 	pass

 @wolf.command()
 async def vcleave():
 	pass

wolf.run(TOKEN)
