# bot.py
import asyncio
import os
import random
import discord
from discord.ext.commands import bot
from dotenv import load_dotenv
from discord.ext import commands
import time
import numpy as np
from itertools import islice
import game as g
import sys

f = open("gameboard.txt", "r+", encoding="utf-8")
r = open("newboard.txt", "r", encoding="utf-8")
n = open("newboard.txt", "r", encoding="utf-8")

load_dotenv()
TOKEN = 'ODI0ODQ4ODE3MTA3MTA3ODUw.YF1WUg.xeDTgrpgkLKymU_sRIEomFzmW_I'
GUILD = 'League'

client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if "start new c4" in message.content.lower():
        time.sleep(0.1)
        welcome = open("welcome.txt", "r")
        time.sleep(0.1)
        await message.channel.send(welcome.read())
        game1 = g.c4Game(7, 6)

        game1.createBoard()
        game1.readBoard()
        game1.drawBoard()

        await message.channel.send(game1.tweetBoard())

        # while not gameOver:
        @client.event
        async def on_message(message):
            if "!c4 " in message.content.lower():
                color = message.content.lower().split(" ")[1]
                column = message.content.lower().split(" ")[2]
                time.sleep(0.5)
                game1.placePiece(int(column), color)
                game1.winDetection()
                game1.drawBoard()
                await message.channel.send(game1.tweetBoard())
            if "!c4reset" in message.content.lower():
                os.execv(sys.executable, ['python'] + sys.argv)
        gameOver = game1.winDetection()
        if gameOver == 1:
            os.execv(sys.executable, ['python'] + sys.argv)


# def gameLoop():
#     gameOver = False
#     game1 = g.c4Game(7, 6)
#
#     game1.createBoard()
#     game1.readBoard()
#     game1.drawBoard()
#
#     async def send():
#         await client.get_channel("499426408213381132").send(game1.tweetBoard())
#
#     while not gameOver:
#         @client.event
#         async def on_message(message):
#             color = message.split(" ")[0]
#             column = message.split(" ")[1]
#             game1.placePiece(int(column), color)
#             game1.winDetection()
#             game1.drawBoard()
#             await message.channel.send(game1.tweetBoard())
#
#         if game1.winDetection() == 1:
#             gameOver = True


client.run(TOKEN)
