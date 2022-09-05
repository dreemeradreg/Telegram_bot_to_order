#! /usr/bin/env python
# -*- coding: utf-8 -*-

# *****************************
# pip install pyTelegramBotAPI
# pip install pycrypto
# pip install pycryptodome
# *****************************
import sys
import os
# import time

import telebot
from telebot import types

import binascii
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
# key bot
bot = telebot.TeleBot('1270839634:AAESrDOO1I8zHmgd3uMuD3vPbEqtYdrth60') # мой 
key_aes_128 = 'fe5ghe56j7kkt78kl8g787gf5j54g4ek'
BLOCK_SIZE = 32


oll_prise = (
			"что-то",
			"из товара",
			"тут",
			"будет"
			)

words_dot_chat = {
			"привет":"Приветик!",
			"пока":"До завтра",
			"как дела?":"Вроде...\n. _.\nвроде норм )",
			"что ты умеешь?":"Я могу показать каталог товаров, которые у меня есть",
			"спасибо":"всегда пожалуйса",
			"кто тебя создал?":"Меня создал администратор! ) ",
			"порно есть?":"нету ( \nтолько эротика)",
			"что делаешь?":"Работаю :(",
			"как ты работаешь?":"Магия :D",
			"что делать?":"Наслождайся каждым моментом, своей короткой жизни",
			"что мне делать?":"Подумай -> Расслабся -> Забей -> и придёт ответ :D",
			"эротика":"о_о если админ увидит меня будут ругать\n...\nПрости ;(",
			"а что у тебя есть?":"В душе ничего, я просто пустая кукла в лапах безумца",
			"ты кто?":"Бот!",
			"что ты умеешь?":"Много чего \nпиши </commands> \nи узнаешь что я умею",
			"а что ты умеешь?":"Много чего \nпиши </commands> \nи узнаешь что я умею",
			"доброе утро":"утречка!",
			"утро":"Доброе?",
			"сладких снов":"И тебе мой сладенький пользователь :3",
			"огонь":"ДАААА ;)",
			"норм":")",
			"konami":":) \nнеа \nнету такого",
			"пидор":"Сам такой",
			"ты пидор":"Нет ты!",
			"сосни хуйца":"Если бы у меня рот, то от твоей висюльки ничего бы не осталось",
			"соси хуй":"У меня не получиться, но ты можешь сломать себе рёбра и отлизать",
			"хуй":"в рот себе засунь",
			"пошел нахуй":"только если с тобой",
			"иди нахуй":"а ты присоединишься?",
			# "как выростить хороший стафф?":"https://telegra.ph/Groupediya-Dzagi-05-19",
			"говно":"что именно?",
			"хуйня":"Не ругайся пожалуйста )",
			"чё есть?":"Много чего кнопочки в помощь!",
			"как получить админку?":"У меня? Такое только через админа",
			"у вас есть магазин?":"Да есть. Напиши <время работы>",
			"время работы":"Наш магазин работает с 10 до 20\nДоставкой занимаемся в это же время",
			"порно":"Такого нету",
			"нет ты":"нет ты!",
			"сам такой!":"Сам такой!",
			# "контакты":"Номер магазина - +7(915)368-19-24\nНаша группа в vk - https://vk.com/vaporstoreclub\nНомер курьерской службы доставки- +7(977)-315-93-75 -(Сергей)-(whatsapp,tg,sms)",
			# "как работать с ботом":"Для удобства обращения к боту есть кнопочки!\nСледует выбрать категорию товара, а затем под категорию. После выбора товара под каждым товаром будет кнопка добавить в корзину.\nТакже есть кнопочка корзина, и для отправки заказа следует нажать отправить заказ. В случае если случайно был добавлен товар то в корзине есть кнопочка очищения. Если необходимо заказать n кол-во товара одного типа то можно пользоваться одной кнопочкой которая будет отображаться выше. После отправки заказа следует связаться либо с магазином либо с курьерской службой доставки для уточнения контактов можно воспользоваться командой <Контакты>",
			# "как работать с ботом?":"Для удобства обращения к боту есть кнопочки!\nСледует выбрать категорию товара, а затем под категорию. После выбора товара под каждым товаром будет кнопка добавить в корзину.\nТакже есть кнопочка корзина, и для отправки заказа следует нажать отправить заказ. В случае если случайно был добавлен товар то в корзине есть кнопочка очищения. Если необходимо заказать n кол-во товара одного типа то можно пользоваться одной кнопочкой которая будет отображаться выше. После отправки заказа следует связаться либо с магазином либо с курьерской службой доставки для уточнения контактов можно воспользоваться командой <Контакты>"
			"огонь":"ДАААА ;)"
			}

# mi func in bot use
# buttons on relese
def get_mi_buttons(mass_in_prise):
	markup_buttons_on_loop = types.InlineKeyboardMarkup(row_width=1)
	for name_in_prase in mass_in_prise:
		oll_button = types.InlineKeyboardButton(name_in_prase, callback_data=name_in_prase)
		markup_buttons_on_loop.add(oll_button)

	return markup_buttons_on_loop
# decrypt on url-refer
def aes128_decrypt(block, key):
	msg = binascii.unhexlify(block.encode('utf8'))
	decipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
	msg_dec = decipher.decrypt(msg)
	return unpad(msg_dec, BLOCK_SIZE).decode('utf8')
# encrypt on url-refer
def aes128_encrypt(block, key):
	global BLOCK_SIZE
	cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
	msg = cipher.encrypt(pad(block.encode('utf8'), BLOCK_SIZE))
	return binascii.hexlify(msg).decode('utf8')


def markup_buttons_on_admins():
	markup_buttons_on_admins = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_url_site = types.KeyboardButton("Наш сайт")
	button_contacts = types.KeyboardButton("Консультант")
	button_useful_overview = types.KeyboardButton("Полезный обзор")
	button_commands = types.KeyboardButton("/adm_commands")
	button_distributs = types.KeyboardButton("Дистребъютеры")
	button = types.KeyboardButton("...")
	markup_buttons_on_admins.add(button_url_site, button_contacts, button_useful_overview,button_commands,button_distributs, button)
	return markup_buttons_on_admins


def markup_buttons_on_destrebuters():
	markup_buttons_on_admins = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_url_site = types.KeyboardButton("Наш сайт")
	button_contacts = types.KeyboardButton("Консультант")
	button_useful_overview = types.KeyboardButton("Полезный обзор")
	button_commands = types.KeyboardButton("/url_refer")
	button_distributs = types.KeyboardButton("Личный кабинет")
	markup_buttons_on_admins.add(button_url_site, button_contacts, button_useful_overview,button_commands,button_distributs)
	return markup_buttons_on_admins

def markup_buttons_on_consultant():
	markup_buttons_on_admins = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_url_site = types.KeyboardButton("Наш сайт")
	button_contacts = types.KeyboardButton("Консультант")
	button_useful_overview = types.KeyboardButton("Полезный обзор")
	button_commands = types.KeyboardButton("/cons_commands")
	button_distributs = types.KeyboardButton("/list_chat")
	markup_buttons_on_admins.add(button_url_site, button_contacts, button_useful_overview,button_commands,button_distributs)
	return markup_buttons_on_admins

