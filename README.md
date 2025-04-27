# Discord LLM Bot 🤖

Petit bot Discord utilisant OpenAI pour répondre aux questions.

## Commandes

- `!ask` : Pose une question au bot.

## Technologies

- Python
- discord.py
- OpenAI API
- Railway (prochainement pour l'hébergement)

## Installation locale

```
git clone https://github.com/ton-pseudo/discord_bot.git
cd discord_bot
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate sur Windows
pip install -r requirements.txt
cp .env.example .env  # Crée ton fichier .env
python main.py
```


## 3. Préparer pour le **déploiement Cloud** 🚀

Tu peux maintenant l'héberger **gratuitement** sur un cloud comme **Railway** ou **Render**.

👉 **Railway** est vraiment simple (mon préféré pour bots).

### Sur Railway :
- Va sur [railway.app](https://railway.app/)
- Crée un compte
- Clique sur "**New Project**" ➔ "**Deploy from GitHub Repo**"
- Connecte ton GitHub et choisis ton repo `discord_bot`
- Dans **Settings**, ajoute tes variables d’environnement :
  - `DISCORD_TOKEN` = ton token Discord
  - `OPENAI_API_KEY` = ta clé OpenAI
- Railway détectera ton `python` et ton `requirements.txt` tout seul.


## 4. Ajouter un `Procfile` (important pour que Railway sache comment lancer ton bot)

Ajoute ce fichier tout simple :

📄 `Procfile`




Puis tu le **commit & push** :
```
git add Procfile
git commit -m "Ajout du Procfile pour Railway"
git push
```