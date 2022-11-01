# /usr/bin/python3
import pyshorteners
import os
import discord
from http.client import HTTPSConnection
from sys import stderr
from json import dumps
from time import sleep
import random
import re
import json
from threading import Thread
from discord.ext import commands
import numpy
from urllib.request import urlopen as urle
import asyncio
from discord.utils import get
import requests
import sys
import subprocess
from dotenv import load_dotenv

global stof
global timessss

prefixes = ["db.", "Db."]
myserver = [759064818001903706]
sq = pyshorteners.Shortener()

load_dotenv()


def mainle(textoas, chsa, timesss):
    message_data = {"content": textoas}
    t = timesss + 1
    for i in range(t):
        send_message(get_connection(), chsa, dumps(message_data))


stof = 0

# color code https://gist.github.com/thomasbnt/b6f455e2c7d743b796917fa3c205f812.js

whitelist = [702181685847916640, 138390027209146368]

header_data = {
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0",
    "authorization": os.environ["tokend"],
    "host": "discordapp.com",
    "referer": "https://discord.com/channels/759064818001903706/789497820159410187",
}


def get_connection():
    return HTTPSConnection("discordapp.com", 443)


def send_message(conn, channel_id, message_data):
    try:
        conn.request(
            "POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data
        )
        resp = conn.getresponse()
        if 199 < resp.status < 300:
            pass
        else:
            stderr.write(f"Received HTTP {resp.status}: {resp.reason}\n")
            pass
    except:
        stderr.write("Failed to send_message\n")


bot = commands.Bot(command_prefix=prefixes, case_insensitive=True)
# slash = SlashCommand(bot, sync_commands=True)
global servers
servers = []

# -----------------------------------------------------------------------------------


@bot.event
async def on_ready():
    global servers
    channel = bot.get_channel(789497820159410187)
    await channel.send(f"bots up")
    print(f"bots up")
    for server in bot.guilds:
        servers.append(server.id)
    bot.loop.create_task(status_task())


async def status_task():
    while True:
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, name="db.help"
            )
        )
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="@dark bot"))
        await asyncio.sleep(1)
        await bot.change_presence(
            activity=discord.Streaming(
                name="P*r*", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            )
        )
        await asyncio.sleep(1)


# ----------------------------------------


@bot.command(hidden=True)
@commands.is_owner()
async def spotify(ctx):
    urle("https://spotify.thinker010.repl.co/")


@bot.command()
async def say(ctx, *, content):
    if content.endswith("-hide"):
        await ctx.message.delete()
        content = content.replace("-hide", "")
    await ctx.send(content)


@bot.command(help="sends dm mesage to anyone in server n u also expect me ofc")
async def dm(ctx, member: discord.User, *, content):
    await ctx.message.delete()
    if member == bot.user:
        await ctx.send("u mad?:face_with_raised_eyebrow:", delete_after=5.0)
        # await ctx.message.add_reaction("\U0001F914")
    else:
        await member.send(content)


@bot.command(hidden=True)
@commands.is_owner()
async def ssend(ctx, timess: int, *, texto):
    await ctx.message.delete()
    textoa = str(texto)
    cha = str(ctx.channel.id)
    mainle(textoa, cha, timess)
    sleep(1)


@bot.command(help="invite the bot")
async def invite(ctx):
    await ctx.send(
        "https://discord.com/api/oauth2/authorize?client_id=787378379719835738&permissions=8&scope=bot%20applications.commands"
    )


@bot.command(help="just a cool command")
@commands.cooldown(1, 50, commands.BucketType.user)
async def spam(ctx, times: int, *, content="spam"):
    global stof
    global timessss
    timessss = times
    urle("https://tinyurl.com/yddwjkvk/spam")
    if not "@everyone" in content:
        if times < 100 and stof == 0:
            for i in range(times):
                if stof == 0:
                    await ctx.send(content)
            stof = 0
        elif stof == 0:
            await ctx.send(f"nope....not more than 100")
            stof = 0
            spam.reset_cooldown(ctx)
    else:
        await ctx.send(f"pls dont mention everyone:rage:")
        await ctx.message.delete()
        spam.reset_cooldown(ctx)
    stof = 0


