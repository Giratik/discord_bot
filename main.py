import discord
import openai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

openai.api_key = OPENAI_API_KEY

@client.event
async def on_ready():
    print(f'🤖 Connecté en tant que {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ask"):
        prompt = message.content[5:].strip()
        if not prompt:
            await message.channel.send("Donne-moi une question après `!ask` !")
            return
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            bot_reply = response.choices[0].message.content
            await message.channel.send(bot_reply)
        except Exception as e:
            await message.channel.send(f"Erreur lors de l'appel à OpenAI : {e}")

client.run(DISCORD_TOKEN)
