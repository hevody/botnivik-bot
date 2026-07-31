import discord

### 2. definition of class ###
class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')


### fetching the discord token ###
with open('my_bot_token.env') as f:
  my_bot_token = f.read()

### 1. initialization of the bot ### 
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(my_bot_token)