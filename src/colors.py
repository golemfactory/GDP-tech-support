
from colorama import init, Fore, Style

from variables import prefix

init()

infoStatus = Fore.YELLOW + "[INFO] "  + Style.RESET_ALL
errorStatus = Fore.RED + "[INFO] " + Style.RESET_ALL

coloredHelp = Fore.LIGHTCYAN_EX + "[" + prefix + "help] " + Style.RESET_ALL
coloredHelpFeedback = Fore.LIGHTCYAN_EX + "[" + prefix + "help feedback] " + Style.RESET_ALL 
coloredHelpSuggest = Fore.LIGHTCYAN_EX + "[" + prefix + "help suggest] " + Style.RESET_ALL
coloredAnswer = Fore.LIGHTCYAN_EX + "[" + prefix + "answer] " + Style.RESET_ALL
coloredFeedback = Fore.LIGHTCYAN_EX + "[" + prefix + "feedback] " + Style.RESET_ALL
coloredSuggest = Fore.LIGHTCYAN_EX + "[" + prefix + "suggest] " + Style.RESET_ALL
coloredDonate = Fore.LIGHTCYAN_EX + "[" + prefix + "donate] " + Style.RESET_ALL
coloredPing = Fore.LIGHTCYAN_EX + "[" + prefix + "ping] " + Style.RESET_ALL
