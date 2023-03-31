#Parser bot for ICQ
import requests
from bs4 import BeautifulSoup as BS
from bot.bot import Bot
from bot.handler import MessageHandler

TOKEN = "" #your token here

bot = Bot(token=TOKEN)
cassd = "Shopping_Live"
te = 20

b = []
q = []
for i in range(11):
	r = requests.get("http://www.smojem.ru/page/" + str(te) + "/")
	html = BS(r.content, 'html.parser')
	for el in html.select('.ss-t-03'):
		q.append(el.text)
		b.append(el.img)
	te = te+1
for i in range(100):
	c = str(b[i])
	qq = str(q[i])
	d = c.find('jpg')+3
	c = c[:d]
	d = c.find('src') + 5
	c2 = c[:d]
	c = 'http://www.smojem.ru/' + c.replace(c2,'')
	print(str(i))
	bot.send_text(chat_id='', text=(c+" "+qq))

bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.start_polling()
bot.idle()
