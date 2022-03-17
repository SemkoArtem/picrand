import telebot
import json
import time
import parse_reactor
import picsrandeomly
import random

while True: 

    file = open('./config_pics.json')
    config = json.load(file)

    bot = telebot.TeleBot(config['token_tg'])
    chanel_name = config['chanel_name']
    rand_digit = random.randint(1,100)
    url_pics = []
    url_pics.append(parse_reactor.scan_content())
    url_pics.append(picsrandeomly.start())

    url = url_pics[random.randint(0,len(url_pics)-1)]
    if url != None:
        print('sent this link to group  TG: ',url)
        bot.send_photo(chanel_name, photo=url)
        time.sleep(config['udate_time']) 
    else:
        print('Restart')
  
bot.polling()