@spam.after_invoke
async def reset_cooldown(ctx):
    global timessss
    timesssss = timessss
    chael = bot.get_channel(789497820159410187)
    await chael.send(
        "user: "
        + ctx.message.author.name
        + "  no.: "
        + str(timesssss)
        + "  ch: "
        + ctx.channel.name
    )
    for e in whitelist:
        if e == ctx.author.id:
            spam.reset_cooldown(ctx)


@bot.command(hidden="true")
@commands.is_owner()
async def spem(ctx, times: int, *, content="spam"):
    global stof
    await ctx.message.delete()
    print("spem:", times)
    for i in range(times):
        if stof == 0:
            await ctx.send(content)
    stof = 0


@bot.command(aliases=["rolldice", "rld"], help="roll's dice")
async def rad(ctx):
    await ctx.send(f"dice fell on: {random.randint(1,6)}")


@bot.command(help="toss a coin")
async def tc(ctx):
    coinside = ["Heads", "Tails", "MIDDLE"]
    weight = [0.495, 0.495, 0.01]
    choice = numpy.random.choice(coinside, p=weight)
    msg = await ctx.send(f"coin fell on: {choice}")
    if choice == "MIDDLE":
        em = discord.Embed(
            title=f"Pog", description=f"Pass: J^W9z=s7V3t@hGp", color=3447003
        )
        await ctx.send(embed=em)
        await msg.add_reaction("\U0001F973")
        await msg.add_reaction("\U0001F60E")
        await msg.add_reaction("\U0001F929")


@bot.command(help="check bot ping")
async def ping(ctx):
    await ctx.message.add_reaction("\U0001F44D")
    await ctx.send(f"Pong: {round(bot.latency*1000)}ms")


@bot.command(hidden="true")
@commands.is_owner()
async def shutdown(ctx):
    await ctx.message.delete()
    await bot.logout()


@bot.command(hidden="true")
@commands.is_owner()
async def rest(ctx):
    await ctx.message.delete()
    os.execv(sys.executable, ["python3"] + sys.argv)


@bot.command(hidden="true")
async def stop(ctx):
    await ctx.message.delete()
    global stof
    stof = 1


@bot.command(help="shorten urls")
async def url(ctx, urld):
    await ctx.send(sq.tinyurl.short(urld))


@bot.command(hidden=True)
@commands.is_owner()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)
    await ctx.send("Done!", delete_after=5.0)


@bot.event
async def on_message(message):
    mention = f"@787378379719835738"
    if message.author == bot.user:
        return
    if re.fullmatch("<@(!)?787378379719835738>", message.content):
        await message.channel.send("My prefix is `{0}`".format(bot.command_prefix))
    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("send a proper value")
        spam.reset_cooldown(ctx)


@spam.error
async def spam_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(
            title=f"Slow it down",
            description=f"Try again in {error.retry_after:.2f}s.",
        )
        await ctx.send(embed=em)


# ----------------------------------------------------------------

optionsforspams = [
    {
        "name": "amount",
        "description": "amount of times",
        "required": True,
        "type": 4,
    },
    {
        "name": "sentence",
        "description": "sentence",
        "required": False,
        "type": 3,
    },
]


# @slash.slash(name="spam", guild_ids=servers, options=optionsforspams)
# async def spams(ctx: SlashContext, amount, sentence="spam"):
#     if amount <= 100:
#         for i in range(amount):
#             await ctx.channel.send(sentence)
#         await ctx.send(f"done", delete_after=1.0)
#     else:
#         await ctx.send(f"nope....not more than 100")


# optionsforgh = [
#     {
#         "name": "person",
#         "description": "person to be gh",
#         "required": True,
#         "type": 6,
#     },
#     {
#         "name": "times",
#         "description": "times",
#         "required": True,
#         "type": 4,
#     },
# ]


# @slash.slash(name="gh", guild_ids=servers, options=optionsforgh, description="just gh")
# async def ghs(ctx: SlashContext, person, times):
#     global stof
#     if times < 100 and stof == 0:
#         for i in range(times):
#             if stof == 0:
#                 msg = await ctx.send(person.mention)
#                 await msg.delete()
#         stof = 0
#     elif stof == 0:
#         await ctx.send("nope....not more than 100")
#         stof = 0
#     stof = 0


# --------------------------------------------------------------------------------------------------------------------------------

bot.run(os.environ["dark_bot"])
