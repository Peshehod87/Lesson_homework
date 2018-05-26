from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.message import Message
import ephem as ep
import ephem as ep
from datetime import datetime as dt

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot, update):
	text = 'Отвали, я занят...'
	print(text)
	update.message.reply_text(text)
	#print('Вызван /start')
	#print(update)

def talk_to_me(bot, update):
	user_text = update.message.text 
	print(user_text)
	update.message.reply_text(user_text)

def planet1(bot, update):
	text = 'Введите название планеты '
	print(text)
	update.message.reply_text(text)
	#bot.send_message(text)
	text = message.text
	planet_choose = update.message.text
	print ('Бля,...', planet_choose)
	#planet_choose = update.message.text
	dt1 = dt.today()
	#planet_choose = input('Выберите планету: ')
	if planet_choose.lower() == 'mercury':
		planet = ep.constellation(ep.Mercury(dt1))
	elif planet_choose.lower() =='venus':
		planet =ep.constellation(ep.Venus(dt1))
	elif planet_choose.lower() =='earth':
		planet = ep.constellation(ep.Earth(dt1))
	elif planet_choose.lower() =='mars':
		planet =ep.constellation(ep.Mars(dt1))
			#print(planet)
	elif planet_choose.lower() =='jupiter':
		planet =ep.constellation(ep.Jupiter(dt1))
	elif planet_choose.lower() =='saturn':
		planet =ep.constellation(ep.Saturn(dt1))
	elif planet_choose.lower() =='uranus':
		planet = ep.constellation(ep.Uranus(dt1))
	elif planet_choose.lower() =='neptune':
		planet = ep.constellation(ep.Neptune(dt1))
	elif planet_choose.lower() =='pluto':
		planet = ep.constellation(ep.Pluto(dt1))
	else:
		print (planet_choose)
		planet = 'Нет таких планет'
	print(planet)
	update.message.reply_text(planet)


def main():
	mybot = Updater('526910022:AAFE5W0butYoB7PqVwg-y1527_E-UfOeAu8', request_kwargs=PROXY)
	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(CommandHandler("planet", planet1))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))
	#dp.add_handler(CommandHandler("planet", planet))
	mybot.start_polling()
	mybot.idle()

main()
