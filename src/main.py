
from multiprocessing.managers import Token
import discord
import os

from discord import DMChannel
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands
from commands import printWithTime

from response import helpResponse, answerResponse, feedbackResponse, suggestResponse, donateResponse, pingResponse
from variables import prefix
from colors import infoStatus, errorStatus


bot = commands.Bot(command_prefix=prefix, help_command=None)

load_dotenv(find_dotenv())

# discord events
@bot.event
async def on_ready():
    printWithTime(infoStatus + "Bot running!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help"))


# discord commands
@bot.command()
async def shutdown(ctx):
    await bot.close()

@bot.command()
async def help(ctx, *, args="help"):
    await ctx.channel.send(embed=helpResponse(ctx, args))

@bot.command()
async def answer(ctx, args):
    await ctx.channel.send(embed=answerResponse(ctx, args))

@bot.command(pass_context=True)
async def feedback(ctx, *, feedback):

    dmEmbed, embed = feedbackResponse(ctx, feedback)
    aldin = await bot.fetch_user("625668378287276082")

    await DMChannel.send(aldin, embed=dmEmbed)
    await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)
async def suggest(ctx, *, suggestion):

    dmEmbed, embed = suggestResponse(ctx, suggestion)
    aldin = await bot.fetch_user("625668378287276082")

    await DMChannel.send(aldin, embed=dmEmbed)
    await ctx.channel.send(embed=embed)

@bot.command()
async def donate(ctx):
    await ctx.channel.send(embed=donateResponse(ctx))

@bot.command()
async def ping(ctx):
    await ctx.channel.send(embed=pingResponse(ctx, str(round(bot.latency * 1000))))

token = os.getenv("TOKEN")
#print(token)
#str(token)
bot.run(token)