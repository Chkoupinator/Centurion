import discord
from discord.ext import commands
import time
from functions import get_url, get_url_v2, get_url_v3, check_stupid, get_joke, check_pp_size

prefix = '$'
token = "NzE3NTYzNDU5ODUxNzgwMjA4.XtcJMQ.j4rmyW2szEfgRTBBj6f5TAlE4KI"
bot = commands.Bot(command_prefix=prefix)

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
        await ctx.send(f"{ctx.message.author.mention} no")


@bot.command()
async def shr(ctx, *args):
    if ctx.message.channel.is_nsfw():
        search_term = " ".join(args)
        title = "here u go faget"
        description = f"requested by {ctx.author.display_name}"
        image_url = get_url_v3(search_term)
        color = 0xff0000
        embed = discord.Embed(
            title=title, description=description, color=color)
        embed.set_image(url=image_url)
        await ctx.send(ctx.message.author.mention)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{ctx.message.author.mention} no")


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
        await ctx.send(f"{ctx.message.author.mention} no")


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


@bot.command()
async def delete(ctx, arg):
    messages = await ctx.channel.history(limit=int(arg)).flatten()
    if ctx.message.author.permissions_in(ctx.message.channel).manage_messages:
        for i in messages:
            await i.delete()
    else:
        await ctx.send("nO")


@bot.command()
async def pp(ctx, arg=None):
    usr = ctx.message.author
    
    if arg is not None:
        usr = ctx.message.mentions[0]

    response = check_pp_size()
    pp = response[0]
    joke = response[1]

    await ctx.send(f"{usr.mention} your pp is {pp} cm, {joke}")

    



#Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the glory of ROME"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if not message.content.startswith(prefix):
        forbidden_words_channel = bot.get_channel(717897450337075260)
        arr = await forbidden_words_channel.history(limit=100).flatten()
        forbidden_words_list = []
        for i in arr:
            forbidden_words_list.append(i.content)
        check = check_stupid(message.content.lower(), forbidden_words_list)
        if check:
            joke = get_joke()
            await message.channel.send(f"{joke} {message.author.mention}")

    await bot.process_commands(message)


bot.run(token)
