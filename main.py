import discord
from discord.ext import commands



TOKEN = ("INSERIRE TOKEN")

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)
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
        "- `!inquinamento`: Impara qualcosa sull'inquinamento.\n"
        "- `!soluzioni`: Soluzioni per l'inquinamento.\n"
        "- `!catania`: Calendario riciclo di Catania.\n"
        "- `!siracusa`: Calendario riciclo di Siracusa.\n"
        "- `!curiosita`: Curiosità o notizia della settimana.\n"
        "- `!helpme`: Farà apparire questo messaggio.\n\n"
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
async def helpme(ctx):
    message6 = (
        "L'Ozono si Restringe (Ma non è una sorpresa): \n" 
        "Una notizia positiva, ma non una 'curiosità' dell'ultimissima settimana, è che il buco dell'ozono si sta restringendo. \n" 
        "Questo è il risultato di un accordo globale storico (Protocollo di Montreal del 1987) che ha vietato i clorofluorocarburi (CFC). \n" 
        "Questo dimostra come l'azione coordinata a livello internazionale possa portare a risultati significativi nella lotta all'inquinamento, \n" 
        "anche se i tempi di recupero sono lunghi. La 'curiosità' qui è quanto tempo ci voglia perché la Terra guarisca da danni che abbiamo causato rapidamente"
        )
    await ctx.send(message6)  
@bot.event
async def on_ready():
    print(f"Il bot è online {bot.user}")


bot.run(TOKEN)
