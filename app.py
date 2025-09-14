# app.py  (discord.py-self 1.9.2  ✔)
from datetime import datetime
import os
from dotenv import load_dotenv
import discord
from discord.ext import tasks

load_dotenv()

TOKEN      = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

MESSAGE = "Pesan otomatis 10 detik sekali ⏰"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"[{datetime.utcnow()}] Bot masuk sebagai {self.user}")
        self.auto_msg.start()

    @tasks.loop(seconds=10)
    async def auto_msg(self):
        ch = self.get_channel(CHANNEL_ID)
        if ch:
            await ch.send(MESSAGE)
            print(f"[{datetime.utcnow()}] Terkirim ke #{ch.name}")

    @auto_msg.before_loop
    async def before_auto_msg(self):
        await self.wait_until_ready()

client = MyClient()
client.run(TOKEN)