def get_me_buttons_on_add_user(user_nic, user_id_add, coll_back_data_add):
	markup_buttons_on_admins = types.InlineKeyboardMarkup(row_width=1)
	button_add_user = types.InlineKeyboardButton("[Добавить] :"+str(user_nic), callback_data=coll_back_data_add)
	button_pass_user = types.InlineKeyboardButton("[Игнорировать]:"+str(user_nic), callback_data=" [pass] :")
	button_dell_user = types.InlineKeyboardButton("[Заблокировать]:"+str(user_nic), callback_data=" [-] :"+str(user_nic)+"-"+str(user_id_add))
	markup_buttons_on_admins.add(button_add_user, button_pass_user,button_dell_user)
	return markup_buttons_on_admins


def get_mi_add_admins_disteb(dirrectori,id_user_on_bot):
	with open(dirrectori, 'a') as file_oll_users:
		file_oll_users.write(id_user_on_bot+"\n")
		file_oll_users.close()

def get_mi_list(dirrectori):
	with open(dirrectori, 'r') as file_oll_users:
		oll_users = file_oll_users.read().split("\n")
		return oll_users

def get_mi_ban_list():
	ban_list = get_mi_list("ban_list")
	ban_user = []
	for name_user in ban_list:
		if name_user != '':
			ban_user.append((name_user.split("-"))[1])
	return ban_user

def get_mi_list_user_admin():
	id_chat_admins = get_mi_list("admin_list_all")
	id_chat_adm = []
	for name_admin in id_chat_admins:
		if name_admin != '':
			id_chat_adm.append((name_admin.split("-"))[3])
	return id_chat_adm

@bot.message_handler(commands=['start'])
def welcome(message):
	# print(str(message.from_user.username))
	if str(message.from_user.username) == "None":
		bot.send_message(message.chat.id, 
				"Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, бот созданный для удобного оформления заказа.\nОднако, у тебя не указанн никнейм! Я не смогу начислить тебе баллы если не добавишь его себе".format(message.from_user, bot.get_me()),
				)
		bot.send_photo(message.chat.id, open('logo_user_name.jpg', 'rb'), 'Для добавления ника следует зайти в настройки аккаунта и найти графу с "Имя пользователя" как представленно на картинке')
	else:	
		global key_aes_128
		markup_buttons_on_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
		button_url_site = types.KeyboardButton("Наш сайт")
		button_contacts = types.KeyboardButton("Консультант")
		button_useful_overview = types.KeyboardButton("Полезный обзор")
		button_back = types.KeyboardButton("<- Назад")
		markup_buttons_on_start.add(button_url_site, button_contacts, button_useful_overview, button_back)

		with open("oll_users", 'r') as file_in_oll_users:
			in_oll_users = file_in_oll_users.readlines()

		if str(message.chat.id)+"\n" not in in_oll_users:
			with open("oll_users", 'a') as file_in_oll_users:
				file_in_oll_users.write(str(message.chat.id)+"\n")
				file_in_oll_users.close()

		bot.send_message(message.chat.id, 
				"Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, бот созданный для удобного оформления заказа.".format(message.from_user, bot.get_me()),
				reply_markup=markup_buttons_on_start
				)
		
		bot.send_photo(message.chat.id, open('intro_on_hint.jpg', 'rb'), 'Возможно, что у вас не отобразились кнопочки. Следует найти похожую кнопочку как на картинке')

		if message.text != '/start':
			try:
				hash_on_referal_in_coding = message.text.split(" ")
				referal_on_decoding = aes128_decrypt(hash_on_referal_in_coding[1],key_aes_128)
				mass_id_name_ferst = referal_on_decoding.split("|")
				if os.path.isfile("users/"+str(message.chat.username)) == True:
					bot.send_message(message.chat.id,"ты перешёл по ссылке от: "+mass_id_name_ferst[1]+" "+mass_id_name_ferst[2]+".Ты уже прихходил от другого пользователя, и за переход по рефераальной ссылке тебе уже не будут начисленны баллы")

				else:
					bot.send_message(message.chat.id,"тебя приглосил: "+mass_id_name_ferst[1]+" "+mass_id_name_ferst[2]+". И За переход по рефераальной ссылке тебе начисленны бонусные балы ")

					with open("users/"+str(message.chat.username), 'w') as file_user:
						file_user.write(referal_on_decoding+"\n100\n")
						file_user.close()
			except Exception as e:
				bot.send_message(message.chat.id, e)
				# bot.send_message(message.chat.id,"Реферальная ссылка от пользователя боллее не активна")

@bot.message_handler(commands=['commands'])
def get_mi_commands(message):
	bot.send_message(message.chat.id, "/start\n/commands\n/dest_commands\n/adm_commands\n")

@bot.message_handler(commands=['dest_commands'])
def get_mi_dest_commands(message):
	id_chat_admins = get_mi_list_user_admin()
	file_list_destreb = os.listdir("destrebuters/")
	file_list_consult = os.listdir("consultant/")
	dest_commands_messeg = "/start\n/commands - видит любой пользователь\n/dest_commands - для Дистребъютеров\n/url_refer\n/add_to_destreb - комманда для добавления в дистребьютеры\n/adm_commands - видна только для админам"
	
	if str(message.chat.id) in id_chat_admins:
		bot.send_message(message.chat.id, "ты же администратор! Зачем тебе эти комманды ?_?")
		bot.send_message(message.chat.id, dest_commands_messeg)
	elif str(message.chat.username) in file_list_destreb:
		bot.send_message(message.chat.id, "Зачем комманды дистребъютеров консультанту?ну ладно держи!")
		bot.send_message(message.chat.id, dest_commands_messeg)
	elif str(message.chat.username) in file_list_destreb:
		bot.send_message(message.chat.id, dest_commands_messeg)
	else:
		bot.send_message(message.chat.id, "Нехватает прав доступа!")

@bot.message_handler(commands=['adm_commands'])
def get_mi_commands_admin(message):
	id_chat_admins = get_mi_list_user_admin()
	file_list = os.listdir("destrebuters/")
	if str(message.chat.id) in id_chat_admins:
		cammands_text_user = "/start - команда для наччала работы с ботом\n/start=<referal_url> - команда для для начала работы с указанием от кого пришел. Это не посредственно ссылка которая генерируеться  командой указанной ниже\n/commands - список доступных команд всем\n/add_to_admins - запрос на добавление в админы\n/list_admins - список админов и удаление из них\n\n/add_to_consul - запрос на добавление в консультанты\n/list_consultant - список консультантов и удаление из них\n\n/add_to_destreb - запрос на добавление в дистребьютеры\n/list_destrebuters - список Дистребъютеров и удаление из них\n\n/list_chat - список кто ждёт в чате + начало общения с ожидающими\n/ban_list - список тех кто в бане + удалления из бана\n(в бан попадают те кто отправлял администраторам запросы на получения прав)\n/grep - поиск по пользователям + начисление или списание баллов\nПримечание: Следует точно указывать ник пользователя, ник пользователя будет высвечиваться в самом верху при активации пользователем чата\nпрямой слеш это спец символ для разделения комманды на саму комманду и полезную нагрузку\nПример: /grep|FreeLagGavr\n/adm_commands - команды с доступом только администратором\n/url_refer - команда для генерации рефераальной ссылки\n\nсайт - наш сайт\nконсультант - связь с консультантом\nполезный обзор - каталог товаара\n\n\n/gr_o_d - инфа по всем реферальным ссылкам /gr_o_d|<ник дистребъютера> - сколько именно людей перело и сколько из них воспользовались баллами\nЛичный кабинет - команда для вывода инфы про себя тагже доступна дистребьютерам\n/oll_users|<всем привет> - команда для массовой рассылки новости\n/dow_fot|<имя картинки>\n-тагже может заменить уже существующую\n\n/get_n_t|<категория товара>|<название товара>|<описание + цена + остальное>\n\nПример:/get_n_t|Что-то|тутимя товара|а здесь описание цена:200р\n\n------\n\nПримечание категории уже созданны! И необходимо использовать уже созданные категории, создание новых категорий возможно только через разработчика. Следует явно указывать категорию.\n\nВАЖНО! имя товара не может быть одинаковым, следует использовать уникальное имя товара!\nпример:<Лед лампа на 100w> и <лед лампа на 100w> разные имена. НО лучше использовать название\n\nДля загрузки товара с картинкой и описанием следует, загрузить картинку и добавить к ней описание с коммандой. Сама комманда и пример команды выше - в своём роде универсальная комманда\n\n"
		bot.send_message(message.chat.id, cammands_text_user)
	elif str(message.chat.username) in file_list: 
		bot.send_message(message.chat.id, "у тебя команды узнать их можно через:\n/dest_commands\nА это админские!")
	else:
		bot.send_message(message.chat.id, "Нехватает прав доступа!")

