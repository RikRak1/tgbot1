import telebot
import random
import requests 
from bs4 import BeautifulSoup
import openpyxl as opx

token = '5707150924:AAGNMAdh6Zgv-hlX49bGYWnRJRePTFDauZM'
bot =telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def  send_hello(mes):
    wel ='Привет я бот, который поможет тебе подготовиться к ОГЭ'
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width= 2, resize_keyboard= True, one_time_keyboard= False)
    button1 = telebot.types.KeyboardButton('Математика')
    button2 = telebot.types.KeyboardButton('Физика')
    button3 = telebot.types.KeyboardButton('Информатика')
    button4 = telebot.types.KeyboardButton('Химия')
    button5 = telebot.types.KeyboardButton('Русский язык(писменный)')
    button6 = telebot.types.KeyboardButton('Русский язык(устный)')
    button7 = telebot.types.KeyboardButton('Билогия')
    button8 = telebot.types.KeyboardButton('Английский язык')
    button9 = telebot.types.KeyboardButton('География')
    button10 = telebot.types.KeyboardButton('Обществознание')
    button11 = telebot.types.KeyboardButton('Литература')
    button12 = telebot.types.KeyboardButton('История')
    keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12)
    bot.send_message(mes.chat.id, wel, reply_markup= keyboard)


@bot.message_handler(commands=['math'])
def send_math(mes):
    ma = 'Для математике тебе поможет сайты: '
    bot.send_message(mes.chat.id,  ma )
    # h = open(r'm.txt', encoding='utf-8')
    # j= h.read()
    # h1 = open('silka_math.txt')
    # j1= h1.readlines()
    # jd0 = j1[0]
    # jd1 = j1[1]
    # jd2 = j1[2]
    # jd3 = j1[3]
    # markup = telebot.types.InlineKeyboardMarkup()
    # button1 = telebot.types.InlineKeyboardButton("1", url=jd0)
    # button2 = telebot.types.InlineKeyboardButton("2", url=jd1)
    # button3 = telebot.types.InlineKeyboardButton("3", url=jd2)
    # button4 = telebot.types.InlineKeyboardButton("4", url=jd3)
    # markup.add(button1, button2, button3, button4)
    # bot.send_message(mes.chat.id,  j, reply_markup= markup)
    
    # a = 'Для решения пробников http://alexlarin.net/'
    # bot.send_message(mes.chat.id,  a )
    # r = 'Для решения каждого задания по отдельности https://math-oge.sdamgia.ru/'
    # bot.send_message(mes.chat.id,  r )
    # n = 'Для решения пробников https://neznaika.info/oge/math_oge/'
    # bot.send_message(mes.chat.id,  n)
    # s = 'Для повторения теории и разбора задач https://spadilo.ru/oge-po-matematike/'
    # bot.send_message(mes.chat.id,  s)

    a =[]
    book = opx.open('math.xlsx', read_only=True)
    book.active = 0
    sheet = book.active
    for i in range(1, 5):
        a.append(sheet[f'A{i}'].value)
    
    b1 = sheet['B1'].value
    b2 = sheet['B2'].value
    b3 = sheet['B3'].value
    b4 = sheet['B4'].value
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("1", url=b1)
    button2 = telebot.types.InlineKeyboardButton("2", url=b2)
    button3 = telebot.types.InlineKeyboardButton("3", url=b3)
    button4 = telebot.types.InlineKeyboardButton("4", url=b4)
    markup.add(button1, button2, button3, button4)
    bot.send_message(mes.chat.id,  '\n'.join(a) , reply_markup= markup)




@bot.message_handler(commands=['phisic'])
def send_phisic(mes):
    ma = 'Для физике тебе помогут такие сайты как:'
    bot.send_message(mes.chat.id,  ma )
    a =[]
    book = opx.open('math.xlsx', read_only=True)
    book.active = 1
    sheet = book.active
    for i in range(1, 5):
        a.append(sheet[f'A{i}'].value)
    
    b1 = sheet['B1'].value
    b2 = sheet['B2'].value
    b3 = sheet['B3'].value
    b4 = sheet['B4'].value
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("1", url=b1)
    button2 = telebot.types.InlineKeyboardButton("2", url=b2)
    button3 = telebot.types.InlineKeyboardButton("3", url=b3)
    button4 = telebot.types.InlineKeyboardButton("4", url=b4)
    markup.add(button1, button2, button3, button4)
    bot.send_message(mes.chat.id,  '\n'.join(a) , reply_markup= markup)

