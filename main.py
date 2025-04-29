import discord
from datetime import datetime
import os
from discord.ext import commands
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Crée une instance du client Discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)

intents.message_content = True
bot=commands.Bot(command_prefix="--",case_insensitive=True,intents=intents)
bot.remove_command("help")

# Événement qui se déclenche lorsque le bot est prêt
@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')

# Événement qui se déclenche lorsqu'un message est reçu
@client.event
async def on_message(message):
    # Ignore les messages envoyés par le bot lui-même pour éviter les boucles infinies
    if message.author == client.user:
        return

    # Vérifie si le message commence par la commande !date
    if message.content.startswith('!date'):
        # Obtient la date actuelle
        now = datetime.now()
        date_actuelle = now.strftime("%d/%m/%Y")
        # Envoie la date dans le canal où la commande a été envoyée
        await message.channel.send(f"La date actuelle est : {date_actuelle}")

# Lance le bot avec le token
client.run(TOKEN)