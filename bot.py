import discord
from discord.ext import commands
import time
from functions import get_url, get_url_v2, check_stupid

token = "NzE3NTYzNDU5ODUxNzgwMjA4.XtcJMQ.j4rmyW2szEfgRTBBj6f5TAlE4KI"
bot = commands.Bot(command_prefix='$')

#Commands
@bot.command()
async def sh(ctx, *args):
    if ctx.message.channel.is_nsfw():
        search_term = " ".join(args)
        title = "here u go faget"
        description = f"requested by {ctx.author.display_name}"
        image_url = get_url(search_term)
        color = 0xff0000
        embed = discord.Embed(
            title=title, description=description, color=color)
        embed.set_image(url=image_url)
        await ctx.send(ctx.message.author.mention)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{ctx.message.author.mention} you need to be in an nsfw channel")


@bot.command()
async def sh2(ctx, *args):
    if ctx.message.channel.is_nsfw():
        search_term = " ".join(args)
        title = "here u go faget"
        description = f"requested by {ctx.author.display_name}"
        image_url = get_url_v2(search_term)
        color = 0xff0000
        embed = discord.Embed(
            title=title, description=description, color=color)
        embed.set_image(url=image_url)
        await ctx.send(ctx.message.author.mention)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{ctx.message.author.mention} you need to be in an nsfw channel")


@bot.command()
async def spem(ctx):
    spammed_roles = ctx.message.role_mentions
    for i in spammed_roles:
        if ctx.message.author.top_role.position >= i.position:
            msg = i.mention
            for j in range(0, 5):
                await ctx.send(msg)
        else:
            pass


@bot.command()
async def spam(ctx):
    spammed_users = ctx.message.mentions
    for i in spammed_users:
        msg = i.mention
        for j in range(0, 5):
            await ctx.send(msg)


@bot.command()
async def tf(ctx):
    messages = await ctx.channel.history(limit=2).flatten()
    msg_author = messages[1].author
    for i in range(0, 5):
        await ctx.send(f"{msg_author.mention} tf")


@bot.command()
async def nice(ctx):
    messages = await ctx.channel.history(limit=2).flatten()
    msg_author = messages[1].author
    for i in range(0, 5):
        await ctx.send(f"{msg_author.mention} n i c e")


@bot.command()
async def gay(ctx):
    messages = await ctx.channel.history(limit=2).flatten()
    msg_author = messages[1].author
    for i in range(0, 5):
        await ctx.send(f"{msg_author.mention} g a y")


@bot.command()
async def spm(ctx, *args):
    string = " ".join(args)
    for j in range(0, 5):
        await ctx.send(string)


#Events
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    check = check_stupid(message.content, ["gay"])
    if check:
        await bot.process_commands(message)


bot.run(token)
