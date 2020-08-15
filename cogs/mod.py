import discord
from discord.ext import commands
import json
import os

async def update_data(self, warnq, member):
    member_id = str(member.id)
    warnq.setdefault(member_id, {"Name": member.name, "Warns": 0})
    warnq[member_id]["Warns"] += 1

class Mod(commands.Cog):
    def __init__(self, wolfie):
        self.wolfie = wolfie

 #@commands.command()
 #async def function(self, ctx):
 #Events with no Decorater
    
    os.chdir(r'C:\Users\ASUS\Desktop\coding\cogs')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.User = None, reason = None):
        if member == None  or member == ctx.message.author:
            await ctx.channel.send("**You Can't Kick yourself.**")
            return
        if reason == None:
            reason = "**No Reason... AT ALL.**"
        message = f"**You have been Kicked from** ***{ctx.guild.name}*** **for** {reason}"
        await member.send(message)
        await ctx.guild.kick(member)
        await ctx.send(embed = discord.Embed(title=f"✅ **{member} was Kicked by {ctx.message.author}**", colour=discord.Colour.discord))

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.User = None, reason = None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("**You Can't Ban yourself.**")
            return
        if reason == None:
            reason = "**No Reason... AT ALL.**"
        message = f"**You have been Suffienctly Thor Hammered (Banned) from** ***{ctx.guild.name}*** **for** {reason}"
        await member.send(message)
        await ctx.guild.ban(member)
        await ctx.send(embed = discord.Embed(title=f"✅ **{member} was Banned by {ctx.message.author}**", colour=discord.Colour.discord))

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user:discord.User):
        await ctx.guild.unban(user)
        await ctx.send(embed = discord.Embed(title=f"✅ **{user} was Unbanned by {ctx.message.author}**", colour=discord.Colour.discord))

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, member:discord.Member, xrole:discord.Role):
        await member.add_roles(xrole)
        embed = discord.Embed(title=f'✅ **Role added**', colour=discord.Colour.blue(
            )
        )
        await ctx.send(embed=embed)
 
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member:discord.Member, xrole:discord.Role):
        await member.remove_roles(xrole)
        embed = discord.Embed(title=f'✅ **Role Removed**', colour=discord.Colour.blue(
            )
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def mute(self, ctx, member:discord.Member = None):
        if member is None:
            await ctx.send(embed = discord.Embed(title=f"**No User Specified**", colour=discord.Colour.blue))
        await member.add_roles(discord.utils.get(member.guild.roles, name="Muted"))
        await ctx.send(embed = discord.Embed(title=f"✅ **User Muted**", colour=discord.Colour.blue))

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def unmute(self, ctx, member:discord.Member = None):
        if member is None:
            await ctx.send("Who?")
        await member.remove_roles(discord.utils.get(member.guild.roles, name="Muted"))
        await ctx.send(embed = discord.Embed(title=f"✅ **User Unmuted**", colour =discord.Colour.blue))

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(title=f"✅ **Messages Deleted**", colour=discord.Colour.blue)
        await ctx.send(embed=embed, delete_after=4)

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def warn(self, ctx, member:discord.Member = None):
        if member is None:
            await ctx.send("**Please Specify a User.**")
            return
        member_id = str(member.id)
        with open('warns.json', 'r') as f:
            warnq = json.load(f)
            await update_data(self, warnq, member)

        with open('warns.json', 'w') as f:
            json.dump(warnq, f)

        embed = discord.Embed(title=f"✅ **User Warned**", colour=discord.Colour.blue)
        await ctx.send(embed=embed)

        with open('warns.json', 'r') as f:
            if warnq[member_id]["Warns"] == 3:
                await member.add_roles(discord.utils.get(member.guild.roles, name="Muted"))
                embed2 = discord.Embed(title=f"✅ **3 Warns Reached, User Muted**", colour=discord.Colour.blue)
                await ctx.send(embed=embed2)

                with open('warns.json', "r") as f:
                    warnq[member_id]["Warns"] = 0
                with open('warns.json', "w") as f:
                    json.dump(warnq, f)

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def cwarns(self, ctx, member:discord.Member):
        member_id = str(member.id)
        with open('warns.json', "r") as f:
            warnq = json.load(f)
            member_id = str(member.id)
            warnq[member_id]["Warns"] = 0

        with open('warns.json', "w") as f:
            json.dump(warnq, f)
            embed = discord.Embed(title=f"✅ **Warns Cleared.**", colour=discord.Colour.blue)
            await ctx.send(embed=embed)

    @commands.command()
    async def warns(self, ctx, member:discord.Member = None):
        if member is None:
            member = ctx.message.author
        member_id = str(member.id)
        with open('warns.json', "r") as f:
            warnq = json.load(f)
            w = warnq[str(member_id)]["Warns"]
            phd = warnq[str(member_id)]
            embed = discord.Embed(title=f"**Warn Count: {w}**", colour=discord.Colour.blue)
            await ctx.send(embed=embed)


def setup(wolfie):
	wolfie.add_cog(Mod(wolfie))
