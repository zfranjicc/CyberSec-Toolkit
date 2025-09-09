
import asyncio
from telegram import Bot
import random

# Your BOTs API 
# In this case, we are using 4 bots.
TOKENS = [
    "8243152817:nnE5OmGcLNpOpUdALcZsjR7QGqotP9e3f4c",  # Bot A
    "8243152817:nnE5OmGcLNpOpUdALcZsjR7QGqotP9e3f4c",  # Bot B
    "8243152817:nnE5OmGcLNpOpUdALcZsjR7QGqotP9e3f4c",  # Bot C
    "8243152817:nnE5OmGcLNpOpUdALcZsjR7QGqotP9e3f4c"   # Bot D
]

# ID Your Telegram Group
CHAT_ID = -112613668924

# lista emojija
EMOJIS = ["😏","😎","🔥","💸","👀","🍵","🚀","👌"]

# Conversation in order
CONVERSATION_ORDERED = [
    {"bot": 0, "msg": "hey, did you check the new update today?"},
    {"bot": 1, "msg": "not yet, what’s going on?"},
    {"bot": 2, "msg": "there’s a surprise challenge online 🔥"},
    {"bot": 3, "msg": "wow, sounds exciting!"},
    {"bot": 0, "msg": "I’m joining, let’s plan it 😎"},
    {"bot": 1, "msg": "same, don’t want to miss it"},
    {"bot": 2, "msg": "do we need any special tools?"},
    {"bot": 3, "msg": "just some skill and patience 💸"},
    {"bot": 0, "msg": "I’ll get everything ready 👀"},
    {"bot": 1, "msg": "perfect, let’s meet tonight 🚀"},
    {"bot": 2, "msg": "where should we gather?"},
    {"bot": 3, "msg": "at the usual spot 🍵"},
    {"bot": 0, "msg": "I’ll bring some energy drinks 😏"},
    {"bot": 1, "msg": "I’ll take some snacks"},
    {"bot": 2, "msg": "I can bring a few surprises 🎲"},
    {"bot": 3, "msg": "haha, we’ll be fully ready 😎"},
    {"bot": 0, "msg": "can’t wait, it’ll be fun 👌"},
    {"bot": 1, "msg": "yeah, it’s been a while since last time"},
    {"bot": 2, "msg": "totally, looking forward to it"},
    {"bot": 3, "msg": "alright, see you tonight! 👋"},
    # Closing messages
    {"bot": 0, "msg": "bye for now, stay safe ✌️"},
    {"bot": 1, "msg": "catch you later 😎"},
    {"bot": 2, "msg": "can’t wait! 👀"},
    {"bot": 3, "msg": "later, don’t be late 🚀"}
]

async def conversation():
    for step in CONVERSATION_ORDERED:
        bot = Bot(TOKENS[step["bot"]])
        emoji = random.choice(EMOJIS)
        msg = f"{step['msg']} {emoji}"
        try:
            # Send message to Telegram group
            await bot.send_message(chat_id=CHAT_ID, text=msg)
            print(f"Bot{step['bot']+1} sent: {msg}")
        except Exception as e:
            # Print error if bot fails to send
            print(f"Error with Bot {step['bot']+1}: {e}")

        # Short random pause between messages (20-60s) to simulate natural chat
        await asyncio.sleep(random.randint(20,60))

    # Print when conversation is finished
    print("Conversation finished. Script stopped.")

if __name__ == "__main__":
    # Run the asynchronous conversation function
    asyncio.run(conversation())
