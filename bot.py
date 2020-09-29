import config
import logging
import keyboard as kb

from aiogram import Bot,Dispatcher,executor,types
from sqlighter import SQLighter

#Базовый уровень логов
logging.basicConfig(level=logging.INFO)

#инициализация бота
bot = Bot(token=config.API_TOKEN)

dp = Dispatcher(bot)

#подключение к БД
db = SQLighter('database.db')

## Функция старт
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        await bot.send_sticker(message.from_user.id,
                               "CAACAgIAAxkBAAEBT3RfV25ONY5QuWBe8MMqaqzUoW0aQAACuj8AAuCjggcykMz6vc920hsE")
        await bot.send_message(message.from_user.id,
                               "Приветствую! Я бот-помощник для студентов :)\nЗдесь ты можешь посмотреть актуальное расписание для твоей группы, рейтинги и узнать новости.\n")
        db.add_subscriber(message.from_user.id)

        await bot.send_message(message.from_user.id, "Давай мы определим твою группу",
                               reply_markup=kb.group_head_keyboard)

    else:
        await bot.send_message(message.from_user.id,"Ты уже добавлен в базу, еще раз команду /start вызывать не нужно")

## Группы(11 или 12)+Подгруппы (1 или 2)
@dp.message_handler()
async def message_handler(message: types.Message):
    if (message.text == kb.button_1_head_text):
        db.group_one_SQL(message.from_user.id)
        await bot.send_message(message.from_user.id, "Окей, ты с 11 группы. Теперь скажи свою подгруппу",reply_markup=kb.group_body_keyboard)
    if (message.text == kb.button_2_head_text):
        db.group_two_SQL(message.from_user.id)
        await bot.send_message(message.from_user.id, "Окей, ты с 12 группы. Теперь скажи свою подгруппу",reply_markup=kb.group_body_keyboard)

    if (message.text == kb.button_1_body_text):
        if (db.check_group_head(message.from_user.id)==11):
            db.group_one_BODY(message.from_user.id)
            await bot.send_message(message.from_user.id, "Ты успешно записан в 11 группу, 1 подгруппу",reply_markup=kb.week_keyboard)
            print(message.from_user.id,' записан в 11.1')
        if (db.check_group_head(message.from_user.id) == 12):
            db.group_one_BODY(message.from_user.id)
            await bot.send_message(message.from_user.id, "Ты успешно записан в 12 группу, 1 подгруппу",reply_markup=kb.week_keyboard)
            print(message.from_user.id,' записан в 12.1')
    if (message.text == kb.button_2_body_text):
        if (db.check_group_head(message.from_user.id)==11):
            db.group_two_BODY(message.from_user.id)
            await bot.send_message(message.from_user.id, "Ты успешно записан в 11 группу, 2 подгруппу",reply_markup=kb.week_keyboard)
            print(message.from_user.id,' записан в 11.2')
        if (db.check_group_head(message.from_user.id) == 12):
            db.group_two_BODY(message.from_user.id)
            await bot.send_message(message.from_user.id, "Ты успешно записан в 12 группу, 2 подгруппу",reply_markup=kb.week_keyboard)
            print(message.from_user.id,' записан в 12.2')


    ##Расписание на дни недели
    """Понедельник"""
    if (message.text == kb.button_monday_text):
        """КБ11"""
        if (db.check_group_head(message.from_user.id)==11):
            """1 подгруппа"""
            if (db.check_group_body(message.from_user.id)==1):

                await bot.send_message(message.from_user.id,"💥12:20 - 13:55💥\n"
                                                      "Лабораторна робота. Викладач - Подолян А.О.\n"
                                                      "🌎Zoom: ідентифікатор 499 928 9620, пароль 0czhaT\n\n"
                                                            "💥14:00-15:20💥\n"
                                                            "Лекція - 9 тижнів, на 10 тиждень і далі - практика\n"
                                                            "🌎Лекція у Zoom: ідентификатор - 242 180 1297, пароль - 5SWbMf\n"
                                                            "🌎Практика у Zoom: ідентифікатор - 242 180 1297,пароль - 5SWbMf\n\n"
                                                            "💥15:25-16:45💥\n"
                                                            "Практична робота. Викладач - Коротченков О.О.\n"
                                                            "🌎Zoom: ідентифікатор 242 180 1297, пароль 5SWbMf\n",reply_markup=kb.week_keyboard)


            """2 подгруппа"""
            if (db.check_group_body(message.from_user.id)==2):
                await bot.send_message(message.from_user.id,"💥12:20 - 13:55💥\n"
                                                      "Лабораторна робота. Викладач - Подолян А.О.\n"
                                                      "🌎Zoom: ідентифікатор 499 928 9620, пароль 0czhaT\n\n"
                                                            "💥14:00-15:20💥\n"
                                                            "Лекція - 9 тижнів, на 10 тиждень і далі - практика\n"
                                                            "🌎Лекція у Zoom: ідентификатор - 242 180 1297, пароль - 5SWbMf\n"
                                                            "🌎Практика у Zoom: ідентифікатор - 242 180 1297,пароль - 5SWbMf\n\n"
                                                            "💥15:25-16:45💥\n"
                                                            "Практична робота. Викладач - Коротченков О.О.\n"
                                                            "🌎Zoom: ідентифікатор 242 180 1297, пароль 5SWbMf\n",reply_markup=kb.week_keyboard)
        """КБ12"""
        if (db.check_group_head(message.from_user.id)==12):
            """1 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 1):
                await bot.send_message(message.from_user.id, "💥12:20 - 13:55💥\n"
                                                       "Лабораторна робота. Викладач - Козаченко В.В.\n"
                                                       "🌎Zoom: ідентифікатор 367 632 8607, пароль 678075\n\n"
                                                             "💥14:00-15:20💥\n"
                                                            "Лекція - 9 тижнів, на 10 тиждень і далі - практика\n"
                                                            "🌎Лекція у Zoom: ідентификатор - 242 180 1297, пароль - 5SWbMf\n"
                                                            "🌎Практика у Zoom: ідентифікатор - 367 632 8607,пароль - 678075\n\n"
                                                             "💥15:25-16:45💥\n"
                                                             "Практика. Викладач - Козаченко В.В\n"
                                                             "🌎Zoom: ідентифікатор - 367 632 8607,пароль - 678075\n",reply_markup=kb.week_keyboard)
            """2 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 2):
                await bot.send_message(message.from_user.id,"💥12:20 - 13:55💥\n"
                                                       "Лабораторна робота. Викладач - Козаченко В.В.\n"
                                                       "🌎Zoom: ідентифікатор 367 632 8607, пароль 678075\n\n"
                                                             "💥14:00-15:20💥\n"
                                                            "Лекція - 9 тижнів, на 10 тиждень і далі - практика\n"
                                                            "🌎Лекція у Zoom: ідентификатор - 242 180 1297, пароль - 5SWbMf\n"
                                                            "🌎Практика у Zoom: ідентифікатор - 367 632 8607,пароль - 678075\n\n"
                                                             "💥15:25-16:45💥\n"
                                                             "Практика. Викладач - Козаченко В.В\n"
                                                             "🌎Zoom: ідентифікатор - 367 632 8607,пароль - 678075\n",reply_markup=kb.week_keyboard)
    """Вторник"""
    if (message.text == kb.button_tuesday_text):
        """КБ11"""
        if (db.check_group_head(message.from_user.id) == 11):
            """1 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 1):
                await bot.send_message(message.from_user.id, "💥10:30 - 11:50💥\n"
                                                             "Вища математика(практика). Викладач - Лукова Н.В.\n"
                                                             "Дати: (22.09,29.09,06.10, 13.10,20.10, 27.10, 03.11, 10.11, 17.11, 24.11,01.12, 8.12)\n"
                                                             "🌎Посилання у Teams\n\n"
                                                             "💥14:00-15:20💥\n"
                                                             "Вища математика(лекція). Викладач - Лукова Н.В.\n"
                                                             "Дати: (22.09,29.09,06.10, 13.10,20.10, 27.10, 03.11, 10.11, 17.11, 24.11)\n"
                                                             "🌎Посилання у Teams\n\n"
                                                             "💥15:25-16:45💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності(лабораторна). Викладач - Шестак Я.В.\n"
                                                             "Дати: (22.09, 29.09, 06.10,13.10, 20.10, 27.10, 03.11,10.11, 17.11,24.11 )\n"
                                                             "🌎Zoom: https://us04web.zoom.us/j/78063496838?pwd=Q2h2UXBEb09VelVBaS9uSjhlZ2Nwdz09\n",reply_markup=kb.week_keyboard)


            """2 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 2):
                await bot.send_message(message.from_user.id, "💥10:30 - 11:50💥\n"
                                                             "Вища математика(практика). Викладач - Лукова Н.В.\n"
                                                             "Дати: (22.09,29.09,06.10, 13.10,20.10, 27.10, 03.11, 10.11, 17.11, 24.11,01.12, 8.12)\n"
                                                             "🌎Посилання у Teams\n\n"
                                                             "💥14:00-15:20💥\n"
                                                             "Вища математика(лекція). Викладач - Лукова Н.В.\n"
                                                             "Дати: (22.09,29.09,06.10, 13.10,20.10, 27.10, 03.11, 10.11, 17.11, 24.11)\n"
                                                             "🌎Посилання у Teams\n\n"
                                                             "💥15:25-16:45💥\n"
                                                             "Вища математика(лабораторна). Викладач - Лукова Н.В.\n"
                                                             "Дати: ( 22.09, 29.09, 06.10,13.10, 20.10, 27.10, 03.11,10.11, 17.11,24.11,01.12, 08.12)"
                                                             "🌎Посилання в Teams\n",reply_markup=kb.week_keyboard)
        """КБ12"""
        if (db.check_group_head(message.from_user.id) == 12):
            """1 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 1):
                await bot.send_message(message.from_user.id, "💥9:00 - 10:20💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності. Викладач - Шестак Я.В.\n"
                                                             "Дати:(22.09, 29.09, 06.10,13.10, 20.10, 27.10, 03.11,10.11, 17.11,24.11 )\n"
                                                             "🌎Zoom: https://us04web.zoom.us/j/73182764668?pwd=clpDcUJpL2gzditManFFUTFuZHQ3Zz09\n\n"
                                                             "💥10:30-11:50💥\n"
                                                             "Вища математика. Викладач - Мірутенко Л.В.\n"
                                                             "Дати:(22.09, 29.09, 06.10,13.10, 20.10, 27.10, 03.11,10.11, 17.11,24.11,01.12, 08.12)\n"
                                                             "🌎Google Meet: https://meet.google.com/oiw-gogx-nxw\n\n"
                                                             "💥12:10-13:30💥\n"
                                                             "Вища математика(лекція). Викладач - Лукова Н.В.\n"
                                                             "Дати: (22.09,29.09,06.10, 13.10,20.10, 27.10, 03.11, 10.11, 17.11, 24.11)\n"
                                                             "🌎Посилання у Teams\n\n",reply_markup=kb.week_keyboard)
            """2 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 2):
                await bot.send_message(message.from_user.id,
                                                             "💥10:30-11:50💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності. Викладач - Шестак Я.В.\n"
                                                             "Дати:(22.09, 29.09, 06.10,13.10, 20.10, 27.10, 03.11,10.11, 17.11,24.11 )\n"
                                                             "🌎Zoom: https://us04web.zoom.us/j/76624310671?pwd=QVpIS0plNEhyWGtZRGJWdDBpZVhrUT09\n\n"
                                                             "💥12:10-13:30💥\n"
                                                             "Вища математика(лекція). Викладач - Лукова Н.В.\n"
                                                             "Дати: (22.09,29.09,06.10, 13.10,20.10, 27.10, 03.11, 10.11, 17.11, 24.11)\n"
                                                             "🌎Посилання у Teams\n\n"
                                                             "💥13:40-15:00💥\n"
                                                             "Вища математика. Викладач - Мірутенко Л.В.\n"
                                                             "Дати:(22.09, 29.09, 06.10,13.10, 20.10, 27.10, 03.11,10.11, 17.11,24.11,01.12, 08.12)\n"
                                                             "🌎Google Meet: https://meet.google.com/oiw-gogx-nxw\n\n",reply_markup=kb.week_keyboard)
    """Среда"""
    if(message.text == kb.button_wednesday_text):
        """КБ11"""
        if (db.check_group_head(message.from_user.id) == 11):
            """1 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 1):
                await bot.send_message(message.from_user.id, "💥9:00 - 10:20💥\n"
                                                             "Вступ до фаху(Лекція). Викладач - Мірутенко Л.В.\n"
                                                             "Дати: (23.09, 07.10, 21.10, 04.11, 18.11)\n"
                                                             "🌎Google Meet: https://meet.google.com/oiw-gogx-nxw\n\n"
                                                             "💥10:30-11:50💥\n"
                                                             "Вступ до університетських студій(лекція). Викладач - Левінець Р.П.\n"
                                                             "Дати: з 23.09 до 9.12\n"
                                                             "🌎Google Meet: https://meet.google.com/cwj-ugif-mhr?pli=1&authuser=1&hma=1&hmv=1\n\n"
                                                             "💥12:10-13:30💥\n"
                                                             "Англійська мова. Викладач - Каленченко О.О.\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper), Ідентифікатор конференції 793 5998 6806, пароль 3txaNh\n\n"
                                                             "Zoom(inter),Посилання: https://us02web.zoom.us/j/85063950841?pwd=aGM5RDJqcThkNEp2NlkydmVCb1hBdz09\n"

                                                             "💥13:40-15:00💥\n"
                                                             "Англійська мова. Викладач - Каленченко О.О.\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper), Ідентифікатор конференції 793 5998 6806, пароль 3txaNh\n\n"
                                                             "Zoom(inter),Посилання: https://us02web.zoom.us/j/85063950841?pwd=aGM5RDJqcThkNEp2NlkydmVCb1hBdz09",reply_markup=kb.week_keyboard)

            """2 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 2):
                await bot.send_message(message.from_user.id, "💥9:00 - 10:20💥\n"
                                                             "Вступ до фаху(Лекція). Викладач - Мірутенко Л.В.\n"
                                                             "Дати: (23.09, 07.10, 21.10, 04.11, 18.11)\n"
                                                             "🌎Google Meet: https://meet.google.com/oiw-gogx-nxw\n\n"
                                                             "💥10:30-11:50💥\n"
                                                             "Вступ до університетських студій(лекція). Викладач - Левінець Р.П.\n"
                                                             "Дати: з 23.09 до 9.12\n"
                                                             "🌎Google Meet: https://meet.google.com/cwj-ugif-mhr?pli=1&authuser=1&hma=1&hmv=1\n\n"
                                                             "💥12:10-13:30💥\n"
                                                             "Англійська мова. Викладач - Каленченко О.О.\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper), Ідентифікатор конференції 793 5998 6806, пароль 3txaNh\n\n"
                                                             "Zoom(inter),Посилання: https://us02web.zoom.us/j/85063950841?pwd=aGM5RDJqcThkNEp2NlkydmVCb1hBdz09\n"

                                                             "💥13:40-15:00💥\n"
                                                             "Англійська мова. Викладач - Каленченко О.О.\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper), Ідентифікатор конференції  776 8994 0791, пароль 0JELfy\n\n"
                                                             "Zoom(inter),Посилання: https://us02web.zoom.us/j/85063950841?pwd=aGM5RDJqcThkNEp2NlkydmVCb1hBdz09",reply_markup=kb.week_keyboard)
        """КБ12"""
        if (db.check_group_head(message.from_user.id) == 12):
            """1 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 1):
                await bot.send_message(message.from_user.id, "💥9:00 - 10:20💥\n"
                                                             "Вступ до фаху(Лекція). Викладач - Мірутенко Л.В.\n"
                                                             "Дати: (23.09, 07.10, 21.10, 04.11, 18.11)\n"
                                                             "🌎Google Meet: https://meet.google.com/oiw-gogx-nxw\n\n"
                                                             "💥10:30-11:50💥\n"
                                                             "Вступ до університетських студій(лекція). Викладач - Левінець Р.П.\n"
                                                             "Дати: з 23.09 до 9.12\n"
                                                             "🌎Google Meet: https://meet.google.com/cwj-ugif-mhr?pli=1&authuser=1&hma=1&hmv=1\n\n"
                                                             "💥12:10-13:30💥\n"
                                                             "Англійська мова. Викладач - Костенко Д.В.\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper), https://us02web.zoom.us/j/83316091819?pwd=bDBoSm51amFkWHl4dEFnZlZ6THRtZz09\n"
                                                             "Zoom(inter), https://us02web.zoom.us/j/85063950841?pwd=aGM5RDJqcThkNEp2NlkydmVCb1hBdz09\n\n"

                                                                "💥13:40-15:00💥\n"
                                                             "Англійська мова. Викладач - Костенко Д.В.\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper), https://us02web.zoom.us/j/83316091819?pwd=bDBoSm51amFkWHl4dEFnZlZ6THRtZz09\n"
                                                             "Zoom(inter), https://us02web.zoom.us/j/85063950841?pwd=aGM5RDJqcThkNEp2NlkydmVCb1hBdz09",reply_markup=kb.week_keyboard)
            """2 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 2):
                await bot.send_message(message.from_user.id,
                                       "💥9:00 - 10:20💥\n"
                                       "Вступ до фаху(Лекція). Викладач - Мірутенко Л.В.\n"
                                       "Дати: (23.09, 07.10, 21.10, 04.11, 18.11)\n"
                                       "🌎Google Meet: https://meet.google.com/oiw-gogx-nxw\n\n"
                                       "💥10:30-11:50💥\n"
                                       "Вступ до університетських студій(лекція). Викладач - Левінець Р.П.\n"
                                       "Дати: з 23.09 до 9.12\n"
                                       "🌎Google Meet: https://meet.google.com/cwj-ugif-mhr?pli=1&authuser=1&hma=1&hmv=1\n\n"
                                       "💥12:10-13:30💥\n"
                                       "Англійська мова. Викладач - Костенко Д.В.\n"
                                       "Тарнавська Т.В. - intermediate\n"
                                       "Дати: -\n"
                                       "🌎Zoom(upper), https://us02web.zoom.us/j/83316091819?pwd=bDBoSm51amFkWHl4dEFnZlZ6THRtZz09\n"
                                       "Zoom(inter), https://us02web.zoom.us/j/85063950841?pwd=aGM5RDJqcThkNEp2NlkydmVCb1hBdz09\n\n"
                                       "\n"
                                       ""
                                       "💥13:40-15:00💥\n"
                                       "Англійська мова. Викладач - Костенко Д.В.\n"
                                       "Тарнавська Т.В. - intermediate\n"
                                       "Дати: -\n"
                                       "🌎Zoom(upper), https://us02web.zoom.us/j/83316091819?pwd=bDBoSm51amFkWHl4dEFnZlZ6THRtZz09\n"
                                       "Zoom(inter), https://us02web.zoom.us/j/85063950841?pwd=aGM5RDJqcThkNEp2NlkydmVCb1hBdz09",
                                       reply_markup=kb.week_keyboard)
    """Четверг"""
    if (message.text == kb.button_thursday_text):
        """КБ11"""
        if (db.check_group_head(message.from_user.id) == 11):
            """1 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 1):
                await bot.send_message(message.from_user.id, "💥9:00 - 10:20💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності(Лекція). Викладач - Мірутенко Л.В.\n"
                                                             "Дати: (17.09, 24.09, 01.10, 08.10, 15.10, 22.10, 29.10, 05.11, 12.11, 19.11, 26.11)\n"
                                                             "🌎Google Meet: https://meet.google.com/oiw-gogx-nxw\n\n"
                                                             "💥10:30-11:50💥\n"
                                                             "Англійська мова. Викладач - Каленченко О.О.(upper intermediate)\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper), Ідентифікатор конференції  778 9947 7903, пароль 5ZiZk2\n"
                                                             "Zoom(inter)https://us02web.zoom.us/j/82972158434?pwd=R2wxUC96Y0M4NVFTYlFSOHRPN3dSZz09   Ідентифікатор конференції: 829 7215 8434Пароль: 1Z7SaR\n\n"
                                                             "💥12:10-13:30💥\n"
                                                             "Англійська мова. Викладач - Каленченко О.О.(upper intermediate)\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper), Ідентифікатор конференції  778 9947 7903, пароль 5ZiZk2\n"
                                                             "Zoom(inter)https://us02web.zoom.us/j/82972158434?pwd=R2wxUC96Y0M4NVFTYlFSOHRPN3dSZz09   Ідентифікатор конференції: 829 7215 8434Пароль: 1Z7SaR\n\n",reply_markup=kb.week_keyboard)
            """2 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 2):
                await bot.send_message(message.from_user.id, "💥9:00 - 10:20💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності(Лекція). Викладач - Мірутенко Л.В.\n"
                                                             "Дати: (17.09, 24.09, 01.10, 08.10, 15.10, 22.10, 29.10, 05.11, 12.11, 19.11, 26.11)\n"
                                                             "🌎Google Meet: https://meet.google.com/oiw-gogx-nxw\n\n"
                                                             "💥10:30-11:50💥\n"
                                                             "Англійська мова. Викладач - Каленченко О.О.(upper intermediate)\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper), Ідентифікатор конференції  778 9947 7903, пароль 5ZiZk2\n"
                                                             "Zoom(inter)https://us02web.zoom.us/j/82972158434?pwd=R2wxUC96Y0M4NVFTYlFSOHRPN3dSZz09   Ідентифікатор конференції: 829 7215 8434Пароль: 1Z7SaR\n\n"
                                                             "💥12:10-13:30💥\n"
                                                             "Англійська мова. Викладач - Каленченко О.О.(upper intermediate)\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper), Ідентифікатор конференції  778 9947 7903, пароль 5ZiZk2\n"
                                                             "Zoom(inter)https://us02web.zoom.us/j/82972158434?pwd=R2wxUC96Y0M4NVFTYlFSOHRPN3dSZz09   Ідентифікатор конференції: 829 7215 8434Пароль: 1Z7SaR\n\n",reply_markup=kb.week_keyboard)
        """КБ12"""
        if (db.check_group_head(message.from_user.id) == 12):
            """1 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 1):
                await bot.send_message(message.from_user.id, "💥9:00 - 10:20💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності(Лекція). Викладач - Мірутенко Л.В.\n"
                                                             "Дати: (17.09, 24.09, 01.10, 08.10, 15.10, 22.10, 29.10, 05.11, 12.11, 19.11, 26.11)\n"
                                                             "🌎Google Meet: https://meet.google.com/oiw-gogx-nxw\n\n"
                                                             "💥10:30-11:50💥\n"
                                                             "Англійська мова. Викладач - Костенко Д.В.(upper intermediate)\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper): https://us02web.zoom.us/j/81061854473?pwd=aGVEMWVJSmptNFhPQUl0c2RoRWlsQT09\n"
                                                             "Zoom(inter): Посилання: https://us02web.zoom.us/j/82972158434?pwd=R2wxUC96Y0M4NVFTYlFSOHRPN3dSZz09   Ідентифікатор конференції: 829 7215 8434Пароль: 1Z7SaR\n\n"

                                                             "💥12:10-13:30💥\n"
                                                             "Англійська мова. Викладач - Костенко Д.В.(upper intermediate)\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper): https://us02web.zoom.us/j/81061854473?pwd=aGVEMWVJSmptNFhPQUl0c2RoRWlsQT09\n"
                                                             "Zoom(inter): Посилання: https://us02web.zoom.us/j/82972158434?pwd=R2wxUC96Y0M4NVFTYlFSOHRPN3dSZz09   Ідентифікатор конференції: 829 7215 8434Пароль: 1Z7SaR\n\n",reply_markup=kb.week_keyboard)
            """2 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 2):
                await bot.send_message(message.from_user.id,
                                       "💥9:00 - 10:20💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності(Лекція). Викладач - Мірутенко Л.В.\n"
                                                             "Дати: (17.09, 24.09, 01.10, 08.10, 15.10, 22.10, 29.10, 05.11, 12.11, 19.11, 26.11)\n"
                                                             "🌎Google Meet: https://meet.google.com/oiw-gogx-nxw\n\n"
                                                             "💥10:30-11:50💥\n"
                                                             "Англійська мова. Викладач - Костенко Д.В.(upper intermediate)\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper): https://us02web.zoom.us/j/81061854473?pwd=aGVEMWVJSmptNFhPQUl0c2RoRWlsQT09\n"
                                                             "Zoom(inter): Посилання: https://us02web.zoom.us/j/82972158434?pwd=R2wxUC96Y0M4NVFTYlFSOHRPN3dSZz09   Ідентифікатор конференції: 829 7215 8434Пароль: 1Z7SaR\n\n"

                                                             "💥12:10-13:30💥\n"
                                                             "Англійська мова. Викладач - Костенко Д.В.(upper intermediate)\n"
                                                             "Тарнавська Т.В. - intermediate\n"
                                                             "Дати: -\n"
                                                             "🌎Zoom(upper): https://us02web.zoom.us/j/81061854473?pwd=aGVEMWVJSmptNFhPQUl0c2RoRWlsQT09\n"
                                                             "Zoom(inter): Посилання: https://us02web.zoom.us/j/82972158434?pwd=R2wxUC96Y0M4NVFTYlFSOHRPN3dSZz09   Ідентифікатор конференції: 829 7215 8434Пароль: 1Z7SaR\n\n",reply_markup=kb.week_keyboard)
    """Пятница"""
    if (message.text == kb.button_friday_text):
        """КБ11"""
        if (db.check_group_head(message.from_user.id) == 11):
            """1 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 1):
                await bot.send_message(message.from_user.id, "💥9:00 - 10:20💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності(Практика). Викладач - Зюбіна Р.В.\n"
                                                             "Дати: (25.09, 02.10, 09.10, 16.10, 23.10, 30.10, 06.11, 13.11, 20.11, 27.11, 04.12, 11.12)\n"
                                                             "🌎Webex: https://meetingsemea27.webex.com/meetingsemea27/e.php?MTID=me15fdaa3c72be574e8069f6e2c60ae0d\n\n"
                                                             "💥10:30-11:50💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності. Викладач - Шестак Я.В.\n"
                                                             "Дати: (25.09, 02.10, 09.10, 16.10, 23.10, 30.10, 06.11, 13.11, 20.11)\n"
                                                             "🌎Zoom: https://us04web.zoom.us/j/72345701005?pwd=SDNRNTFVcS9uVXg3STljWGFSQlIxQT09\n\n"
                                                             "💥12:10-13:30💥\n"
                                                             "Вища математика. Викладач - Лукова-Чуйко Н.В.\n"
                                                             "Дати: (25.09, 02.10, 09.10, 16.10, 23.10, 30.10, 06.11, 13.11, 20.11, 01.12, 8.12)\n"
                                                             "🌎Посилання у Teams\n\n",reply_markup=kb.week_keyboard)
            """2 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 2):
                await bot.send_message(message.from_user.id,"💥9:00 - 10:20💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності(Практика). Викладач - Зюбіна Р.В.\n"
                                                             "Дати: (25.09, 02.10, 09.10, 16.10, 23.10, 30.10, 06.11, 13.11, 20.11, 27.11, 04.12, 11.12)\n"
                                                             "🌎Webex: https://meetingsemea27.webex.com/meetingsemea27/e.php?MTID=me15fdaa3c72be574e8069f6e2c60ae0d\n\n"
                                                             "💥10:30-11:50💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності. Викладач - Шестак Я.В.\n"
                                                             "Дати: (25.09, 02.10, 09.10, 16.10, 23.10, 30.10, 06.11, 13.11, 20.11)\n"
                                                             "🌎Zoom: https://us04web.zoom.us/j/72345701005?pwd=SDNRNTFVcS9uVXg3STljWGFSQlIxQT09\n\n"
                                                             "💥12:10-13:30💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності. Викладач - Шестак Я.В.\n"
                                                             "Дати: (18.09, 25.09, 02.10, 09.10, 16.10, 23.10, 30.10, 06.11, 13.11, 20.11)\n"
                                                             "🌎Zoom: https://us04web.zoom.us/j/78119405918?pwd=QUh5c0xReEhXcDdLdHlMd0prbmowQT09\n\n",reply_markup=kb.week_keyboard)
        """КБ12"""
        if (db.check_group_head(message.from_user.id) == 12):
            """1 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 1):
                await bot.send_message(message.from_user.id, "💥9:00 - 10:20💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності. Викладач - Шестак Я.В.\n"
                                                             "Дати: (25.09, 02.10, 09.10, 16.10, 23.10, 30.10, 06.11, 13.11, 20.11)\n"
                                                             "🌎Zoom https://us04web.zoom.us/j/75167614077?pwd=Tk9laHNuVXRkbHg2RHY5enJEelhjUT09\n\n"
                                                             "💥10:30-11:50💥\n"
                                                             "Вступ до фаху. Викладач - Зюбина Р.В.\n"
                                                             "Дати: (25.09, 02.10, 09.10, 16.10, 23.10, 30.10, 06.11, 13.11, 20.11, 27.11, 04.12, 11.12)\n"
                                                             "🌎Webex:  https://meetingsemea27.webex.com/meetingsemea27/e.php?MTID=me15fdaa3c72be574e8069f6e2c60ae0d\n\n"
                                                             "💥12:10-13:30💥\n"
                                                             "Вища математика. Викладач - Мірутенко Л.В.\n"
                                                             "Дати: (18.09,25.09, 02.10, 09.10,16.10, 23.10, 30.10, 06.11, 13.11, 20.11, 27.11,04.12, 11.12)\n"
                                                             "🌎Google Meet: https://meet.google.com/oiw-gogx-nxw\n\n",reply_markup=kb.week_keyboard)
            """2 подгруппа"""
            if (db.check_group_body(message.from_user.id) == 2):
                await bot.send_message(message.from_user.id,
                                       "💥9:00 - 10:20💥\n"
                                                             "Кіберпростір та протидія кіберзлочинності. Викладач - Шестак Я.В.\n"
                                                             "Дати: (25.09, 02.10, 09.10, 16.10, 23.10, 30.10, 06.11, 13.11, 20.11)\n"
                                                             "🌎Zoom https://us04web.zoom.us/j/75167614077?pwd=Tk9laHNuVXRkbHg2RHY5enJEelhjUT09\n\n"
                                                             "💥10:30-11:50💥\n"
                                                             "Вступ до фаху. Викладач - Зюбина Р.В.\n"
                                                             "Дати: (25.09, 02.10, 09.10, 16.10, 23.10, 30.10, 06.11, 13.11, 20.11, 27.11, 04.12, 11.12)\n"
                                                             "🌎Webex:  https://meetingsemea27.webex.com/meetingsemea27/e.php?MTID=me15fdaa3c72be574e8069f6e2c60ae0d\n\n"
                                                             "💥12:10-13:30💥\n"
                                                             "Вища математика. Викладач - Мірутенко Л.В.\n"
                                                             "Дати: (18.09,25.09, 02.10, 09.10,16.10, 23.10, 30.10, 06.11, 13.11, 20.11, 27.11,04.12, 11.12)\n"
                                                             "🌎Google Meet: https://meet.google.com/oiw-gogx-nxw\n\n",reply_markup=kb.week_keyboard)

    ##Просто лягушка
    if(message.text == kb.button_frog_text):
        await bot.send_sticker(message.from_user.id,"CAACAgQAAxkBAAEBT3ZfV3n3fxt7U49hO2Iphn_U1zj4sAACTAEAAqghIQZjKrRWscYWyBsE")
        await bot.send_message(message.from_user.id,"Ну и зачем ты нажал на эту кнопку...",reply_markup=kb.week_keyboard)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



