import discord
import os
import random
from keep_alive import keep_alive
from discord.ext.commands import Bot

BOT_PREFIX = ("!")

client = commands.Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('------')

@client.command(name='TiltBot', 
                description="Tilts whoever calls the bot.",
                brief="Tilting statements.",
                aliases=['tilt_me', 'tiltme', 'tilt','Tilt_me', 'Tiltme', 'Tilt', 'Tilt_Me', 'TiltMe'],
                pass_context=True)
async def tilt_bot(context):
  possible_responses = [
    'Get fucked',
    'I didn\'t know bots could ping me',
    'Don\'t worry, I\'m sure you can ask Ryse to boost you too',
  ]
  await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name='CalmBot', 
                description="De-tilts whoever calls the bot.",
                brief="Not tilting statements.",
                aliases=['calm', 'relax', 'untilt'],
                pass_context=True)
async def tilt_bot(context):
  possible_responses = [
    'Just blame Saway',
    'They were smurfing, doesn\'t count',
    'You were playing on like, 100 ping, it wasn\'t fair',
    'Don\'t worry, you\'re Top 500 in my heart :heart:',
  ]
  await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
