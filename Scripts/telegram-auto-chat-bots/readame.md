# Telegram Auto Chat Bot 🤖💬

Automated conversation between multiple Telegram bots in a Telegram group.  
Each bot sends predefined messages with **random emojis** and **random delays** to simulate a natural chat.

---

## Table of Contents
- [Description](#description)
- [Prerequisites](#prerequisites)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Script](#running-the-script)
- [How It Works](#how-it-works)
- [Security](#security)
- [License](#license)

---

## Description
This Python script allows 4 Telegram bots to **simulate a natural conversation** in a group chat.  
Each bot sends messages according to a predefined order, but with **random emojis** and **random pauses** between 20–60 seconds.  

It can be used for:  
- Testing Telegram bot setups  
- Demonstrating automated messaging  
- Fun automated chat simulation  

---

## Prerequisites
Before running the script, make sure you have:  

1. **Python 3** installed. Check version with `python3 --version`.  
   If not installed, install Python and pip using your package manager.  

2. **Internet connection** – the script needs to connect to Telegram servers  

3. **Telegram bots** created using [BotFather](https://t.me/botfather).  
   - Copy the bot tokens for later configuration  

---

## Dependencies
The script needs the Python library `python-telegram-bot` to connect to Telegram API.  

- On Kali Linux, you **cannot install packages directly into the system Python** due to security rules (PEP 668).  
- The solution is to use a **virtual environment**.

---

## Installation

### Step 1 – Clone the repository
```
git clone https://github.com/zfranjicc/CyberSec-Toolkit.git
cd CyberSec-Toolkit/Scripts/telegram-auto-chat-bots
python3 main.py
```


### Step 2 – Create a virtual environment
```
python3 -m venv mybotenv
```
- This creates an isolated Python environment in the folder `mybotenv`.

### Step 3 – Activate the virtual environment

```
source mybotenv/bin/activate
```
- Your terminal prompt will show `(mybotenv)` indicating that the virtual environment is active.

### Step 4 – Install dependencies inside the virtual environment

```
pip install python-telegram-bot
```
---

## Configuration
1. Add your bot tokens and chat ID (you can put them **directly in `main.py`**, which is recommended for simplicity):
2. Replace `token1, token2…` with your **actual bot tokens**.  
3. Replace `CHAT_ID` with your **Telegram group ID** (negative for supergroups).   
## Running the Script
After activating the virtual environment and installing dependencies:

1. Make sure you are in the project folder.  
2. Activate virtualenv if not already: `source mybotenv/bin/activate`  
3. Run the script: `python3 main.py`  

- Bots will start sending messages according to `CONVERSATION_ORDERED`.  
- Each message gets a **random emoji** from the `EMOJIS` list.  
- Each message is delayed randomly between 20–60 seconds to appear natural.  
- Logs are printed in the console showing which bot sent which message.  

To stop the script, press `Ctrl + C`.  

---

## How It Works
1. `CONVERSATION_ORDERED` – A list of dictionaries specifying which bot sends which message.  
2. `async def conversation()` – Sends messages asynchronously:  
   - Picks the bot using the token  
   - Adds a random emoji  
   - Sends the message to the Telegram group  
   - Waits 20–60 seconds before the next message  
3. Errors are caught and printed, so one failed bot does not stop the script.  
4. Script ends after all messages are sent.  

---

## Security
- **Never share your bot tokens publicly**.  
- Use `.env` and `.gitignore` to keep tokens private.  
- Only use this bot in groups you control or have permission to automate.  

---

> ⚠️ **Disclaimer:** This cheatsheet is intended for educational purposes only.  
> It is meant to support learning and ethical use of cybersecurity tools and techniques.  
> Unauthorized access or misuse of systems is illegal and strictly discouraged.


