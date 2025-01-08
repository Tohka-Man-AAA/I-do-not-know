import telebot,time
from bot_logic import gen_pass,coin
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    time.sleep(1)
    bot.reply_to(message, f"Привет! Я бот {bot.get_me().first_name}!")
    time.sleep(2)
    bot.reply_to(message, "На данный момент у меня есть 6 команд:'hello', 'bye', 'password', 'coin', 'heh', 'ping'. Испробуй их!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    time.sleep(1)
    bot.reply_to(message, "Привет! Как дела?")


@bot.message_handler(commands=['bye'])
def send_bye(message):
    time.sleep(1)
    bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(commands=['password'])
def send_pass(message):
    time.sleep(1)
    password =gen_pass(10)
    bot.reply_to(message, password)


@bot.message_handler(commands=['coin'])
def send_pass(message):
    time.sleep(1)
    attempt = coin()
    bot.reply_to(message, f"Монетка выпала так:{attempt}")


@bot.message_handler(commands=['heh'])
def send_heh(message):
    time.sleep(1)
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)


@bot.message_handler(commands=["ping"])
def on_ping(message):
    time.sleep(1)
    bot.reply_to(message, "Я все еще работаю!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    time.sleep(1)
    bot.reply_to(message, message.text)



bot.polling()
