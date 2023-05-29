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

f = open("gameboard.txt", "r+", encoding="utf-8")
r = open("newboard.txt", "r", encoding="utf-8")
n = open("newboard.txt", "r", encoding="utf-8")

load_dotenv()
TOKEN = 'YOUR-TOKEN'
GUILD = 'YOUR-SERVER-NAME'

client = discord.Client()

bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


class c4Game:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.boardList = []
        self.length = []
        for i in range(height):
            self.length.append(8)
        print(self.length)
        self.tweetMessage = ""

    def createBoard(self):
        f = open("gameboard.txt", "w", encoding="utf-8")
        n = open("newboard.txt", "r", encoding="utf-8")
        f.write(n.read())
        tally = open("gamenumber.txt", "r", encoding="utf=8")
        gameNumber = int(tally.read())
        gameNumber += 1
        tallyWrite = open("gamenumber.txt", "w", encoding="utf=8")
        tallyWrite.write(str(gameNumber))

    def drawBoard(self):
        z = open("gameboard.txt", "w", encoding="utf-8")
        tally = open("gamenumber.txt", "r", encoding="utf=8")
        gameNumber = tally.read()
        z.write("**Game #**" + gameNumber + "\n\n 0    1    2   3   4   5   6\n")
        for i in self.boardList:
            for item in i:
                z.write(item)
        z.write(" 0    1    2    3    4    5    6")
        print(self.boardList)

    def tweetBoard(self):
        f = open("gameboard.txt", "r", encoding="utf-8")
        general = 499426408213381132
        return f.read() + '\n' + self.tweetMessage

    def readBoard(self):
        for i in f.read():
            self.boardList.append(i)
        board = iter(self.boardList)
        self.boardList = [list(islice(board, length))
                          for length in self.length]
        print(self.boardList)

    def placePiece(self, x, color):
        for i in range(len(self.boardList)):
            k = (len(self.boardList)-1)-i
            if self.boardList[k][x] == "🟦":
                if color == "yellow":
                    self.boardList[k][x] = "🟨"
                    break
                elif color == "red":
                    self.boardList[k][x] = "🟥"
                    break
        # print(self.boardList)

    def winDetection(self):
        endgame = open("endgame.txt", "r")
        red = "\n**Red Wins!**\n" + "\n" + endgame.read()
        yellow = "\n**Yellow Wins!**\n" + "\n" + endgame.read()
        for list in range(len(self.boardList)):
            for item in range(len(self.boardList[list])):
                if self.boardList[list][item] == "🟥" and self.boardList[list][item+1] == "🟥" and self.boardList[list][item+2] == "🟥" and self.boardList[list][item+3] == "🟥":
                    self.tweetMessage = red
                    return 1
                elif self.boardList[list][item] == "🟨" and self.boardList[list][item+1] == "🟨" and self.boardList[list][item+2] == "🟨" and self.boardList[list][item+3] == "🟨":
                    self.tweetMessage = yellow
                    return 1
        for list in range(len(self.boardList)-3):
            for item in range(len(self.boardList[list])):
                if self.boardList[list][item] == "🟥" and self.boardList[list+1][item] == "🟥" and self.boardList[list+2][item] == "🟥" and self.boardList[list+3][item] == "🟥":
                    self.tweetMessage = red
                    return 1
                if self.boardList[list][item] == "🟨" and self.boardList[list+1][item] == "🟨" and self.boardList[list+2][item] == "🟨" and self.boardList[list+3][item] == "🟨":
                    self.tweetMessage = yellow
                    return 1
                if self.boardList[list][item] == "🟥" and self.boardList[list+1][item+1] == "🟥" and self.boardList[list+2][item+2] == "🟥" and self.boardList[list+3][item+3] == "🟥":
                    self.tweetMessage = red
                    return 1
                if self.boardList[list][item] == "🟨" and self.boardList[list+1][item+1] == "🟨" and self.boardList[list+2][item+2] == "🟨" and self.boardList[list+3][item+3] == "🟨":
                    self.tweetMessage = yellow
                    return 1
                if self.boardList[list][item] == "🟥" and self.boardList[list+1][item-1] == "🟥" and self.boardList[list+2][item-2] == "🟥" and self.boardList[list+3][item-3] == "🟥":
                    self.tweetMessage = red
                    return 1
                if self.boardList[list][item] == "🟨" and self.boardList[list+1][item-1] == "🟨" and self.boardList[list+2][item-2] == "🟨" and self.boardList[list+3][item-3] == "🟨":
                    self.tweetMessage = yellow
                    return 1

