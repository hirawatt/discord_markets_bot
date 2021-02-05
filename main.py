import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

#token = open("token.txt", "r").read()
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(ctx):
  if "python" in str(ctx.content.lower()):
      await ctx.channel.send('accepted!')
  elif "discord" in str(ctx.content.lower()):
      await ctx.channel.send('accepted!')
  elif "lego" in str(ctx.content.lower()):
      await ctx.channel.send('accepted!')
  elif "code" in str(ctx.content.lower()):
      await ctx.channel.send('accepted!')
client.run(token)

'''
mongo = os.getenv('MONGO_DB')
cluster = MongoClient(mongo)
db = cluster["UserData"]
collection = db["UserData"]

if "python" in str(ctx.content.lower()):
    post = {"_id": ctx.author.id, "score": 1}
    collection.insert_one(post)
    await ctx.channel.send('accepted!')
'''
