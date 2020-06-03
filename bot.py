import discord
import time
from functions import get_url

token = "NzE3NTYzNDU5ODUxNzgwMjA4.XtcJMQ.j4rmyW2szEfgRTBBj6f5TAlE4KI"
prefix = "$"
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f"{prefix}sho"):
        channel = message.channel
        title = "here u go faget"
        description = f"requested by {message.author.display_name}"
        image_url = get_url("tits")
        color = 0xff0000
        embed = discord.Embed(
            title=title, description=description, color=color)
        embed.set_image(url=image_url)
        await channel.send(embed=embed)

    if message.content.startswith(f"{prefix}spam"):
        channel = message.channel
        spammed_users = message.mentions
        for i in spammed_users:
            msg = i.mention
            for j in range(0, 10):
                await channel.send(msg)

    if message.content.startswith(f"{prefix}spam role"):
        channel = message.channel
        spammed_roles = message.role_mentions
        for i in spammed_roles:
            if message.author.top_role.position >= i.position:
                msg = i.mention
                for j in range(0, 10):
                    await channel.send(msg)
            else:
                pass

client.run(token)
