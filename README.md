# Telegram_bot_to_order
bot to order

Этот бот делался на заказ. По сути он является основой для магазина в ТГ.
У него имеются функции:

/start - команда для начала работы с ботом
/start=<referal_url> - команда для для начала работы с указанием от кого пришел. Это непосредственно ссылка которая генерируется  командой указанной ниже
/commands - список доступных команд всем
/add_to_admins - запрос на добавление в админы
/list_admins - список админов и удаление из них

/add_to_consul - запрос на добавление в консультанты
/list_consultant - список консультантов и удаление из них

/add_to_destreb - запрос на добавление в дистрибьюторы
/list_destrebuters - список Дистрибьюторов и удаление из них

/list_chat - список кто ждёт в чате + начало общения с ожидающими
/ban_list - список тех кто в бане + удаления из бана
(в бан попадают те кто отправлял администраторам запросы на получения прав)
/grep - поиск по пользователям + начисление или списание баллов
Примечание: Следует точно указывать ник пользователя, ник пользователя будет высвечиваться в самом верху при активации пользователем чата
прямой слеш это спец символ для разделения команды на саму команду и полезную нагрузку
Пример: /grep|FreeLagGavr
/adm_commands - команды с доступом только администратором
/url_refer - команда для генерации реферальной ссылки

сайт - наш сайт
консультант - связь с консультантом
полезный обзор - каталог товара


/gr_o_d - инфа по всем реферальным ссылкам /gr_o_d|<ник дистрибьютора> - сколько именно людей пришла  и сколько из них воспользовались баллами
Личный кабинет - команда для вывода инфы про себя так же доступна дистрибьюторам
/oll_users|<всем привет> - команда для массовой рассылки новости
/dow_fot|<имя картинки>
-также может заменить уже существующую

/get_n_t|<категория товара>|<название товара>|<описание + цена + остальное>

Пример:/get_n_t|Что-то|тут имя товара|а здесь описание цена:200р

------

Примечание категории уже созданы! И необходимо использовать уже созданные категории, создание новых категорий возможно только через разработчика. Следует явно указывать категорию.

ВАЖНО! имя товара не может быть одинаковым, следует использовать уникальное имя товара!
пример:<Лед лампа на 100w> и <лед лампа на 100w> разные имена. НО лучше использовать название

Для загрузки товара с картинкой и описанием следует, загрузить картинку и добавить к ней описание с командой. Сама команда и пример команды выше - в своём роде универсальная команда

