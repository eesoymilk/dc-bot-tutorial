import os
from dotenv import load_dotenv
from discord import Intents, Message
from discord.ext.commands import Bot, Context

intents = Intents.default()
intents.message_content = True
bot = Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message: Message):
    if message.author == bot.user:
        return

    print(f'{message.author} says {message.content}')


@bot.command
async def hello(ctx: Context):
    await ctx.send("Hello, I'm your Discord bot!")


def main():
    load_dotenv()
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()
