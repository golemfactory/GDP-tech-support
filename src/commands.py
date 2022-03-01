
import datetime

from colorama import Fore, Style


def printWithTime(textToPrint):   
    now = datetime.datetime.now()
    time = now.strftime("[%Y-%m-%d %H:%M:%S] ")
    print(Fore.GREEN + time + textToPrint)

def status(ctx, infoStatus, color):
    authorName = "\"" + ctx.author.name + "\" " + "used a "
    channelName =  "command in channel" + Fore.LIGHTCYAN_EX + " #" + ctx.channel.name + ". " + Style.RESET_ALL
    
    now = datetime.datetime.now()
    time = now.strftime("[%Y-%m-%d %H:%M:%S] ")
    print(Fore.GREEN + time + infoStatus + authorName + color + channelName)

 