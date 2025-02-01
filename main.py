""" main.py - starts and control betty bot process"""
# required libraries for code to run.
from dotenv import load_dotenv, dotenv_values
from datetime import datetime
from modules import functions
import discord,os

# Initiating enviroment variables
load_dotenv()

# Intents are required for client creation, creating intent to read message content.
intent = discord.Intents.default()
intent.message_content = True
# Creating discord client for betty.
client = discord.Client(intents=intent) 
headers = {'Accept':'application/json'} 
word_list = functions.word_list()

@client.event
async def on_ready(): print("{0.user} is ready for dutty".format(client))

@client.event
async def on_message(message):
  

  if message.author == client.user:
     return
 
  if any(word in message.content.split() for word in word_list):
     joke = functions.get_joke(str(os.getenv('URL')), headers)
     await message.channel.send(joke)
  if message.content.startswith('$time'):
     await message.channel.send('The time is: ' + datetime.now().strftime("%I:%M %p"))
  if message.content.startswith('$date'):
     await message.channel.send("Today is " + datetime.now().strftime("%A %b %d %Y"))


# both getenv() method and using the environ[?] dictionary accepted
client.run(os.getenv('TOKEN'))

