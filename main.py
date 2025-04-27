import discord
import openai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.message_content = True  # Important pour lire les messages

# Utiliser un bot avec des commandes slash
bot = discord.Bot(intents=intents)

openai.api_key = OPENAI_API_KEY

@bot.event
async def on_ready():
    print(f'🤖 Connecté en tant que {bot.user}')

# Slash command /ask
@bot.slash_command(name="ask", description="Pose une question au bot et il te répondra grâce à OpenAI")
async def ask(ctx: discord.ApplicationContext, question: str):
    await ctx.defer()  # Pour indiquer que le bot prend un peu de temps

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        bot_reply = response.choices[0].message.content
        await ctx.respond(bot_reply)
    except Exception as e:
        await ctx.respond(f"Erreur lors de l'appel à OpenAI : {e}")

bot.run(DISCORD_TOKEN)
