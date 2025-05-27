import discord
from discord.ext import commands
import random


TOKEN = ("TOKEN")

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="/", intents=intents)
intents.message_content = True


@bot.command(name="inquinamento")
async def pollution(ctx):
    message1 = (
        "🌍 **Consapevolezza dell'inquinamento** 🌍\n"
        "L'inquinamento è l'immissione di sostanze nocive nell'ambiente."
        "Colpisce l'aria, l'acqua e il suolo, causando danni a esseri umani, animali e piante.\n\n"
        "**Tipi di inquinamento:**\n"
        "- Inquinamento atmosferico\n"
        "- Inquinamento idrico\n"
        "- Inquinamento del suolo\n"
        "- Inquinamento acustico\n\n"
        "Lavoriamo insieme per ridurre l'inquinamento e proteggere il nostro pianeta! 💚"
    )
    await ctx.send(message1)

@bot.command(name="soluzioni")
async def solutions(ctx):
    message2 = (
        "💡 **Soluzioni all'inquinamento** 💡\n"
"Ecco alcuni modi per ridurre l'inquinamento:\n"
"- Ridurre, Riutilizzare, Riciclare ♻️\n"
"- Utilizzare i mezzi pubblici o condividere l'auto 🚍\n"
"- Risparmiare energia spegnendo luci e dispositivi elettronici 🔌\n"
"- Evitare la plastica monouso 🛍️\n"
"- Piantare alberi e sostenere la riforestazione 🌳\n"
"- Diffondere consapevolezza ed educare gli altri 📢\n\n"
"Ogni piccolo passo conta per un pianeta più pulito e più sano! 🌟"
    )
    await ctx.send(message2)

@bot.command(name="helpme")
async def helpme(ctx):
    message3 = (
        "🤖 **Comandi del bot** 🤖\n"
        "Usa i comandi seguenti per interaggire con il bot:\n"
        "- `/inquinamento`: Impara qualcosa sull'inquinamento.\n"
        "- `/soluzioni`: Soluzioni per l'inquinamento.\n"
        "- `/catania`: Calendario riciclo di Catania.\n"
        "- `/siracusa`: Calendario riciclo di Siracusa.\n"
        "- `/curiosita`: Curiosità casuale.\n"
        "- `/helpme`: Farà apparire questo messaggio.\n\n"
        "Insieme posiamo fare la differenza! 🌍"
    )
    await ctx.send(message3)

@bot.command(name="catania")
async def helpme(ctx):
    message4 = (
        "**Riciclo a Catania**\n"
        "Organico: Domenica, Lunedì, Mercoledì, Giovedì, \n"
        "Secco residuo: Giovedì. \n"
        "Plastica e Metalli: Lunedì, Giovedì. \n"
        "Carta e Cartone: Mercoledì. \n"
        "Vetro: Martedì, Venerdì. \n"
        "Pannolini/Pannoloni: Lunedì, Mercoledì, Giovedì e Venerdì (in sacchetti separati)."
        )
    await ctx.send(message4)

@bot.command(name="siracusa")
async def helpme(ctx):
    message5 = (
        "**Riciclo a Siracusa**\n"
        "Organico: Lunedì, Mercoledì, Venerdì, \n"
        "Secco residuo: Giovedì. \n"
        "Plastica e Metalli: Mercoledì. \n"
        "Carta e Cartone: Martedì, Sabato. \n"
        "Vetro: Lunedì."
        )
    await ctx.send(message5)   


@bot.command(name="curiosita")
async def pollution_facts(ctx):
    facts = [
        "🌍 **L'inquinamento dell'aria riduce l'aspettativa di vita**: Si stima che ogni anno milioni di persone muoiano prematuramente a causa dell'inquinamento atmosferico.",
        "🌱 **Le piante assorbono inquinanti**: Gli alberi e le piante aiutano a ridurre l'inquinamento assorbendo CO₂ e altre sostanze nocive dall'aria.",
        "💡 **La plastica impiega secoli a decomporsi**: Un sacchetto di plastica può impiegare fino a 1000 anni per degradarsi completamente.",
        "🚗 **Il traffico è uno dei principali responsabili dell'inquinamento**: I gas di scarico dei veicoli contribuiscono al riscaldamento globale e alla formazione di smog.",
        "🏭 **Le industrie sono tra i maggiori inquinatori**: Molti stabilimenti rilasciano grandi quantità di gas serra e sostanze tossiche nell'aria e nelle acque.",
        "🌊 **Gli oceani soffrono per l'inquinamento**: Ogni anno milioni di tonnellate di plastica finiscono nei mari, danneggiando l'ecosistema marino.",
        "⚡ **L'energia pulita può ridurre drasticamente l'inquinamento**: L'uso di energia solare ed eolica può aiutare a diminuire le emissioni di CO₂.",
        "🚭 **Le sigarette inquinano più di quanto si pensi**: I mozziconi di sigaretta sono tra i rifiuti più comuni e contengono sostanze tossiche che contaminano il suolo e l'acqua.",
        "🦠 **L'inquinamento dell'aria può danneggiare il cervello**: Studi suggeriscono che l'esposizione prolungata all'inquinamento atmosferico può influenzare negativamente le funzioni cognitive.",
        "🌡️ **L'inquinamento contribuisce al cambiamento climatico**: Le emissioni di gas serra, come il CO₂, aumentano la temperatura globale e causano eventi climatici estremi."
    ]

    fact = random.choice(facts)
    await ctx.send(f"🔎 **Curiosità sull'inquinamento:**\n{fact}")
@bot.event
async def on_ready():
    print(f"Il bot è online {bot.user}")


bot.run(TOKEN)
