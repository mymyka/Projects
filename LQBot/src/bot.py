import cfg
import lib
import qrcode
import telebot

bot = telebot.TeleBot(cfg.TOKEN)

Data = {
    "12345": {
        "active": {
            "total": 100,
            "ready": 20,
            "clientsList": [1233, 7586]
        },
        "static": {
            "Message": "Hello, Welcome!",
            "max": 700,
            "timeLimits": {
                "min": 10,
                "max": 30
            }
        }
    }
}

Clients = {
    "8378": {
        "active": {
            "status": 1,
            "queue": "12345",
            "number": 1
        },
        "static": {
            "name": "Mykyta",
            "Surname": "Kasianenko",
            "trust": 100,
            "pleaseList": ["12345", "876543"]
        }
    }
}


@bot.message_handler(commands=["Start"])
def start(message):
    bot.send_message(message.chat.id, cfg.Start_Message)

    msg = bot.send_message(message.chat.id, "Enter text")
    bot.register_next_step_handler(msg, process_fullname_step)


def process_fullname_step(message):
    print(message.text)


@bot.message_handler(commands=["Help me"])
def helpme(message):
    bot.send_message(message.chat.id, cfg.Help_Message)


@bot.message_handler(commands=["Status-mymy"])
def status(message):
    bot.send_message(message.chat.id,
                     "Кількість активних черг: {}\nКількість користувачів: {}\n".format(len(Data), len(Clients)))


if __name__ == '__main__':
    bot.infinity_polling()
