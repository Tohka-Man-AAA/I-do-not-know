import telebot,time
bot = telebot.TeleBot('TELEBOT')


@bot.message_handler(commands=['start'])
def send_start(message):
    time.sleep(1)
    f = open('Text.txt', 'r' , encoding='utf-8')
    f_a = f.read()
    bot.reply_to(message,f_a)
    f.close()
    time.sleep(1)
    m = open('text2.txt', 'r', encoding='utf-8')
    m_a = m.read()
    bot.reply_to(message, m_a)
    m.close()

@bot.message_handler(commands=['life_hacks'])
def send_help(message):
    time.sleep(1)
    n = open('lifehuck.txt', 'r', encoding='utf-8')
    n_a = n.read()
    bot.reply_to(message, n_a)
    n.close()


@bot.message_handler(commands=['help'])
def send_help(message):
    time.sleep(1)
    z = open('help.txt', 'r', encoding='utf-8')
    z_a = z.read()
    bot.reply_to(message, z_a)
    z.close()

@bot.message_handler(commands=['plastic'])
def send_plastic(message):
    time.sleep(1)
    h = open('plastic.txt','r',encoding='utf-8')
    h_a = h.read()
    bot.reply_to(message,h_a)
    h.close()


@bot.message_handler(commands=['paper'])
def send_paper(message):
    time.sleep(1)
    b = open('paper.txt','r',encoding='utf-8')
    b_a = b.read()
    bot.reply_to(message,b_a)
    b.close()


@bot.message_handler(commands=['glass'])
def send_glass(message):
    time.sleep(1)
    g = open('glass.txt','r',encoding='utf-8')
    g_a = g.read()
    bot.reply_to(message,g_a)
    g.close()


bot.polling()
