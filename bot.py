import logging
import os
import random

from dotenv import load_dotenv
from telegram import Update, InputFile
from telegram.ext import (
    filters,
    MessageHandler,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
import yfinance as yf
from urllib.parse import quote

load_dotenv()
token = os.getenv("TOKEN")


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


# Comandi bot
# messaggio di benvenuto
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_username = update.message.from_user.username
    response_text = f"Ciao, @{user_username}! Clicca sul menu per sapere i comandi disponibili per questo bot!"
    await update.message.reply_text(response_text)


# ricevi il prezzo delle stocks
async def stocks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stock_symbols = [
        "AAPL",
        "MSFT",
        "GOOG",
        "AMZN",
        "NVDA",
        "TSLA",
        "RACE",
        "ORCL",
        "ASML",
        "AMD",
        "SONY",
        "SPOT",
        "META",
        "NFLX",
        "PYPL",
        "SMSN.IL",
        "CS",
    ]
    response_text = ""
    stampata_stock = True
    for stock_symbol in stock_symbols:
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.info
        if "currentPrice" in stock_info and stock_info["currentPrice"]:
            stock_price = stock_info["currentPrice"]
            if stampata_stock:
                response_text += "Prezzo delle stocks selezionate\n"
                stampata_stock = False
            stock_search_query = quote(f"{stock_symbol}")
            stock_search_url = f"https://finance.yahoo.com/quote/{stock_search_query}"
            graph_url = f"[Grafico andamento]({stock_search_url})"
            response_text += f"{stock_symbol}: {stock_price}$ - {graph_url}\n"
        else:
            response_text += f"Impossibile ottenere il prezzo delle stocks di {stock_symbol} al momento.\n"
    await update.message.reply_markdown(response_text, disable_web_page_preview=True)


# market cap
async def marketcap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stock_symbols = [
        "AAPL",
        "MSFT",
        "GOOG",
        "AMZN",
        "NVDA",
        "TSLA",
        "RACE",
        "ORCL",
        "ASML",
        "AMD",
        "SONY",
        "SPOT",
        "META",
        "NFLX",
        "PYPL",
        "SMSN.IL",
        "CS",
    ]
    response_text = ""
    stampata_mcap = True
    for stock_symbol in stock_symbols:
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.info
        if "marketCap" in stock_info and stock_info["marketCap"]:
            market_cap = stock_info["marketCap"]
            if stampata_mcap:
                response_text += "Market cap delle aziende selezionate\n"
                stampata_mcap = False
            stock_search_query = quote(f"{stock_symbol}")
            stock_search_url = f"https://finance.yahoo.com/quote/{stock_search_query}"
            graph_url = f"[Market cap]({stock_search_url})"
            response_text += f"{stock_symbol}: {market_cap}$ - {graph_url}\n"
        else:
            response_text += (
                f"Impossibile ottenere il market cap di {stock_symbol} al momento.\n"
            )
    await update.message.reply_markdown(response_text, disable_web_page_preview=True)


# funzione che copia i messaggi dell'utente e li reinvia
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_username = update.message.from_user.username
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"@{user_username} ha scritto: {update.message.text}",
    )


# invia una foto random di un gatto presente nella cartella photo
async def gatto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_folder = "photo/gatto"
    photo_files = os.listdir(photo_folder)
    random_photo_file = random.choice(photo_files)
    photo_path = os.path.join(photo_folder, random_photo_file)
    with open(photo_path, "rb") as photo:
        await context.bot.send_document(
            chat_id=update.effective_chat.id,
            document=InputFile(photo),
            caption="Gatto del giorno",
        )


# manda un dado interattivo in chat
async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_dice(chat_id=update.effective_chat.id)


# addizione tra due numeri
async def addizione(update: Update, context: ContextTypes.DEFAULT_TYPE):
    x = 1
    y = 1
    addizione = x + y
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Il risultato di {x}+{y} è: {addizione}"
    )


async def mario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    audio_folder = "music/supermario"
    audio_files = os.listdir(audio_folder)
    random_audio_file = random.choice(audio_files)
    audio_path = os.path.join(audio_folder, random_audio_file)
    with open(audio_path, "rb") as audio:
        await context.bot.send_document(
            chat_id=update.effective_chat.id,
            document=InputFile(audio),
            caption="Super Mario del giorno",
        )


# comandi non presenti nel bot (va aggiunto come ultimo comando anche nella parte if __name__ == "__main__")
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Comando inesistente. Scrivi /help per avere la lista di tutti i comandi del bot.",
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler("start", start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    stocks_handler = CommandHandler("stocks", stocks)
    gatto_handler = CommandHandler("gatto", gatto)
    dice_handler = CommandHandler("dice", dice)
    addizione_handler = CommandHandler("addizione", addizione)
    mario_handler = CommandHandler("mario", mario)
    marketcap_handler = CommandHandler("marketcap", marketcap)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(stocks_handler)
    application.add_handler(gatto_handler)
    application.add_handler(dice_handler)
    application.add_handler(addizione_handler)
    application.add_handler(mario_handler)
    application.add_handler(marketcap_handler)

    application.add_handler(unknown_handler)

    application.run_polling()
