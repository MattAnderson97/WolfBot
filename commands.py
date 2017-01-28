import random
import settings


def hi():
    return "Hello there!"


def roll(args):
    if len(args) < 2:
        return "**Not enough arguments!** usage: " + settings.COMMAND_USAGE["roll"]

    try:
        rolls = int(args[0])
        sides = int(args[1])
    except ValueError:
        return "**Invalid arguments:** must be integers. usage: " + settings.COMMAND_USAGE["roll"]

    if rolls < 1:
        return "**amount of rolls too small! must be at least 1 roll."
    if sides < 3:
        return "**amount of sides too small! must be at least 3 sides."

    msg = ""

    for count in range(rolls):
        msg += "roll {0}: ".format((count + 1)) + str(random.randint(1, sides)) + "\n"

    return msg


def bark():
    noise = ["WOOF", "BORF", "ARF ARF", "MIAOW", "MEW", "MOO", "OINK", "BAA", "NEIGH", "HISS"]
    return ":loud_sound: **" + random.choice(noise) + "**"


def help():
    keys = settings.COMMAND_USAGE.keys()
    msg = ""

    for key in keys:
        msg += settings.COMMAND_USAGE[key] + "\n"
    return msg
