import telepot
import time
import pyperclip
from pynput.keyboard import Key, Controller
keyboard = Controller()

from telepot.loop import MessageLoop

key = # your telegram key here

bot = telepot.Bot(key)


text = None
old = None
while 1:

    response = bot.getUpdates()
    try:
        text = response[2]['channel_post']['text']
    except:
        pass
    if(text != old):
        print(text)
        pyperclip.copy(text)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
        keyboard.press(Key.enter)
        old = text
    time.sleep(10)

    