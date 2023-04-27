import os
from typing import Optional
from dotenv import load_dotenv
from discord import (
    app_commands,
    Intents,
    Message,
    Interaction,
    Member)
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
    await ctx.send(f'Hi, {ctx.author.mention}')


@bot.tree.command()
async def hello(intx: Interaction):
    await intx.response.send_message(f'Hi, {intx.user.mention}')


@bot.tree.command()
@app_commands.describe(
    num1='The first value you want to add something to',
    num2='The second value you want to add to the first value',
)
async def add(intx: Interaction, num1: float, num2: float):
    """Adds two numbers together."""
    await intx.response.send_message(f'{num1} + {num2} = {num1 + num2}')


@bot.tree.command()
@app_commands.rename(msg='text')
@app_commands.describe(msg='Text to send in the current channel')
async def echo(intx: Interaction, msg: str):
    """Sends the text into the current channel."""
    await intx.response.send_message(msg)


@bot.tree.command()
@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
async def avatar(intx: Interaction, member: Optional[Member] = None):
    # If no member is explicitly provided then we use the command user here
    member = member or intx.user

    await intx.response.send_message(member.display_avatar)


# This context menu command only works on members
@bot.tree.context_menu(name='Get Avatar')
async def avatar_ctx_menu(intx: Interaction, member: Member):
    await intx.response.send_message(member.display_avatar)


def main():
    load_dotenv()
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()
