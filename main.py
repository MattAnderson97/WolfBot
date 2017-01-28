import discord
import settings
import commands

client = discord.Client()


@client.async_event
def on_ready():
    print("Bot ready");


@client.event
async def on_message(message):
    msg = message.content.lower()
    print(msg)
    for command_symbol in settings.COMMAND_SYMBOLS:
        for command in settings.COMMANDS:
            if msg.startswith(command_symbol + command):
                args = msg.replace(command_symbol + command, "").strip()

                out = {
                    'help': lambda f: commands.help(),
                    '❓': lambda f: commands.help(),
                    'hi': lambda f: commands.hi(),
                    'hello': lambda f: commands.hi(),
                    'roll': lambda f: commands.roll(args.split(" ")),
                    '🔢': lambda f: commands.roll(args.split(" ")),
                    '🎲': lambda f: commands.roll(args.split(" ")),
                    'bark': lambda f: commands.bark(),
                    '🔊': lambda f: commands.bark()
                }[command]

                await client.send_message(message.channel, out(args))
                return


if __name__ == "__main__":
    client.run(settings.TOKEN)