@bot.message_handler(commands=['cons_commands'])
def get_mi_commands_admin(message):
	id_chat_admins = get_mi_list_user_admin()
	file_list_consult = os.listdir("consultant/")
	cammands_text_user = "/start - команда для наччала работы с ботом\n/start=<referal_url> - команда для для начала работы с указанием от кого пришел. Это не посредственно ссылка которая генерируеться  командой указанной ниже\n/commands - список доступных команд всем\n/add_to_consul - запрос на добавление в консультанты\n/list_chat - список кто ждёт в чате + начало общения с ожидающими\n\n/cons_commands - команды для консультантов/url_refer - команда для генерации рефераальной ссылки\n\n"

	if str(message.chat.id) in id_chat_admins:
		bot.send_message(message.chat.id, "ты же администратор! Зачем тебе эти комманды ?_?")
		bot.send_message(message.chat.id, cammands_text_user)
	elif str(message.chat.username) in file_list_consult: 
		bot.send_message(message.chat.id, cammands_text_user)
	else:
		bot.send_message(message.chat.id, "Нехватает прав доступа!")

@bot.message_handler(commands=['url_refer'])
def get_mi_url_refer(message):
	global key_aes_128
	id_chat_admins = get_mi_list_user_admin()
	file_list_destreb = os.listdir("destrebuters/")
	file_list_consult = os.listdir("consultant/")

	if str(message.chat.id) in id_chat_admins or str(message.chat.username) in file_list_destreb or str(message.chat.username) in file_list_consult:
		hash_on_refer_text = str(message.chat.id)+"|"+str(message.from_user.first_name)+"|"+str(message.from_user.last_name)
		hash_on_refer = aes128_encrypt(hash_on_refer_text, key_aes_128)
		bot.send_message(message.chat.id,  "https://t.me/"+str(bot.get_me().username)+"?start="+str(hash_on_refer))
	else:
		bot.send_message(message.chat.id, "Нехватает прав доступа!")


@bot.message_handler(commands=['add_to_admins'])
def get_add_to_admins(message):
	id_chat_admins = get_mi_list_user_admin()
	ban_user =[]
	if str(message.chat.id) in id_chat_admins:
		bot.send_message(message.chat.id, "Вы уже администратор!")
	elif message.chat.username == None:
		bot.send_message(message.chat.id, "У вас не указанно имя пользователя!")
	else:
		ban_list = get_mi_ban_list()
		if str(message.chat.id) in ban_list:
			bot.send_message(message.chat.id, "Вы уже отправили запрос на получение админских прав, и администратор запретил вам отправлять подобные запросы")
		else:

			for id_chat_admin in id_chat_admins:
				if id_chat_admin != "":
					try:
						bot.send_message(int(id_chat_admin), "Пользователь :"+str(message.chat.id)+"-"+str(message.from_user.first_name)+" "+str(message.from_user.last_name)+"\nжелает получить доступ\n\n [Добавить] - добавит пользователя как администратора в систему\n [Игнорировать] - просто закроет это сообщение \n[Заблокировать] - запретит отправлять этому пользователю подобные сообщения", 
							reply_markup=get_me_buttons_on_add_user(
								str(message.chat.username), 
								str(message.chat.id), 
								" [+] :"+str(message.chat.username)+"-"+str(message.from_user.first_name)+"-"+str(message.from_user.last_name)+"-"+str(message.chat.id)
								)
							)
					except:
						bot.send_message(int(id_chat_admin), "Пользователь :"+str(message.chat.id)+"-"+str(message.from_user.first_name)+" "+str(message.from_user.last_name)+"\nжелает получить доступ\n\n [Добавить] - добавит пользователя как администратора в систему\n [Игнорировать] - просто закроет это сообщение \n[Заблокировать] - запретит отправлять этому пользователю подобные сообщения", 
							reply_markup=get_me_buttons_on_add_user(
								str(message.chat.username), 
								str(message.chat.id), 
								" [+] :"+str(message.chat.username)+"-rus-rus-"+str(message.chat.id)
								)
							)
			bot.send_message(message.chat.id, "Вы отправили запрос на получение админских прав")

@bot.message_handler(commands=['add_to_destreb'])
def get_add_to_destreb(message):
	id_chat_admins = get_mi_list_user_admin()
	ban_list = get_mi_ban_list()
	file_list = os.listdir("destrebuters/")
	
	if message.chat.username == None:
		bot.send_message(message.chat.id, "У вас не указанно имя пользователя!")
	else:
		if str(message.chat.username) in file_list:
			bot.send_message(message.chat.id, "Вы уже дистребъютер!")
		elif str(message.chat.id) in ban_list:
			bot.send_message(message.chat.id, "Вы добавленны в бан")
		else:
			for id_chat_admin in id_chat_admins:
				if id_chat_admin != "":
					try:
						bot.send_message(int(id_chat_admin), "Пользователь :"+str(message.chat.id)+"-"+str(message.from_user.first_name)+" "+str(message.from_user.last_name)+"\nжелает получить доступ как дистребъютер\n\n [Добавить] - добавит пользователя как дистребъютера в систему\n [Игнорировать] - просто закроет это сообщение \n[Заблокировать] - запретит отправлять этому пользователю подобные сообщения", 
							reply_markup=get_me_buttons_on_add_user(
								str(message.chat.username),
								str(message.chat.id),
								"[Добавить]:"+str(message.chat.username)+"-"+str(message.from_user.first_name)+"-"+str(message.from_user.last_name)+"-"+str(message.chat.id)
								)
							)
					except:
						bot.send_message(int(id_chat_admin), "Пользователь :"+str(message.chat.id)+"-"+str(message.from_user.first_name)+" "+str(message.from_user.last_name)+"\nжелает получить доступ как дистребъютер\n\n [Добавить] - добавит пользователя как дистребъютера в систему\n [Игнорировать] - просто закроет это сообщение \n[Заблокировать] - запретит отправлять этому пользователю подобные сообщения", 
							reply_markup=get_me_buttons_on_add_user(
								str(message.chat.username),
								str(message.chat.id),
								"[Добавить]:"+str(message.chat.username)+"-rus-rus-"+str(message.chat.id)
								)
							)
			bot.send_message(message.chat.id, "Вы отправили запрос на получение прав дистребъютера")

