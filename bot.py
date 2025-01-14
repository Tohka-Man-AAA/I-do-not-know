import telebot,time,os,random,requests
from bot_logic import gen_pass,coin
bot = telebot.TeleBot("TOKEN")


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


#def get_fox_image_url():
    #url = 'https://randomfox.ca/floof'
    #res = requests.get(url)
    #data = res.json()
    #return data['url']

def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

#@bot.message_handler(commands=['fox'])
#def fox(message):
    #time.sleep(1)
    #image_url = get_fox_image_url()
    #bot.reply_to(message, image_url)


@bot.message_handler(commands=['duck'])
def duck(message):
    time.sleep(1)
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)


@bot.message_handler(commands=['dog'])
def dog(message):
    time.sleep(1)
    image_url = get_dog_image_url()
    bot.reply_to(message, image_url)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    time.sleep(1)
    bot.reply_to(message, f"Привет! Я бот {bot.get_me().first_name}!")
    time.sleep(1)
    bot.reply_to(message, "На данный момент у меня есть 10 команд\nВведи /help чтобы узнать о каждой!")


@bot.message_handler(commands=['help'])
def send_help(message):
    time.sleep(2)
    bot.reply_to(message, "/hello - бот поприветствует тебя.\n/bye - бот попрощается с тобой.\n/coin - подбросит монетку.\n/password - сгенерирует случайный пароль.\n/duck - отправляет рандомное милое изображение уток.\n/meme - скинет рандомный мем на любую тематику.\n/ping - проверяет работу бота, если бот не отвечает: он выключен.\n/heh - преумножает любое ваше слово или фразу на то количество,которое вы введете.\nПравильная запись:\n/heh слово количество раз\n/dog - бот отправит тебе милое изображение собачек\n/fox - отправляет рандомную картинку с лисами")


@bot.message_handler(commands=['hello'])
def send_hello(message):
    time.sleep(1)
    bot.reply_to(message, "Привет! Как дела?")


@bot.message_handler(commands=['bye'])
def send_bye(message):
    time.sleep(1)
    bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(commands=['meme'])
def send_meme(message):
    time.sleep(1)
    a = os.listdir('images')
    img_name = random.choice(a)
    with open(f'images/{img_name}','rb') as f:
        bot.send_photo(message.chat.id, f)


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
    count_heh = int(message.text.split()[2]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, message.text.split()[1] * count_heh)


@bot.message_handler(commands=["ping"])
def on_ping(message):
    time.sleep(1)
    bot.reply_to(message, "Я все еще работаю!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    time.sleep(1)
    bot.reply_to(message, message.text)



bot.polling()
