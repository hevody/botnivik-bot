# This example requires the 'message_content' intent.

import discord

### fetching the discord token ###
with open('my_bot_token.env') as f:
  my_bot_token = f.read()

### 1. initializing the bot ###
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

### 3. bot waiting for events ### 
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

### 2. running the bot ###
client.run(my_bot_token)
