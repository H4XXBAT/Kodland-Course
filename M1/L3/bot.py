import discord
from bot_logic import gen_pass
from settings_utils import settings

# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send("Ciao!")
    if message.content.startswith('$password'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$arrivederci'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send("Il messaggio inserito non è corretto, per usare il bot puoi inserire questi comandi: $ciao e $arrivederci")

client.run(settings["TOKEN"])
