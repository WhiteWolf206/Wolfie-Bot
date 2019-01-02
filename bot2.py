import discord
import sqlite3
from discord.ext import commands
import asyncio
import logging
import random 
import time 
import datetime
from datetime import datetime
import os

now = datetime.now()

logging.basicConfig(level='INFO')

bot = commands.Bot(command_prefix='w!', description='')
bot.remove_command("help")

@bot.event
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
async def hello(ctx):
    await ctx.send('Sup')

@bot.command()
async def youtube(ctx):
    await ctx.send('https://www.youtube.com/channel/UC9j8u0TLh3SnPfnskC8tCJg')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def github(ctx):
    await ctx.send('https://github.com/WhiteWolf206/Wolfie-DB')


bot.run('')
