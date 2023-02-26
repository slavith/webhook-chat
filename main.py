import discord_webhook
from discord_webhook import DiscordWebhook
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import os
import time
import requests



os.system("title Webhook Chat")

front = f"""

{Fore.BLUE}██{Fore.RED}╗{Fore.BLUE}    ██{Fore.RED}╗{Fore.BLUE}███████{Fore.RED}╗{Fore.BLUE}██████{Fore.RED}╗{Fore.BLUE} ██{Fore.RED}╗{Fore.BLUE}  ██{Fore.RED}╗{Fore.BLUE} ██████{Fore.RED}╗{Fore.BLUE}  ██████{Fore.RED}╗{Fore.BLUE} ██{Fore.RED}╗{Fore.BLUE}  ██{Fore.RED}╗{Fore.BLUE}     ██████{Fore.RED}╗{Fore.BLUE}██{Fore.RED}╗{Fore.BLUE}  ██{Fore.RED}╗{Fore.BLUE} █████{Fore.RED}╗{Fore.BLUE} ████████{Fore.RED}╗
{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}    ██{Fore.RED}║{Fore.BLUE}██{Fore.RED}╔════╝{Fore.BLUE}██{Fore.RED}╔══{Fore.BLUE}██{Fore.RED}╗{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}  ██{Fore.RED}║{Fore.BLUE}██{Fore.RED}╔═══{Fore.BLUE}██{Fore.RED}╗{Fore.BLUE}██{Fore.RED}╔═══{Fore.BLUE}██{Fore.RED}╗{Fore.BLUE}██{Fore.RED}║{Fore.BLUE} ██{Fore.RED}╔╝{Fore.BLUE}    ██{Fore.RED}╔════╝{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}  ██{Fore.RED}║{Fore.BLUE}██{Fore.RED}╔══{Fore.BLUE}██{Fore.RED}╗╚══{Fore.BLUE}██{Fore.RED}╔══╝
{Fore.BLUE}██{Fore.RED}║{Fore.BLUE} █{Fore.RED}╗{Fore.BLUE} ██{Fore.RED}║{Fore.BLUE}█████{Fore.RED}╗{Fore.BLUE}  ██████{Fore.RED}╔╝{Fore.BLUE}███████{Fore.RED}║{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}   ██{Fore.RED}║{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}   ██{Fore.RED}║{Fore.BLUE}█████{Fore.RED}╔╝{Fore.BLUE}     ██{Fore.RED}║{Fore.BLUE}     ███████{Fore.RED}║{Fore.BLUE}███████{Fore.RED}║{Fore.BLUE}   ██{Fore.RED}║   
{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}███{Fore.RED}╗{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}██{Fore.RED}╔══╝{Fore.BLUE}  ██{Fore.RED}╔══{Fore.BLUE}██{Fore.RED}╗{Fore.BLUE}██{Fore.RED}╔══{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}   ██{Fore.RED}║{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}   ██{Fore.RED}║{Fore.BLUE}██{Fore.RED}╔═{Fore.BLUE}██{Fore.RED}╗{Fore.BLUE}     ██{Fore.RED}║{Fore.BLUE}     ██{Fore.RED}╔══{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}██{Fore.RED}╔══{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}   ██{Fore.RED}║   
{Fore.RED}╚{Fore.BLUE}███{Fore.RED}╔{Fore.BLUE}███{Fore.RED}╔╝{Fore.BLUE}███████{Fore.RED}╗{Fore.BLUE}██████{Fore.RED}╔╝{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}  ██{Fore.RED}║╚{Fore.BLUE}██████{Fore.RED}╔╝╚{Fore.BLUE}██████{Fore.RED}╔╝{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}  ██{Fore.RED}╗    ╚{Fore.BLUE}██████{Fore.RED}╗{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}  ██{Fore.RED}║{Fore.BLUE}██{Fore.RED}║{Fore.BLUE}  ██{Fore.RED}║{Fore.BLUE}   ██{Fore.RED}║   
{Fore.RED} ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                                                 

                                    {Fore.BLUE}[{Fore.RED}*{Fore.BLUE}] Coded by >slavith#0001

"""
print(front)
user_webhook = input(f"{Fore.BLUE}[{Fore.RED}webhook{Fore.BLUE}] Enter your webhook url > ")
os.system("cls")

def repeat():
    msg = input(f"{Fore.BLUE}[{Fore.RED}message{Fore.BLUE}] Enter your message > ")
    send = DiscordWebhook(url=user_webhook, content=msg)
    response = send.execute()
    status = requests.get(user_webhook)
    print(f"{Fore.BLUE}[{Fore.RED}+{Fore.BLUE}] Message successfully sent!")
    time.sleep(1)
    os.system("cls")
    repeat()
repeat()