@bot.message_handler(commands=['add_to_consul'])
def get_add_to_consultant(message):
	id_chat_admins = get_mi_list_user_admin()
	ban_list = get_mi_ban_list()
	file_list = os.listdir("consultant/")
	
	if message.chat.username == None:
		bot.send_message(message.chat.id, "У вас не указанно имя пользователя!")
	else:

		if str(message.chat.username) in file_list:
			bot.send_message(message.chat.id, "Вы уже консультант!")
		elif str(message.chat.id) in ban_list:
			bot.send_message(message.chat.id, "Вы добавленны в бан")
		else:
			
			for id_chat_admin in id_chat_admins:
				if id_chat_admin != "":
					try:
						bot.send_message(int(id_chat_admin), "Пользователь :"+str(message.chat.id)+"-"+str(message.from_user.first_name)+" "+str(message.from_user.last_name)+"\nжелает получить доступ как Консультант\n\n [Добавить] - добавит пользователя как Консультанта в систему\n [Игнорировать] - просто закроет это сообщение \n[Заблокировать] - запретит отправлять этому пользователю подобные сообщения", 
							reply_markup=get_me_buttons_on_add_user(
								str(message.chat.username),
								str(message.chat.id),
								"[add_cons]:"+str(message.chat.username)+"-"+str(message.from_user.first_name)+"-"+str(message.from_user.last_name)+"-"+str(message.chat.id)
								)
							)
					except:
						bot.send_message(int(id_chat_admin), "Пользователь :"+str(message.chat.id)+"-"+str(message.from_user.first_name)+" "+str(message.from_user.last_name)+"\nжелает получить доступ как Консультант\n\n [Добавить] - добавит пользователя как Консультанта в систему\n [Игнорировать] - просто закроет это сообщение \n[Заблокировать] - запретит отправлять этому пользователю подобные сообщения", 
							reply_markup=get_me_buttons_on_add_user(
								str(message.chat.username),
								str(message.chat.id),
								"[add_cons]:"+str(message.chat.username)+"-rus-rus-"+str(message.chat.id)
								)
							)
			bot.send_message(message.chat.id, "Вы отправили запрос на получение прав Консультанта")

@bot.message_handler(commands=['list_admins'])
def get_mi_list_admins(message):
	id_chat_admins = get_mi_list_user_admin()
	if str(message.chat.id) in id_chat_admins:
		namber_user = 0
		admins_list = get_mi_list("admin_list_all")
		for name_admin in admins_list:
			if name_admin != "":
				markup_buttons_add_rm = types.InlineKeyboardMarkup(row_width=1)
					
				button_add = types.InlineKeyboardButton("[pass] :"+name_admin, callback_data="pass :"+name_admin)
				button_rm = types.InlineKeyboardButton("[del] :"+name_admin, callback_data="del :"+name_admin)

				markup_buttons_add_rm.add(button_add,button_rm)
				namber_user += 1
				
				bot.send_message(message.chat.id, "пользователь №<"+str(namber_user)+"> :["+name_admin+"] - админ", reply_markup=markup_buttons_add_rm)
	else:
		bot.send_message(message.chat.id, "Нехватает прав доступа!")

@bot.message_handler(commands=['list_destrebuters'])
def get_mi_list_destrebuters(message):
	id_chat_admins = get_mi_list_user_admin()
	if str(message.chat.id) in id_chat_admins:
		file_list_destreb = os.listdir("destrebuters/")
		if len(file_list_destreb) != 0:
			namber_user = 0
			for user_destrebuters in file_list_destreb:
					markup_buttons_add_rm = types.InlineKeyboardMarkup(row_width=1)
						
					button_add = types.InlineKeyboardButton("[pass] :"+user_destrebuters, callback_data="[pass] :"+user_destrebuters)
					button_rm = types.InlineKeyboardButton("[del] :"+user_destrebuters, callback_data="[del] :"+user_destrebuters)

					markup_buttons_add_rm.add(button_add,button_rm)
					namber_user += 1
					
					bot.send_message(message.chat.id, "пользователь №<"+str(namber_user)+"> :["+user_destrebuters+"] - дистребъютер", reply_markup=markup_buttons_add_rm)
		else:
			bot.send_message(message.chat.id, "Таких пользователей нет")
	else:
		bot.send_message(message.chat.id, "Нехватает прав доступа!")

@bot.message_handler(commands=['list_consultant'])
def get_mi_list_consultant(message):
	id_chat_admins = get_mi_list_user_admin()
	if str(message.chat.id) in id_chat_admins:
		file_list_consultant = os.listdir("consultant/")
		if len(file_list_consultant) != 0:
			namber_user = 0
			for user_consultant in file_list_consultant:
					markup_buttons_add_rm = types.InlineKeyboardMarkup(row_width=1)
						
					button_add = types.InlineKeyboardButton("[pass] :"+user_consultant, callback_data="[pass] :"+user_consultant)
					button_rm = types.InlineKeyboardButton("[del] :"+user_consultant, callback_data="[dell] :"+user_consultant)

					markup_buttons_add_rm.add(button_add,button_rm)
					namber_user += 1
					
					bot.send_message(message.chat.id, "пользователь №<"+str(namber_user)+"> :["+user_consultant+"] - дистребъютер", reply_markup=markup_buttons_add_rm)
		else:
			bot.send_message(message.chat.id, "Таких пользователей нет")
	else:
		bot.send_message(message.chat.id, "Нехватает прав доступа!")

@bot.message_handler(commands=['list_chat'])
def get_mi_list_chat(message):
	file_list_consult = os.listdir("consultant/")
	if str(message.chat.username) in file_list_consult:

		file_list_chat = os.listdir("chat_dest/")
		if len(file_list_chat) != 0 : 
			for user_name in file_list_chat:
				with open("chat_dest/"+str(user_name), 'r') as file_user_info:

					info_user = file_user_info.read().split("\n")
					if str(info_user[0]) in file_list_chat:
						pass
						# bot.send_message(call.message.chat.id, "Уже начал общение!")
					else:
						with open("chat_dest/"+str(user_name), 'r') as file_user_info:
							mass_info_user = file_user_info.read().split("\n")
							markup_buttons_add_rm = types.InlineKeyboardMarkup(row_width=1)
				
							button_add = types.InlineKeyboardButton("[Войти в чат] c :"+str(mass_info_user[0]), callback_data="[Войти в чат] c :"+str(user_name))
							button_rm = types.InlineKeyboardButton("[Пропустить]:"+str(mass_info_user[0]), callback_data="[Пропустить]:"+str(mass_info_user[0]))

							markup_buttons_add_rm.add(button_add,button_rm)
							bot.send_message(message.chat.id, "Пользователь:  <"+str(mass_info_user[0])+">\nимя: "+str(mass_info_user[1])+"\nПришел от: "+str(mass_info_user[2])+"\nбаллы:"+str(mass_info_user[3])+"\nЖелает подключиться к чату",
								reply_markup=markup_buttons_add_rm
								)
		else:
			bot.send_message(message.chat.id, "в чате никого")
	else:
		bot.send_message(message.chat.id, "Нехватает прав доступа!")

