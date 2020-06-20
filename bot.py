import discord
from discord.ext import commands
import time
from functions import get_url, get_url_v2, get_url_v3, check_stupid, get_forbidden_words_joke, check_pp_size, get_dad_joke

prefix = '$'
token = "NzE3NTYzNDU5ODUxNzgwMjA4.XtcJMQ.j4rmyW2szEfgRTBBj6f5TAlE4KI"
bot = commands.Bot(command_prefix=prefix)


# Commands
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
            for j in range(0, (ctx.message.author.top_role.position - 5)):
                await ctx.send(msg)
        else:
            pass


@bot.command()
async def spam(ctx):
    spammed_users = ctx.message.mentions
    for i in spammed_users:
        msg = i.mention
        for j in range(0, (ctx.message.author.top_role.position - 5)):
            await ctx.send(msg)


@bot.command()
async def tf(ctx):
    messages = await ctx.channel.history(limit=2).flatten()
    msg_author = messages[1].author
    for i in range(0, (ctx.message.author.top_role.position - 5)):
        await ctx.send(f"{msg_author.mention} tf")


@bot.command()
async def nice(ctx):
    messages = await ctx.channel.history(limit=2).flatten()
    msg_author = messages[1].author
    for i in range(0, (ctx.message.author.top_role.position - 5)):
        await ctx.send(f"{msg_author.mention} n i c e")


@bot.command()
async def gay(ctx):
    messages = await ctx.channel.history(limit=2).flatten()
    msg_author = messages[1].author
    for i in range(0, (ctx.message.author.top_role.position - 5)):
        await ctx.send(f"{msg_author.mention} g a y")


@bot.command()
async def bruh(ctx):
    messages = await ctx.channel.history(limit=2).flatten()
    msg_author = messages[1].author
    for i in range(0, (ctx.message.author.top_role.position - 5)):
        await ctx.send(f"{msg_author.mention} b r u h")


@bot.command()
async def spm(ctx, *args):
    string = " ".join(args)
    for j in range(0, (ctx.message.author.top_role.position - 5)):
        await ctx.send(string)


@bot.command()
async def delete(ctx, arg):
    if ctx.message.author.permissions_in(ctx.message.channel).manage_messages:
        await ctx.message.channel.purge(limit=int(arg))
    else:
        await ctx.send("<:harold:718791729398022184>")


@bot.command()
async def pp(ctx, arg=None):
    usr = ctx.message.author

    if arg is not None:
        usr = ctx.message.mentions[0]

    response = check_pp_size()
    pp = response[0]
    joke = response[1]

    if pp == 0:
        await ctx.send(f"{usr.mention} has a vagina LMFAO")
    else:
        await ctx.send(f"{usr.mention} your pp is {pp} cm, {joke}")


@bot.command()
async def joke(ctx):
    joke = get_dad_joke()
    await ctx.send(joke)


@bot.command()
async def mute(ctx):
    muted_user = ctx.message.mentions[0]

    if muted_user == bot.user:
        await ctx.send("<:tucker:720181645919125535>")

    if ctx.message.author.top_role.position > muted_user.top_role.position and ctx.message.author.permissions_in(ctx.message.channel).manage_roles:
        guild_roles = await ctx.guild.fetch_roles()
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted_role in guild_roles:
            pass
        else:
            await ctx.guild.create_role(name="Muted")
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        muted_user_roles = muted_user.roles[1:]
        for role in muted_user_roles:
            await muted_user.remove_roles(role, reason=None, atomic=True)

        await muted_user.add_roles(muted_role, reason=None, atomic=True)
        await ctx.send(f"{muted_user.display_name} has been muted!")
    else:
        await ctx.send("<:harold:718791729398022184>")


@bot.command()
async def unmute(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).manage_roles:
        muted_user = ctx.message.mentions[0]
        if muted_user == bot.user:
            await ctx.send("***nta ba9lawa***")
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted_role in muted_user.roles:
            await muted_user.remove_roles(muted_role, reason=None, atomic=True)
            await ctx.send(f"{muted_user.display_name} has been unmuted!")

            if ctx.guild.id == 659188268029444110:
                plebian_role = discord.utils.get(
                    ctx.guild.roles, name="Plebian")
                await muted_user.add_roles(plebian_role, reason=None, atomic=True)
        else:
            await ctx.send("user needs to be muted first!")
    else:
        await ctx.send("<:harold:718791729398022184>")


@bot.command()
async def chill(ctx, arg):
    if ctx.message.author.permissions_in(ctx.message.channel).manage_channels:
        await ctx.channel.edit(slowmode_delay=int(arg))
    else:
        await ctx.send("<:harold:718791729398022184>")


@bot.command()
async def kick(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).kick_members:
        kicked_users = ctx.message.mentions
        for user in kicked_users:
            if ctx.message.author.top_role.position > user.top_role.position:
                await ctx.send(f"{user.display_name} has been kicked!")
                await user.kick()
            else:
                await ctx.send("<:harold:718791729398022184>")
    else:
        await ctx.send("<:harold:718791729398022184>")


@bot.command()
async def ban(ctx, *args):
    if ctx.message.author.permissions_in(ctx.message.channel).ban_members:
        reason = " ".join(args[1:])
        banned_users = ctx.message.mentions
        for user in banned_users:
            if ctx.message.author.top_role.position > user.top_role.position:
                await ctx.send(f"{user.display_name} has been banned!")
                await user.ban(reason=reason)
            else:
                await ctx.send("<:harold:718791729398022184>")
    else:
        await ctx.send("<:harold:718791729398022184>")


@bot.command()
async def unban(ctx):
    banned_users = await ctx.guild.bans()
    for user in banned_users:
        await ctx.guild.unban(user[1])
        await ctx.send(f"{user[1].display_name} has been unbanned!")

# Events
@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(f"connected to {guild}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the glory of ROME"))


@bot.event
async def on_member_join(member):
    if member.guild.id == 659188268029444110:
        role = discord.utils.get(member.guild.roles, name="Plebian")
        channel = bot.get_channel(659251677865443358)
        await member.add_roles(role, reason=None, atomic=True)
    await channel.send(f"{member.mention} welcome to da clUb reeeeeeeeeee!")


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(659251677865443358)
    await channel.send(f"{member.display_name} has left, what a fag lol")


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
            joke = get_forbidden_words_joke()
            await message.channel.send(f"{joke} {message.author.mention}")

    await bot.process_commands(message)


bot.run(token)
