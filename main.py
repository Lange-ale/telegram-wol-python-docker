from time import sleep
from telepot import Bot
from wakeonlan import send_magic_packet
from config import *

HELP_MESSAGE = """type turnon <pc name> to turn on a pc, \ntype list to see the list of pc"""
                  
def manage(msg):
    global run
    text = msg['text'] . strip() . split(" ")
    command = text[0] . lower()
    if command == "help":
        bot.sendMessage(user_id, HELP_MESSAGE)
    elif command == "list":
        bot.sendMessage(user_id, list(hosts.keys()))
    elif command == "turnon":
        pc = text[1]
        if pc in hosts:
            send_magic_packet(hosts[pc])
            bot.sendMessage(user_id, "Turned on " + pc)
        else:
            bot.sendMessage(user_id, "Invalid pc name")
    else:
        bot.sendMessage(user_id, "Invalid command")
        
bot = Bot(addressBot)
bot.message_loop(manage)
bot.sendMessage(user_id, "Hi, type help to see the commands")

while True:
    sleep(600)