@bot.message_handler(commands=['ban_list'])
def get_chec_ban_list(message):
	id_chat_admins = get_mi_list_user_admin()
	if str(message.chat.id) in id_chat_admins:
		ban_list = get_mi_list("ban_list")
		# print(ban_list)
		if ban_list[0] != '':
			namber_user = 0
			for name_ban in ban_list:
				if name_ban != "":
					markup_buttons_add_rm = types.InlineKeyboardMarkup(row_width=1)
						
					button_add = types.InlineKeyboardButton("[pass] :"+name_ban, callback_data="[pass] :"+name_ban)
					button_rm = types.InlineKeyboardButton("[del] :"+name_ban, callback_data=" dell :"+name_ban)

					markup_buttons_add_rm.add(button_add,button_rm)
					namber_user += 1
					
					bot.send_message(message.chat.id, "пользователь №<"+str(namber_user)+"> :["+name_ban+"] - в бане", reply_markup=markup_buttons_add_rm)	
		else:
			bot.send_message(message.chat.id, "В бане никого")
	else:
		bot.send_message(message.chat.id, "Нехватает прав доступа!")

@bot.message_handler(commands=['gr_o_d'])
def get_chec_destrb_stat(message):
	id_chat_admins = get_mi_list_user_admin()
	if str(message.chat.id) in id_chat_admins:
		file_list_user = os.listdir("users/")
		string_mass = ''
		for x in file_list_user:
			with open("users/"+str(x), 'r') as new_foto_file:
				a = new_foto_file.read().split("\n")
				string_mass = string_mass+" "+str(a[0])

		refer_id_name_in_user = string_mass.split(" ")

		mass_not_repit = []
		for refer in refer_id_name_in_user:
			if refer != '':
				if refer not in mass_not_repit:
					mass_not_repit.append(refer)

		for name_url in mass_not_repit:
			users_app = 0
			users_bye = 0
			for z in file_list_user:
				with open("users/"+str(z), 'r') as new_foto_file:
					dot = new_foto_file.read().split("\n")
					if str(dot[0]) == str(name_url):
						users_app += 1
						if int(dot[1]) == 0:
							users_bye +=1
			bot.send_message(message.chat.id, "По ссылке <"+str(name_url)+">\nперешло: "+str(users_app)+" - человек\nиз них: "+str(users_bye)+"\n воспользовались бонусами")
	else:
		bot.send_message(message.chat.id, "Нехватает прав доступа!")


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
	try:
		file_list_chat = os.listdir("chat_dest/")
		file_list_consult = os.listdir("consultant/")
		if str(message.chat.id) in file_list_chat:
			foto_file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
			downloaded_file = bot.download_file(foto_file_info.file_path)
			format_file = foto_file_info.file_path.split(".")
			src='foto/foto_pre_dfa.'+format_file[1]

			with open(src, 'wb') as new_foto_file:
				new_foto_file.write(downloaded_file)

			with open("chat_dest/"+str(message.chat.id), 'r') as messeg_name_in_file:
				id_user_chat = messeg_name_in_file.read().split("\n")
				# print(id_user_chat)
				if str(message.chat.username) in file_list_consult:
					bot.send_photo(int(id_user_chat[0]), open(str(src), 'rb'),"Консультант №<"+id_user_chat[0]+">")
				else:
					bot.send_photo(int(id_user_chat[0]), open(str(src), 'rb'),"User id <"+id_user_chat[0]+">")

		else:
			id_chat_admins = get_mi_list_user_admin()
			if str(message.chat.id) in id_chat_admins:
				if 	message.caption != '':
					caption_on_foto = message.caption.split("|")

					if caption_on_foto[0] == "/dow_fot":
						foto_file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
						downloaded_file = bot.download_file(foto_file_info.file_path)
						format_file = foto_file_info.file_path.split(".")
						src='foto/'+caption_on_foto[1]+"."+format_file[1]

						with open(src, 'wb') as new_foto_file:
							new_foto_file.write(downloaded_file)
						bot.reply_to(message,"Фото добавлено") 

					elif caption_on_foto[0] == "/get_n_t":
						global oll_prise
						towar = next((x for x in oll_prise if x == caption_on_foto[1]),None)
						if caption_on_foto[1] == towar:
							try:
								os.mkdir("categori/"+caption_on_foto[1])
								bot.send_message(message.chat.id, "создание директории.. отправь ещё раз")
							except:
								foto_file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
								downloaded_file = bot.download_file(foto_file_info.file_path)
								format_file = foto_file_info.file_path.split(".")
								src='foto/'+caption_on_foto[2]+"."+format_file[1]

								with open(src, 'wb') as new_foto_file:
									new_foto_file.write(downloaded_file)

								with open("categori/"+caption_on_foto[1]+"/"+caption_on_foto[2], 'w') as new_file_in_product:
									new_file_in_product.write(str(caption_on_foto[3]))
									new_file_in_product.close()

								bot.send_message(message.chat.id, "товар с картинкой добавлен")
						else:
							bot.send_message(message.chat.id, "ошибка...")
				else:
					bot.reply_to(message,"Неверная команда! Или не указанна вообще.\nУбедись в правильности написания описания к картинки.\n ")	
			else:
				bot.send_message(message.chat.id, "Нехватает прав доступа!") 
	except Exception as e:
		# print(e)
		bot.reply_to(message,e)

