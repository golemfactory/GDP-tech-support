
import discord
import datetime
import json

from discord import DMChannel

from logic import DetectKeywords
from commands import status
from colors import infoStatus, errorStatus, coloredHelp, coloredHelpFeedback, coloredHelpSuggest, coloredAnswer, coloredFeedback, coloredSuggest, coloredDonate, coloredPing

from variables import prefix, embedColor, icon, allowedChannels, wallet_akash, wallet_ERC20


with open("../faq.json") as f:
    faq = json.load(f)


def helpResponse(ctx, args):

    if ctx.message.channel.id in allowedChannels:

        if args == "help":

            status(ctx, infoStatus, coloredHelp)
            embed = discord.Embed(title="Guide to use Tech Support" , color=embedColor)

            embed.add_field(name="About" ,value="Discord Bot developed to help community members with questions and errors, to get started try one of the commands!", inline=False)
            embed.add_field(name="How To Use", value=f"Commands start with `{prefix}`, experiment with any of the commands below, and if your stuck on a certain command type `!help [command]` for more info :)\n\n\n\n", inline=False)
            embed.add_field(name="Commands", value="Here's a list of all commands:", inline=False)

            embed.add_field(name="Answer", value=f"`{prefix}answer [question]`", inline=True)
            embed.add_field(name="Feedback", value=f"`{prefix}feedback \"[feedback]\"`", inline=True)
            embed.add_field(name="Suggest", value=f"`{prefix}suggest \"[suggestion]\"`", inline=True)

            embed.add_field(name="Ping", value=f"`{prefix}ping`", inline=True)
            embed.add_field(name="empty", value=f"`{prefix}empty`", inline=True)
            embed.add_field(name="Donate", value=f"`{prefix}donate`", inline=True)

            embed.add_field(name="\u200b", value="Feel free to ping @aldin#2390 for any questions or talk about the bot :D\n\n -[ github](https://github.com/adnssc/TaskForceGeneral)", inline=False)

            embed.set_footer(text="Tech Support", icon_url="https://cdn.discordapp.com/avatars/917390822939447307/762c5053cda62e609ee954b7868b42d5.png?size=4096")
            embed.timestamp = datetime.datetime.utcnow()

            return embed

        elif args == "feedback":

            status(ctx, infoStatus, coloredHelp)
            embed = discord.Embed(title="Feedback Command", color=embedColor)

            embed.add_field(name="Description", value="Allows for feedback on the bot, positive/negative, and what could be changed about the bot, but don't get it confused with `!suggest` command.", inline=False)
            embed.add_field(name="Usage", value="`!feedback \"[feedback]\"` - [feedback] argument being what positive/negative thoughts you have about the bot.")
            embed.add_field(name="Example", value="`!feedback \"I really like how this bot helps the community, but I would like to see more questions/answers :(\"`", inline=False)

            embed.set_footer(text="Tech Support", icon_url="https://cdn.discordapp.com/avatars/917390822939447307/762c5053cda62e609ee954b7868b42d5.png?size=4096")
            embed.timestamp = datetime.datetime.utcnow()

            return embed

        elif args == "suggest":

            status(ctx, infoStatus, coloredHelp)
            embed = discord.Embed(title="Suggest Command", color=embedColor)

            embed.add_field(name="Description", value="Allows for suggestions of questions/answers, if you think there is a question that we didn't cover, and answer is needed, write up the question with optional answer with it and it will be added soon :)", inline=False)
            embed.add_field(name="Usage", value="`!suggest \"[question]\" \"[answer]\"` - [question] argument of course being the question you think we are missing, and [answer] argument (optional) which is your beautifully written answer to the specified question which will help the community in incoming years :)")
            embed.add_field(name="Example", value="`!suggest \"What is golem?\" \"Golem is a global, open-source, decentralized supercomputer that anyone can use. It is made up of the combined computing power of the users' machines, from PCs to entire data centers.\"`", inline=False)

            embed.set_footer(text="Tech Support", icon_url="https://cdn.discordapp.com/avatars/917390822939447307/762c5053cda62e609ee954b7868b42d5.png?size=4096")
            embed.timestamp = datetime.datetime.utcnow()

            return embed

        elif args == "donate":
            exit

        elif args == "ping":
            exit

    else:
        return

def answerResponse(ctx, question):
    status(ctx, infoStatus, coloredAnswer)

    index = DetectKeywords(question)
    print("INDEXXXXXXXXXXXXX " + index)

    int(index)

    embed = discord.Embed(title=faq[index]["question"], description=faq[index]["answer"], color=embedColor)

    embed.set_footer(text="Tech Support", icon_url="https://cdn.discordapp.com/avatars/917390822939447307/762c5053cda62e609ee954b7868b42d5.png?size=4096")
    embed.timestamp = datetime.datetime.utcnow()

    return embed

def feedbackResponse(ctx, feedback):
    status(ctx, infoStatus, coloredFeedback)

    dmEmbed = discord.Embed(title="Feedback", description=feedback, color=embedColor)
    dmEmbed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)

    embed = discord.Embed(title="Feedback proposed!", description="Thank you for improving the bot :)", color=embedColor)
    embed.set_footer(text="Tech Support", icon_url="https://cdn.discordapp.com/avatars/917390822939447307/762c5053cda62e609ee954b7868b42d5.png?size=4096")
    embed.timestamp = datetime.datetime.utcnow()

    return dmEmbed, embed

def suggestResponse(ctx, suggestion):
    status(ctx, infoStatus, coloredFeedback)

    dmEmbed = discord.Embed(title="Suggestion", description=suggestion, color=embedColor)
    dmEmbed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)

    embed = discord.Embed(title="Suggestion saved!", description="Thank you for improving the bot :)", color=embedColor)
    embed.set_footer(text="Tech Support", icon_url="https://cdn.discordapp.com/avatars/917390822939447307/762c5053cda62e609ee954b7868b42d5.png?size=4096")
    embed.timestamp = datetime.datetime.utcnow()

    return dmEmbed, embed

def donateResponse(ctx):
    status(ctx, infoStatus, coloredDonate)

    embed = discord.Embed(title="Donate", description="If you would like to support development, consider supporting on addresses:", color=embedColor)

    embed.add_field(name="ERC-20: ", value=wallet_ERC20)

    embed.set_footer(text="Tech Support", icon_url="https://cdn.discordapp.com/avatars/917390822939447307/762c5053cda62e609ee954b7868b42d5.png?size=4096")
    embed.timestamp = datetime.datetime.utcnow()

    return embed

def pingResponse(ctx, ping):
    status(ctx, infoStatus, coloredPing)
    embed = discord.Embed(title="Ping", description="Pong! " + str(ping) + "ms", color=embedColor)
    return embed