@bot.message_handler(commands=['Informatika'])
def send_info(mes):
    ma = 'Для информатике тебе помогут такие сайты как:'
    bot.send_message(mes.chat.id,  ma )
    a =[]
    book = opx.open('math.xlsx', read_only=True)
    book.active = 2
    sheet = book.active
    for i in range(1, 5):
        a.append(sheet[f'A{i}'].value)
    
    b1 = sheet['B1'].value
    b2 = sheet['B2'].value
    b3 = sheet['B3'].value
    b4 = sheet['B4'].value
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("1", url=b1)
    button2 = telebot.types.InlineKeyboardButton("2", url=b2)
    button3 = telebot.types.InlineKeyboardButton("3", url=b3)
    button4 = telebot.types.InlineKeyboardButton("4", url=b4)
    markup.add(button1, button2, button3, button4)
    bot.send_message(mes.chat.id,  '\n'.join(a) , reply_markup= markup)
    
@bot.message_handler(commands=['Chemistry'])
def send_сhemistry(mes):
    ma = 'Для химии тебе помогут такие сайты как:'
    bot.send_message(mes.chat.id,  ma )
    a =[]
    book = opx.open('math.xlsx', read_only=True)
    book.active = 3
    sheet = book.active
    for i in range(1, 5):
        a.append(sheet[f'A{i}'].value)
    
    b1 = sheet['B1'].value
    b2 = sheet['B2'].value
    b3 = sheet['B3'].value
    b4 = sheet['B4'].value
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("1", url=b1)
    button2 = telebot.types.InlineKeyboardButton("2", url=b2)
    button3 = telebot.types.InlineKeyboardButton("3", url=b3)
    button4 = telebot.types.InlineKeyboardButton("4", url=b4)
    markup.add(button1, button2, button3, button4)
    bot.send_message(mes.chat.id,  '\n'.join(a) , reply_markup= markup)

@bot.message_handler(commands=['Russian(w)'])
def send_rus(mes):
    ma = 'Для русского тебе помогут такие сайты как:'
    bot.send_message(mes.chat.id,  ma )
    a =[]
    book = opx.open('math.xlsx', read_only=True)
    book.active = 4
    sheet = book.active
    for i in range(1, 5):
        a.append(sheet[f'A{i}'].value)
    
    b1 = sheet['B1'].value
    b2 = sheet['B2'].value
    b3 = sheet['B3'].value
    b4 = sheet['B4'].value
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("1", url=b1)
    button2 = telebot.types.InlineKeyboardButton("2", url=b2)
    button3 = telebot.types.InlineKeyboardButton("3", url=b3)
    button4 = telebot.types.InlineKeyboardButton("4", url=b4)
    markup.add(button1, button2, button3, button4)
    bot.send_message(mes.chat.id,  '\n'.join(a) , reply_markup= markup)


@bot.message_handler(commands=['Russian(r)'])
def send_rus_r(mes):
    ma = 'Для русского тебе помогут такие сайты как:'
    bot.send_message(mes.chat.id,  ma )
    a =[]
    book = opx.open('math.xlsx', read_only=True)
    book.active = 5
    sheet = book.active
    for i in range(1, 4):
        a.append(sheet[f'A{i}'].value)
    
    b1 = sheet['B1'].value
    b2 = sheet['B2'].value
    b3 = sheet['B3'].value
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("1", url=b1)
    button2 = telebot.types.InlineKeyboardButton("2", url=b2)
    button3 = telebot.types.InlineKeyboardButton("3", url=b3)
    markup.add(button1, button2, button3)
    bot.send_message(mes.chat.id,  '\n'.join(a) , reply_markup= markup)

@bot.message_handler(commands=['Biology'])
def send_bio(mes):
    ma = 'Для биологии тебе помогут такие сайты как:'
    bot.send_message(mes.chat.id,  ma )
    a =[]
    book = opx.open('math.xlsx', read_only=True)
    book.active = 6
    sheet = book.active
    for i in range(1, 4):
        a.append(sheet[f'A{i}'].value)
    
    b1 = sheet['B1'].value
    b2 = sheet['B2'].value
    b3 = sheet['B3'].value
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("1", url=b1)
    button2 = telebot.types.InlineKeyboardButton("2", url=b2)
    button3 = telebot.types.InlineKeyboardButton("3", url=b3)
    markup.add(button1, button2, button3)
    bot.send_message(mes.chat.id,  '\n'.join(a) , reply_markup= markup)