@bot.message_handler(content_types=['text'])
def main(message):
	if message.chat.type == 'private':
		global words_dot_chat
		id_chat_admins = get_mi_list_user_admin()
		file_list_chat = os.listdir("chat_dest/")
		file_list_consult = os.listdir("consultant/")
		file_list_destreb = os.listdir("destrebuters/")

		print(message.text.lower())
		text_is_commit = message.text
		mass_text_commit = text_is_commit.split("|")
		messeg_text = message.text.lower()

		if str(message.chat.id) in file_list_chat:
			if message.text == "<- Выход":
				try:
					if os.path.isfile("chat_dest/"+str(message.chat.id)) == True:
						markup_buttons_on_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
						buttons_on_start = types.KeyboardButton("/start")
						markup_buttons_on_start.add(buttons_on_start)
						
						with open("chat_dest/"+str(message.chat.id), 'r') as dell_file_user_name:
							name_file = dell_file_user_name.read().split("\n")
							
							if len(name_file) > 2:
								pass
							else:
								os.remove("chat_dest/"+str(name_file[0]))
								dell_file_user_name.close()
								bot.send_message(int(name_file[0]),"Пользователь закрыл чат", reply_markup=markup_buttons_on_start)
								
						os.remove("chat_dest/"+str(message.chat.id))
						bot.send_message(message.chat.id,"Вы вышли из чата", reply_markup=markup_buttons_on_start)
				except Exception as e:
					raise e
			else:
				with open("chat_dest/"+str(message.chat.id), 'r') as messeg_name_in_file:
					id_user_chat = messeg_name_in_file.read().split("\n")
					if str(message.chat.username) in file_list_consult:
						bot.send_message(int(id_user_chat[0]),"Консультант №<"+id_user_chat[0]+">\n"+str(message.text))
					else:
						bot.send_message(int(id_user_chat[0]),"User id <"+id_user_chat[0]+">\n"+str(message.text))

		elif message.text == "Полезный обзор":
			in_prise = (
						"что-то",
						"из товара",
						"тут",
						"будет"
						)
			bot.send_message(message.chat.id, "У тебя появились новые кнопки!\nВыбери категорию которая тебе интересна", reply_markup=get_mi_buttons(in_prise))
		
		elif message.text == "Консультант":
			markup_buttons_True_False = types.InlineKeyboardMarkup(row_width=1)
			button_add = types.InlineKeyboardButton("***[да]***", callback_data="***[да]***")
			button_rm = types.InlineKeyboardButton("**[нет]**", callback_data="**[нет]**")
			markup_buttons_True_False.add(button_add,button_rm)
			bot.send_message(message.chat.id, "наши контакты...")
			bot.send_message(message.chat.id, "Желаете перейти в чат?", reply_markup=markup_buttons_True_False)	

		elif message.text == "Наш сайт":
			bot.send_message(message.chat.id, "сайт....")

		elif message.text == "Дистребъютеры":
			if str(message.chat.id) in id_chat_admins:
				bot.send_message(message.chat.id, "будет сводка и кнопки по дистребьютерам")
			else:
				bot.send_message(message.chat.id, "Нехватает прав доступа!")

		elif message.text == "<- Назад":
			if str(message.chat.id) in id_chat_admins:
				bot.send_message(message.chat.id, "Верное решение! эти кнопочки по удобнее", reply_markup=markup_buttons_on_admins())

			elif str(message.chat.username) in file_list_destreb:
				bot.send_message(message.chat.id, "Верное решение! эти кнопочки по удобнее", reply_markup=markup_buttons_on_destrebuters())
			elif str(message.chat.username) in file_list_consult:
				bot.send_message(message.chat.id, "Верное решение! эти кнопочки по удобнее", reply_markup=markup_buttons_on_consultant())
			else:
				markup_buttons_on_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
				buttons_on_start = types.KeyboardButton("/start")
				markup_buttons_on_start.add(buttons_on_start)
				bot.send_message(message.chat.id, "Вы вернулись на старт", reply_markup=markup_buttons_on_start)

		elif message.text == "Личный кабинет":
			if str(message.chat.username) in file_list_destreb:
				hash_on_refer_text = str(message.chat.id)+"|"+str(message.from_user.first_name)+"|"+str(message.from_user.last_name)
				list_nik_name_user = os.listdir("users/")
				i = 0
				j = 0
				for nik_user in list_nik_name_user:
					with open("users/"+str(nik_user), 'r') as user_info_file:
						mass_ref_ball = user_info_file.read().split("\n")
						if str(mass_ref_ball[0]) == str(hash_on_refer_text):
							i += 1
							if int(mass_ref_ball[1]) == 0:
								j += 1

				bot.send_message(message.chat.id, "оттебя пришло: "+str(i)+"\nИз них: "+str(j)+"\nвоспользовались баллами")
			else:
				bot.send_message(message.chat.id, "Нехватает прав доступа!")


		elif mass_text_commit[0] == '/get_n_t':
			global oll_prise
			if str(message.chat.id) in id_chat_admins:
				towar = next((x for x in oll_prise if x == mass_text_commit[1]),None)
				if mass_text_commit[1] == towar:
					try:
						os.mkdir("categori/"+mass_text_commit[1])
						bot.send_message(message.chat.id, "создание директории.. отправь ещё раз")
					except:
						# /get_n_t|0мг-25мг|название товара|описание ыавп ыап ып ып
						with open("categori/"+mass_text_commit[1]+"/"+mass_text_commit[2], 'w') as f:
							f.write(str(mass_text_commit[3]))
							f.close()
						bot.send_message(message.chat.id, "товар добавлен")
				else:
					bot.send_message(message.chat.id, "Неверно указанна категория")
			else:
				bot.send_message(message.chat.id, "Нехватает прав доступа!")

		elif mass_text_commit[0] == '/gr_o_d':
			if str(message.chat.id) in id_chat_admins or str(message.chat.username) in file_list_consult:
				try:
					list_nik_name_user = os.listdir("users/")
					referal_user = 0
					refer_balls = 0
					with open("destrebuters/"+str(mass_text_commit[1]), 'r') as user_info_file:
						mass_id = user_info_file.read().split("-")
						for x in list_nik_name_user:
							with open("users/"+str(x), 'r') as user_info_file:
								mass_ref_ball = user_info_file.read().split("|")
								if str(mass_ref_ball[0]) == str(mass_id[0]):
									referal_user +=1
									ball_mass = mass_ref_ball[2].split("\n")
									if int(ball_mass[1]) == 0:
										refer_balls += 1
		
					bot.send_message(message.chat.id, "от дистребъютера: <"+str(mass_text_commit[1])+">\nпришло: "+str(referal_user)+"\nИз них: "+str(refer_balls)+"\nвоспользовались баллами")
				except Exception as e:
					# bot.send_message(message.chat.id,e)
					bot.send_message(message.chat.id, "Не верное указание комманды! Посмотри в воммандах правило работы с ээтой коммандой")
			else:
				bot.send_message(message.chat.id, "Нехватает прав доступа!")

		elif mass_text_commit[0] == '/grep':
			if str(message.chat.id) in id_chat_admins:
				try:
					if os.path.isfile("users/"+str(mass_text_commit[1])) == True:
						with open("users/"+str(mass_text_commit[1]), 'r') as file_users:
							info_user = file_users.read().split("\n")

							markup_buttons_add_rm = types.InlineKeyboardMarkup(row_width=1)
							button_add = types.InlineKeyboardButton("+ 100 баллов", callback_data="+ 100 :"+str(mass_text_commit[1]))
							button_rm = types.InlineKeyboardButton("- 100 баллов", callback_data="- 100 :"+str(mass_text_commit[1]))
							markup_buttons_add_rm.add(button_add,button_rm)

							bot.send_message(message.chat.id, 
								"Пользователь <"+str(mass_text_commit[1])+">\nПришел от:"+str(info_user[0])+"\nбаллы: "+str(info_user[1])+"\n\nнажмите кнопочки что бы убрать или добавить баллов пользователю",
								reply_markup=markup_buttons_add_rm)
					else:
						bot.send_message(message.chat.id, "Не верно указанн ник пользователя\nИли пользователь не пользовался реферальной системой")
				except:
					bot.send_message(message.chat.id, "Не верное указание комманды! Посмотри в воммандах правило работы с ээтой коммандой")
			else:
				bot.send_message(message.chat.id, "Нехватает прав доступа!")

		elif messeg_text in words_dot_chat:
			bot.send_message(message.chat.id, words_dot_chat[messeg_text])

		elif mass_text_commit[0] == '/oll_users':
			if str(message.chat.id) in id_chat_admins:
				try:
					with open("oll_users", 'r') as file_oll_users:
						oll_users = file_oll_users.read().split("\n")
						for user_in_file in oll_users:
							try:
								bot.send_message(int(user_in_file), str(mass_text_commit[1]))
							except:
								pass
				except:
					bot.send_message(message.chat.id, "Не верное указание комманды! Посмотри в воммандах правило работы с ээтой коммандой")
			else:
				bot.send_message(message.chat.id, "Нехватает прав доступа!")
			
		else:
			bot.send_message(message.chat.id, 'Я не знаю что значит \n(' + message.text + ')\n Рекомендую использовать кнопки, что бы избежать подобного сообщения' )

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			global oll_prise
			towar = next((x for x in oll_prise if x == call.data),None)

			if towar == call.data:
				try:
					file_list_in_directory= os.listdir("categori/"+call.data)
					mark_button_in_product = types.InlineKeyboardMarkup(row_width=1)
					for file_in_directory in file_list_in_directory:
						button_on_product = types.InlineKeyboardButton(file_in_directory, callback_data=file_in_directory)
						mark_button_in_product.add(button_on_product)
					bot.send_message(call.message.chat.id, 'выберете товар', reply_markup=mark_button_in_product)
				except Exception as e:
					bot.send_message(call.message.chat.id, 'товар ещё не добавлен')

			elif call.data.startswith(" [+] :") == True:
				admin_list_all_users = get_mi_list("admin_list_all")
				text_button_on_input_admin = call.data.split(":")
				id_user_chat = text_button_on_input_admin[1].split("-")

				if str(id_user_chat[0]) in admin_list_all_users:
					bot.send_message(call.message.chat.id, 'Пользователь :'+id_user_chat[0]+' уже был добавлен как админ')
				else:
					get_mi_add_admins_disteb("admin_list_all",str(id_user_chat[0])+"-"+str(id_user_chat[1])+"-"+str(id_user_chat[2])+"-"+str(id_user_chat[3]))
					bot.send_message(call.message.chat.id, 'Новый пользователь :\n'+str(id_user_chat[0])+"\nимя - "+str(id_user_chat[1])+"\nфамилия -"+str(id_user_chat[2])+'\nдобавлин как администратор')
					bot.send_message(int(id_user_chat[3]), 'Вас добавили как администратора',reply_markup=markup_buttons_on_admins())

			elif call.data.startswith(" [-] :") == True:
				id_chat_admins = get_mi_list_user_admin()
				if str(call.message.chat.id) in id_chat_admins:
					ban_list_users = get_mi_list("ban_list")
					text_button_on_input_admin = call.data.split(":")

					if text_button_on_input_admin in ban_list_users:
						bot.send_message(call.message.chat.id, 'Пользователь :'+text_button_on_input_admin[1]+' уже был добавлен в бан')
					else:
						id_user_chat =  text_button_on_input_admin[1].split('-')
						with open("ban_list", 'a') as file_oll_users:
							file_oll_users.write(text_button_on_input_admin[1]+"\n")
							file_oll_users.close()
						bot.send_message(call.message.chat.id, 'Пользователь :'+text_button_on_input_admin[1]+' Помечан как шалун и неимеет права получить даминские права')
						bot.send_message(int(id_user_chat[1]), 'вам отказанно в вправах доступа')
				else:
					bot.send_message(call.message.chat.id, "Нехватает прав доступа!")


			elif call.data.startswith("del :") == True:
				id_chat_admins = get_mi_list_user_admin()
				if str(call.message.chat.id) in id_chat_admins:
					oll_users = get_mi_list("admin_list_all")
					text_button_on_input_admin_name_user = call.data.split(":")
					oll_users.remove(text_button_on_input_admin_name_user[1])
				
					with open("admin_list_all", 'w') as file_oll_users:
						for x in oll_users:
							if x != '':
								file_oll_users.write(x+"\n")
						file_oll_users.close()
				else:
					bot.send_message(call.message.chat.id, "Нехватает прав доступа!")
	

			elif call.data.startswith("[Добавить]") == True:
				
				text_button_on_input_admin = call.data.split(":")
				id_user_chat = text_button_on_input_admin[1].split("-")
				get_mi_add_admins_disteb("destrebuters/"+str(id_user_chat[0]),str(id_user_chat[3])+"-"+str(id_user_chat[1]))
				bot.send_message(call.message.chat.id, 'Новый пользователь :\n'+str(id_user_chat[0])+"\nимя - "+str(id_user_chat[1])+"\nфамилия -"+str(id_user_chat[2])+'\nдобавлин как дистребъютер')
				bot.send_message(int(id_user_chat[3]), 'Вас добавили как дистребъютера',reply_markup=markup_buttons_on_destrebuters())

			elif call.data.startswith("[del] :") == True:
				id_chat_adm = get_mi_list_user_admin()
				if str(call.message.chat.id) in id_chat_adm:
					text_button_on_input_admin = call.data.split(":")
					if os.path.isfile("destrebuters/"+text_button_on_input_admin[1]) == True:
						os.remove("destrebuters/"+text_button_on_input_admin[1])
						bot.send_message(call.message.chat.id, 'Пользователь ['+text_button_on_input_admin[1]+"] - был удалён из дистребъютеров")
				else:
					bot.send_message(call.message.chat.id, "Нехватает прав доступа!")

			elif call.data.startswith(" dell :") == True:
				id_chat_adm = get_mi_list_user_admin()
				if str(call.message.chat.id) in id_chat_adm:
					oll_users = get_mi_list("ban_list")
					text_button_on_input_admin_name_user = call.data.split(":")
					oll_users.remove(text_button_on_input_admin_name_user[1])
					with open("ban_list", 'w') as file_oll_users:
						for x in oll_users:
							if x != '':
								file_oll_users.write(x+"\n")
						file_oll_users.close()
				else:
					bot.send_message(call.message.chat.id, "Нехватает прав доступа!")
			
			elif call.data.startswith("[dell] :") == True:
				id_chat_adm = get_mi_list_user_admin()
				if str(call.message.chat.id) in id_chat_adm:
					text_button_on_input_admin = call.data.split(":")
					if os.path.isfile("consultant/"+text_button_on_input_admin[1]) == True:
						os.remove("consultant/"+text_button_on_input_admin[1])
						bot.send_message(call.message.chat.id, 'Пользователь ['+text_button_on_input_admin[1]+"] - был удалён из консультантов")
				else:
					bot.send_message(call.message.chat.id, "Нехватает прав доступа!")

			elif call.data.startswith("[add_cons]:") == True:
				text_button_on_input_admin = call.data.split(":")
				id_user_chat = text_button_on_input_admin[1].split("-")
				get_mi_add_admins_disteb("consultant/"+str(id_user_chat[0]),str(id_user_chat[3])+"-"+str(id_user_chat[1]))
				bot.send_message(call.message.chat.id, 'Новый пользователь :\n'+str(id_user_chat[0])+"\nимя - "+str(id_user_chat[1])+"\nфамилия -"+str(id_user_chat[2])+'\nдобавлин как Консультант')
				bot.send_message(int(id_user_chat[3]), 'Вас добавили как Консультанта',reply_markup=markup_buttons_on_consultant())


			elif call.data.startswith("+ 100 :") == True:
				text_button_on_input_consul = call.data.split(":")
				try:
					if os.path.isfile("users/"+str(text_button_on_input_consul[1])) == True:
						with open("users/"+str(text_button_on_input_consul[1]), 'r') as file_users:
							info_user = file_users.read().split("\n")
							file_users.close()

						new_balls = int(info_user[1])+100
						with open("users/"+str(text_button_on_input_consul[1]), 'w') as file:
							file.write(str(info_user[0])+"\n"+str(new_balls)+"\n")
							

						bot.send_message(call.message.chat.id, "баллы начисленны теперь:"+str(new_balls))

					else:
						bot.send_message(call.message.chat.id, "Не верно указанн ник пользователя")
				except:
					bot.send_message(call.message.chat.id, "Не верное указание комманды! Посмотри в воммандах правило работы с ээтой коммандой")

			elif call.data.startswith("- 100 :") == True:
				text_button_on_input_consul = call.data.split(":")
				
				try:
					if os.path.isfile("users/"+str(text_button_on_input_consul[1])) == True:
						with open("users/"+str(text_button_on_input_consul[1]), 'r') as file_users:
							info_user = file_users.read().split("\n")
							file_users.close()

						if int(info_user[1]) != 0:
							new_balls = int(info_user[1])-100
							with open("users/"+str(text_button_on_input_consul[1]), 'w') as file:
								file.write(str(info_user[0])+"\n"+str(new_balls)+"\n")
								

							bot.send_message(call.message.chat.id, "баллы начисленны теперь:"+str(new_balls))
						else:
							bot.send_message(call.message.chat.id, "-_- их и так нет")
					else:
						bot.send_message(call.message.chat.id, "Не верно указанн ник пользователя")
				except:
					bot.send_message(call.message.chat.id, "Не верное указание комманды! Посмотри в воммандах правило работы с ээтой коммандой")


			elif call.data.startswith("***[да]***") == True:
				try:
					file_list_consult = os.listdir("consultant/")
					file_list_chat = os.listdir("chat_dest/")
					
					if os.path.isfile("users/"+call.message.chat.username) == True:
						with open("users/"+call.message.chat.username, 'r') as file_user_info:
							file_user_info = file_user_info.read().split("\n")
							# print(file_user_info)
							with open("chat_dest/"+str(call.message.chat.id), 'w') as file_oll_users:
								file_oll_users.write(str(call.message.chat.username)+"\n"+str(call.message.chat.first_name)+"\n"+str(file_user_info[0])+"\n"+str(file_user_info[1])+"\n")
								file_oll_users.close()
					else:
						with open("chat_dest/"+str(call.message.chat.id), 'w') as file_oll_users:
							file_oll_users.write(str(call.message.chat.username)+"\n"+str(call.message.chat.first_name)+"\nnone\nnone\n")
							file_oll_users.close()

					for file_destreb in file_list_consult:
						with open("consultant/"+file_destreb, 'r') as file_id_name:

							id_name_destreb = file_id_name.read().split("-")
							if str(id_name_destreb[0]) in file_list_chat:
								pass
							else:
								with open("chat_dest/"+str(call.message.chat.id), 'r') as file_user_info:
									mass_info_user = file_user_info.read().split("\n")
									markup_buttons_add_rm = types.InlineKeyboardMarkup(row_width=1)
						
									button_add = types.InlineKeyboardButton("[Войти в чат] c :"+str(mass_info_user[0]), callback_data="[Войти в чат] c :"+str(call.message.chat.id))
									button_rm = types.InlineKeyboardButton("[Пропустить]:"+str(mass_info_user[0]), callback_data="[Пропустить]:"+str(mass_info_user[0]))

									markup_buttons_add_rm.add(button_add,button_rm)
									bot.send_message(int(id_name_destreb[0]), "Пользователь:  <"+str(mass_info_user[0])+">\nимя: "+str(mass_info_user[1])+"\nПришел от: "+str(mass_info_user[2])+"\nбаллы:"+str(mass_info_user[3])+"\nЖелает подключиться к чату",
										reply_markup=markup_buttons_add_rm
										)


					markup_buttons_on_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
					button_back = types.KeyboardButton("<- Выход")
					markup_buttons_on_back.add(button_back)
					bot.send_message(call.message.chat.id, 
						"Пожалуйсто подождите пока к вам подключиться свободный дистребъютер\n\nДля выхода из чата следует нажать кнопочку <выход> Чат поддерживает текст и картинки",
						reply_markup=markup_buttons_on_back
						)
				except Exception as e:
					raise e
			
			elif call.data.startswith("[Войти в чат] c :") == True:
				destrebus_call = call.data.split(":")
				if os.path.isfile("chat_dest/"+str(destrebus_call[1])) == True:
					file_list_chat = os.listdir("chat_dest/")

					with open("chat_dest/"+str(destrebus_call[1]), 'r') as file_user_info:
						info_user = file_user_info.read().split("\n")
						if str(info_user[0]) in file_list_chat:
							bot.send_message(call.message.chat.id, "Уже начал общение!")
						else:
							with open("chat_dest/"+str(destrebus_call[1]), 'w') as file_user_info:
								file_user_info.write(str(call.message.chat.id)+"\n")

							with open("chat_dest/"+str(call.message.chat.id), 'w') as file_user_info:
								file_user_info.write(str(destrebus_call[1])+"\n")

								markup_buttons_on_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
								button_back = types.KeyboardButton("<- Выход")

								markup_buttons_on_back.add(button_back)
								bot.send_message(call.message.chat.id, 
									"Вы подключились к чату с :<"+info_user[0]+">\nИмя: "+info_user[1]+"\nПришел от: "+info_user[2]+"\nбаллы:"+info_user[3]+"\n\nПосле завершения общения появяться кнопочки на добавления или снятия баллов",
									reply_markup=markup_buttons_on_back
									)
								bot.send_message(int(destrebus_call[1]), "К вам подключился консультант с №<"+str(call.message.chat.id)+">\nИмя: "+str(call.message.chat.first_name))

			elif call.data.startswith("**[нет]**") == True:
				pass
			elif call.data.startswith("[Пропустить]:") == True:
				pass
			elif call.data.startswith("[pass] :") == True:
				pass
			else:
				try:
					file_list_in_directory = os.listdir("categori/")
					format_on_file = ['.jpg', '.png']
					cycle_step = 0
					loop_step_in_loop = 0
					while cycle_step < len(file_list_in_directory):
						if os.path.isfile("categori/"+file_list_in_directory[cycle_step]+"/"+call.data) == True:

							while loop_step_in_loop < len(format_on_file):
								if os.path.isfile("foto/"+call.data+format_on_file[loop_step_in_loop]) == True:
									doc = open('foto/'+call.data+format_on_file[loop_step_in_loop], 'rb')
									with open("categori/"+file_list_in_directory[cycle_step]+"/"+call.data, 'r') as f:
										caption = f.read()
										name_towar_in_prise = call.data
										# buttons_on_order = get_mi_button_on_to_order(name_towar_in_prise)

										bot.send_photo(call.message.chat.id, doc, caption, 
											# reply_markup=buttons_on_order
											)
										loop_step_in_loop=0
										break
								else:
									loop_step_in_loop+=1
							
							if loop_step_in_loop > 0:
								with open("categori/"+file_list_in_directory[cycle_step]+"/"+call.data, 'r') as file_in_user_prise:
									file_in_user_prise = file_in_user_prise.read()
									name_towar_in_prise = call.data
									# buttons_on_order = get_mi_button_on_to_order(name_towar_in_prise)

									bot.send_message(call.message.chat.id, 'вы выбрали '+call.data+"\n"+file_in_user_prise,
									# reply_markup=buttons_on_order
									)
							break

						else:
							cycle_step+=1
				except Exception as e:
					bot.send_message(call.message.chat.id, e)

			try:
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= "вы выбрали "+ call.data, reply_markup=None)
			except:
				pass

	except Exception as e:
		print(repr(e))

if __name__ == '__main__':
	bot.polling(none_stop=True, interval=0)
