import discord
import sqlite3
from discord.ext import commands
import asyncio
import logging
import random 
import time 
import datetime
from datetime import datetime
import json
import os

now = datetime.now()

logging.basicConfig(level='INFO')

bot = commands.Bot(command_prefix="w!", description="Me is bot and me is dumb...")
bot.remove_command("help")

@bot.listen()
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"ID : {bot.user.id}")
    print(f"Discrim: {bot.user.discriminator}")
    print(f"Is Bot On? {bot.user.bot}")
    print(f"Preparing Game...")
    game = discord.Game(f" Being Tortured by my Dev :( | User Count: {len(bot.guilds)}")
    await bot.change_presence(status=discord.Status.online,activity=game)
    print(f"Playing {game}")

@bot.listen()
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
            
@bot.listen()
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
                channel = discord.utils.get(member.guild.channels, name="testingtesting-123") 
                await channel.send(embed=embed)
        else:
            embed = discord.Embed(title=f"BOT {member.name}#{member.discriminator}",color=0xff0000)
            embed.add_field(name=f"Join Date", value=f" {member.joined_at.strftime('%B %d, %Y')}",inline=True)
            embed.add_field(name=f"Leave Date", value=f" {now.strftime('%B %d, %Y')}",inline=True)
            embed.set_author(name="Member left",icon_url=member.avatar_url)
            try:
                channel = discord.utils.get(member.guild.channels, name="logs")
                await channel.send(embed=embed)
            except:
                channel = discord.utils.get(member.guild.channels, name="testingtesting-123") 
                await channel.send(embed=embed)



@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send(f"Ping Value is {ping}ms")

@bot.command()
async def github(ctx):
    await ctx.send("https://github.com/WhiteWolf206/Wolfie-DB")
    await ctx.send("And Click on this -> https://www.youtube.com/channel/UC9j8u0TLh3SnPfnskC8tCJg and Subcribe to my Devs Channel")

@bot.command()
async def user(ctx, member:discord.Member = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
        pronounn = "You"
    else:
        pronoun = "Their"
        pronounn = "They"
    name = f"{member.name}#{member.discriminator}"
    status = member.status
    joined = member.joined_at
    role = member.top_role
    await ctx.channel.send(f"***{pronoun} name is {name}***\n***{pronoun} Status is {status}***\n**{pronounn} Joined at {member.joined_at.strftime('%B %d, %Y')}**\n**{pronoun} Highest role is {role}**")

@bot.command()
@commands.has_any_role("Moderators, Administrators")
async def kick(ctx, member:discord.User = None, reason = None):
    if member == None  or member == ctx.message.author:
        await ctx.channel.send("You Can't Kick yourself!!")
        return
    if reason == None:
        reason = "No Reason was Specified"
    message = f"You have been Kicked from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.kick(member)
    await ctx.channel.send(f"{member} has Been KICKED! ~~in the arse~~")

@bot.command()
@commands.has_any_role("Moderators, Administrators")
async def ban(ctx, member:discord.User = None, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You Can't Ban yourself!!")
        return
    if reason == None:
        reason = "No Reason... AT ALL"
    message = f"You have been Thor Hammered (Banned) from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(member)
    await ctx.channel.send(f"{member} has been BANNED!")

@bot.command(pass_context = True)
@commands.has_any_role("Moderators, Administrators")
async def mute(ctx, member: discord.Member):
    try:
        role = discord.utils.get(member.server.roles, name="Muted")
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was Muted!".format(member, color=0xff00f6))
        await bot.say(embed=embed)
    except:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)

bot.run('')

