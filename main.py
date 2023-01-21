import discord

token = "<client token here>"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    await message.channel.send(message.content)

client.run(token)
