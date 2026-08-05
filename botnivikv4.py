import discord
import random
import awv9U1ekja3Q

### fetching the discord token ###
with open('my_bot_token.env') as f:
  my_bot_token = f.read()

### variable declaration ###
channel_ids = {
   'botnivik': 1532586964036092206
}
help = {
  'commands': {
    'help': ['➡️ `.help`', 'displays this help page'],
    'passwordgen': ['➡️ `.passwordgen`', 'generates a 15-character password'],
    'obfuscated_1': [f'➡️ {awv9U1ekja3Q.command_name}', awv9U1ekja3Q.command_help],
    '.': ['➡️ `.`', 'debugs the bot'],
  }
}
### 1. initialization of the bot ###
client = discord.Client(intents=discord.Intents.all())

### 3. bot events ###
@client.event
async def on_ready():
  print(f'We have logged in as {client.user}') 

@client.event
async def on_message(message):
  if message.author != client.user:
    if message.channel.id in channel_ids.values():
      if message.content == '.passwordgen':
        ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'
        punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        candidate_list = []
        
        alphanumpunc = ascii_letters + digits + punctuation
        alphanumpuncList = list(alphanumpunc)
        for _ in range(15):
          candidate = random.choice(alphanumpuncList)
          candidate_list += candidate
        password = ''.join(candidate_list)
        embed = discord.Embed(title="Generated password",     
                                      description=password,
                                      colour=discord.Colour.purple())
        embed.set_author( name=message.author,
                          icon_url="https://i.pinimg.com/736x/83/11/1a/83111a294e4eff3e42c905fa21908cbf.jpg" )
        await message.channel.send(embed=embed)
      if message.content.startswith(awv9U1ekja3Q.tXO5l):
        arguments = message.content.split()
        RWs3xFJ = awv9U1ekja3Q.main(arguments[1], arguments[2])
        embed = discord.Embed(title="Success!",
                              description=RWs3xFJ,
                              colour=discord.Colour.purple())
        embed.set_author(name=message.author,
                         icon_url="https://i.pinimg.com/736x/83/11/1a/83111a294e4eff3e42c905fa21908cbf.jpg")
        await message.channel.send(embed=embed)
        
      if message.content == '.help':
        embed = discord.Embed(title='List of all available commands', color=0x49fc03)
        for i in help['commands'].keys():
          embed.add_field(name=help['commands'][i][0], value=help['commands'][i][1], inline=False)
        await message.channel.send(embed=embed)

### 2. running the bot ###
client.run(my_bot_token)