@bot.message_handler(commands=['English'])
def send_eng(mes):
    ma = 'Для английского тебе помогут такие сайты как:'
    bot.send_message(mes.chat.id,  ma )
    a =[]
    book = opx.open('math.xlsx', read_only=True)
    book.active = 7
    sheet = book.active
    for i in range(1, 4):
        a.append(sheet[f'A{i}'].value)
    
    b1 = sheet['B1'].value
    b2 = sheet['B2'].value
    b3 = sheet['B3'].value
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("1", url=b1)
    button2 = telebot.types.InlineKeyboardButton("2", url=b2)
    button3 = telebot.types.InlineKeyboardButton("3", url=b3)
    markup.add(button1, button2, button3)
    bot.send_message(mes.chat.id,  '\n'.join(a) , reply_markup= markup)

@bot.message_handler(commands=['Geografy'])
def send_geo(mes):
    ma = 'Для географии тебе помогут такие сайты как:'
    bot.send_message(mes.chat.id,  ma )
    a =[]
    book = opx.open('math.xlsx', read_only=True)
    book.active = 8
    sheet = book.active
    for i in range(1, 4):
        a.append(sheet[f'A{i}'].value)
    
    b1 = sheet['B1'].value
    b2 = sheet['B2'].value
    b3 = sheet['B3'].value
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("1", url=b1)
    button2 = telebot.types.InlineKeyboardButton("2", url=b2)
    button3 = telebot.types.InlineKeyboardButton("3", url=b3)
    markup.add(button1, button2, button3)
    bot.send_message(mes.chat.id,  '\n'.join(a) , reply_markup= markup)

@bot.message_handler(commands=['Obshest'])
def send_obsh(mes):
    ma = 'Для обществознания тебе помогут такие сайты как:'
    bot.send_message(mes.chat.id,  ma )
    a =[]
    book = opx.open('math.xlsx', read_only=True)
    book.active = 9
    sheet = book.active
    for i in range(1, 4):
        a.append(sheet[f'A{i}'].value)
    
    b1 = sheet['B1'].value
    b2 = sheet['B2'].value
    b3 = sheet['B3'].value
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("1", url=b1)
    button2 = telebot.types.InlineKeyboardButton("2", url=b2)
    button3 = telebot.types.InlineKeyboardButton("3", url=b3)
    markup.add(button1, button2, button3)
    bot.send_message(mes.chat.id,  '\n'.join(a) , reply_markup= markup)

@bot.message_handler(commands=['Litruter'])
def send_lit(mes):
    ma = 'Для литературы тебе помогут такие сайты как:'
    bot.send_message(mes.chat.id,  ma )
    a =[]
    book = opx.open('math.xlsx', read_only=True)
    book.active = 10
    sheet = book.active
    for i in range(1, 4):
        a.append(sheet[f'A{i}'].value)
    
    b1 = sheet['B1'].value
    b2 = sheet['B2'].value
    b3 = sheet['B3'].value
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("1", url=b1)
    button2 = telebot.types.InlineKeyboardButton("2", url=b2)
    button3 = telebot.types.InlineKeyboardButton("3", url=b3)
    markup.add(button1, button2, button3)
    bot.send_message(mes.chat.id,  '\n'.join(a) , reply_markup= markup)

@bot.message_handler(commands=['History'])
def send_his(mes):
    ma = 'Для истории тебе помогут такие сайты как:'
    bot.send_message(mes.chat.id,  ma )
    a =[]
    book = opx.open('math.xlsx', read_only=True)
    book.active = 11
    sheet = book.active
    for i in range(1, 4):
        a.append(sheet[f'A{i}'].value)
    
    b1 = sheet['B1'].value
    b2 = sheet['B2'].value
    b3 = sheet['B3'].value
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("1", url=b1)
    button2 = telebot.types.InlineKeyboardButton("2", url=b2)
    button3 = telebot.types.InlineKeyboardButton("3", url=b3)
    markup.add(button1, button2, button3)
    bot.send_message(mes.chat.id,  '\n'.join(a) , reply_markup= markup)

@bot.message_handler(content_types=['text'])
def ans(mes):
    if mes.text.strip() == 'Математика':
        send_math(mes)
    elif  mes.text.strip() == 'Физика':
        send_phisic(mes)
    elif mes.text.strip() == 'Информатика':
        send_info(mes)
    elif mes.text.strip() == 'Химия':
        send_сhemistry(mes)
    elif mes.text.strip() == 'Русский язык(писменный)':
        send_rus(mes)
    elif mes.text.strip() == 'Русский язык(устный)':
        send_rus_r(mes)
    elif mes.text.strip() == 'Билогия':
        send_bio(mes)
    elif mes.text.strip() == 'Английский язык':
        send_eng(mes)
    elif mes.text.strip() == 'География':
        send_geo(mes)
    elif mes.text.strip() == 'Обществознание':
        send_obsh(mes)
    elif mes.text.strip() == 'Литература':
        send_lit(mes)
    elif mes.text.strip() == 'История':
        send_his(mes)
bot.polling()

