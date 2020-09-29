from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

"""Дни недели"""
button_monday_text = "Понедельник"
button_tuesday_text = "Вторник"
button_wednesday_text = "Среда"
button_thursday_text = "Четверг"
button_friday_text = "Пятница"

button_monday = KeyboardButton(button_monday_text)
button_tuesday = KeyboardButton(button_tuesday_text)
button_wednesday = KeyboardButton(button_wednesday_text)
button_thursday = KeyboardButton(button_thursday_text)
button_friday = KeyboardButton(button_friday_text)
"""Дни недели"""

button_frog_text = "Стикер с лягушкой"

button_frog = KeyboardButton(button_frog_text)



""""""
button_1_head_text = "11 группа"
button_2_head_text = "12 группа"

button_1_head = KeyboardButton(button_1_head_text)
button_2_head = KeyboardButton(button_2_head_text)

button_1_body_text = "1 подгруппа"
button_2_body_text = "2 подгруппа"

button_1_body = KeyboardButton(button_1_body_text)
button_2_body = KeyboardButton(button_2_body_text)

week_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_monday).add(button_tuesday).add(button_wednesday).add(button_thursday).add(button_friday).add(button_frog)
group_head_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1_head).add(button_2_head)
group_body_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1_body).add(button_2_body)
""""""