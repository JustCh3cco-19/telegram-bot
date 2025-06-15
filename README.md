# Telegram Finance & Fun Bot 🇮🇹

> **A multi-purpose Telegram bot that delivers finance data and fun commands, built with `python-telegram-bot` and `yfinance`.**

This Telegram bot retrieves real-time financial data from Yahoo Finance and offers several playful commands—all in Italian. Built with Python, it's perfect for experimenting with bots that combine utility and entertainment.

---

## 🧠 Features

### 🎯 Core Commands (in Italian)

- `/start` – Sends a welcome message.
- `/addizione` – Adds two numbers and returns the result.
- `/dice` – Rolls a dice and challenges the user.
- `/gatto` – Sends a random cat photo from a local directory.
- `/mario` – Sends a classic Mario sound effect (audio).
- `/marketcap` – Returns market capitalizations of predefined stocks via Yahoo Finance.
- `/stocks` – Returns current prices of predefined stocks via Yahoo Finance.

---

## 📈 Finance Integration

- Uses the [`yfinance`](https://pypi.org/project/yfinance/) Python library to query financial data.
- Predefined stock symbols are hardcoded in the bot.
- Work in progress: user-defined stock input and dynamic download.

---

## 🚀 Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/JustCh3cco-19/telegram-bot.git
cd telegram-bot
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your bot token:
```env
BOT_TOKEN=your_telegram_token_here
```

4. Start the bot:
```bash
python bot.py
```

---

## 📁 File Structure

```
├── bot.py              # Main bot logic
├── requirements.txt    # Python dependencies
├── .env                # Your secret bot token
├── /images             # Folder with cat pictures
├── /audio              # Folder with sound effects (e.g. mario.wav)
```
