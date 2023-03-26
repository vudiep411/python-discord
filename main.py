import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
import requests


load_dotenv()  # load variables from .env file
bot_token = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

cuss = ["fuck", "bitch", "nigga", "shit", "fuk", "nigger", "whore", "pussy", "fag", "dumbass"]
cussReply = ["Stop cussing u little bitch", "stfu hoe stop cussing", "Stop cussing stupid bitch", "stfu foo stop cussing", "stop cussing dumbass bitch", "stop cuss bitch ass n****"]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$generate"):
        prompt = ' '.join(message.content.split()[1:])
        res = requests.get(f"https://lexica.art/api/v1/search?q=${prompt}")
        data = res.json()

        for i in range(5):
            random_idx = random.randint(0, len(data["images"]))
            await message.channel.send(data["images"][random_idx]["src"], reference=message)
    
    if message.content.startswith("$quote"):
        res = requests.get("https://type.fit/api/quotes")
        quotes = res.json()
        random_idx = random.randint(0, len(quotes))
        q = quotes[random_idx]["text"]
        author = quotes[random_idx]["author"] if quotes[random_idx]["author"] else ""
        await message.channel.send(f"*{q}* \n *-{author}*", reference=message)

    r = random.randint(0, len(cussReply) - 1)
    for c in cuss:
        if c in message.content.lower():
            await message.channel.send(cussReply[r])


client.run(bot_token)


