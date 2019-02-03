import discord
from discord.ext import commands
import asyncio
import youtube_dl

'''Before you continue reading... this is not a cog this is just 
to help people see the functions and modules conducting my voice class for the bot'''

players = {}
queues = {}

def check_queue(id):
    if queues[id] is not []:
        player = queues[id].pop[0]
        players[id] = player
        player.start()

class Voice:

 @wolf.command()
 async def vcjoin(ctx):
     channel = ctx.author.voice.channel
     user = ctx.message.author
     client = ctx.voice_client

     if user is None: #Checks if the user is occupied in a voice channel
         await ctx.send("You must be in Voice Channel first!")
     elif client is not None: #checks if the bot\client is already in a voice channel
         await client.move_to(channel) #moves the client to the authors voice channel
     else:
         try:
             await channel.connect()
         except asyncio.TimeoutError as e:
             print(e)

 @wolf.command()
 async def vcleave(ctx):
     await ctx.voice_client.disconnect()

 @wolf.command()
 async def play(ctx, url):
     player = await ctx.voice_client.create_ytdl_player(url, after=lambda: check_queue(guild.id))
     players[guild.id] = player
     player.start()

 @wolf.command()
 async def queue(ctx, url):
     player = await ctx.voice_client.create_ytdl_player(url, after=lambda: check_queue(guild.id))
     if guild.id in queues:
         queues[guild.id].append(player)
     else:
         queues[guild.id] = [player]
     await ctx.send("Queue updated. {url} has been Added.")


 @wolf.command()
 async def pause(ctx):
     id = ctx.message.author.id
     players[id].pause()

 @wolf.command()
 async def resume(ctx):
     id = ctx.message.author.id
     players[id].resume()

 @wolf.command()
 async def stop(ctx):
     id = ctx.message.author.id
     players[id].stop()

wolf.run("Nope!")
