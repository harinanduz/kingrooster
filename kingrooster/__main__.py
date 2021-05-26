from sys import argv, exit
from kingrooster import tbot
from kingrooster import TOKEN

# IDK WHY IT'S SO IMPORTANT, JUST DON'T REMOVE THIS
import kingrooster.events

try:
    tbot.start(bot_token=TOKEN)
except Exception:
    print("Network Error !")
    exit(1)

if len(argv) not in (1, 3, 4):
    tbot.disconnect()
else:
    tbot.run_until_disconnected()
