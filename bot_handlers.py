from main import bot # Импортируем объект бота
from telebot import types
import random
import uuid
import time
from messages import * # Инмпортируем все с файла сообщений


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("💊Ассортимент")
    btn2 = types.KeyboardButton("💰Работа")
    btn3 = types.KeyboardButton("👨‍💻Поддержка")
    markup.add(btn1, btn2)
    markup.add(btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Ты находишься в шопе качественного стаффа. В настоящее время работаем только по РУ.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "💊Ассортимент"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Москва")
        btn2 = types.KeyboardButton("СПБ")
        btn3 = types.KeyboardButton("Новосибирск")
        btn4 = types.KeyboardButton("Екатеринбург")
        btn5 = types.KeyboardButton("Казань")
        btn6 = types.KeyboardButton("Челябинск")
        btn7 = types.KeyboardButton("Омск")
        btn8 = types.KeyboardButton("Воронеж")
        btn9 = types.KeyboardButton("Нижний Новгород")
        btn10 = types.KeyboardButton("Самара")
        btn11 = types.KeyboardButton("Пермь")
        btn12 = types.KeyboardButton("Петрозаводск")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
        markup.add(btn7, btn8)
        markup.add(btn9, btn10)
        markup.add(btn11, btn12)
        markup.add(back)
        bot.send_message(message.chat.id, text="Выбери Ваш регион:", reply_markup=markup)

    elif (message.text == "AlphaPVP"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("0.3г - 500руб")
        btn2 = types.KeyboardButton("0.5г - 700руб")
        btn3 = types.KeyboardButton("1г - 1000руб")
        btn4 = types.KeyboardButton("2г - 1700руб")
        btn5 = types.KeyboardButton("5г - 3700руб")
        btn6 = types.KeyboardButton("10г - 6000руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
        markup.add(back)
        bot.send_message(message.chat.id, "Выберите вес:", reply_markup=markup)
    elif (message.text == "Мефедрон"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("1г - 1100руб")
        btn4 = types.KeyboardButton("2г - 1800руб")
        btn5 = types.KeyboardButton("5г - 3800руб")
        btn6 = types.KeyboardButton("10г - 6200руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
        markup.add(back)
        bot.send_message(message.chat.id, "Выберите вес:", reply_markup=markup)
    elif (message.text == "LSD-25"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("2 марки - 3000руб")
        btn4 = types.KeyboardButton("5 марок - 6000руб")
        btn5 = types.KeyboardButton("10 марок - 10000руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3)
        markup.add(btn4)
        markup.add(btn5)
        markup.add(back)
        bot.send_message(message.chat.id, "Выберите вес:", reply_markup=markup)
    elif (message.text == "Кокаин(50-60%)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("1г - 5000руб")
        btn4 = types.KeyboardButton("2г - 9000руб")
        btn5 = types.KeyboardButton("5г - 20000руб")
        btn6 = types.KeyboardButton("10г - 37000руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
        markup.add(back)
        bot.send_message(message.chat.id, "Выберите вес:", reply_markup=markup)
    elif (message.text == "Метадон"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("1г - 3500руб")
        btn4 = types.KeyboardButton("2г - 6900руб")
        btn5 = types.KeyboardButton("5г - 14000руб")
        btn6 = types.KeyboardButton("10г - 26000руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
        markup.add(back)
        bot.send_message(message.chat.id, "Выберите вес:", reply_markup=markup)
    elif (message.text == "Метамфетамин(Рацемат Гидрохлорид)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("1г - 1500руб")
        btn4 = types.KeyboardButton("2г - 2800руб")
        btn5 = types.KeyboardButton("5г - 5600руб")
        btn6 = types.KeyboardButton("10г - 10000руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
        markup.add(back)
        bot.send_message(message.chat.id, "Выберите вес:", reply_markup=markup)

    elif (message.text == "Амфетамин"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("0.3г - 400руб")
        btn2 = types.KeyboardButton("0.5г - 600руб")
        btn3 = types.KeyboardButton("1г - 900руб")
        btn4 = types.KeyboardButton("2г - 1600руб")
        btn5 = types.KeyboardButton("5г - 3500руб")
        btn6 = types.KeyboardButton("10г - 5500руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
        markup.add(back)
        bot.send_message(message.chat.id, "Выберите вес:", reply_markup=markup)
    elif (message.text == "Гашиш(Las-Vegas)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("1г - 400руб")
        btn4 = types.KeyboardButton("2г - 800руб")
        btn5 = types.KeyboardButton("5г - 1600руб")
        btn6 = types.KeyboardButton("10г - 2800руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
        markup.add(back)
        bot.send_message(message.chat.id, "Выберите вес:", reply_markup=markup)
    elif (message.text == "0.3г - 500руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: AlphaPVP\nВес: 0,3г \nСумма к оплате: 500руб", reply_markup=markup)
        bot.send_message(message.chat.id, "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,0004 BTC*", reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id, f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ", reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id, "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",reply_markup=markup)
    elif (message.text == "0.5г - 700руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: AlphaPVP\nВес: 0,5г \nСумма к оплате: 700руб", reply_markup=markup)
        bot.send_message(message.chat.id, "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00056 BTC*", reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id, f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ", reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id, "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",reply_markup=markup)
    elif (message.text == "1г - 1000руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: AlphaPVP\nВес: 1г \nСумма к оплате: 1000руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,0008 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "2г - 1700руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: AlphaPVP\nВес: 2г \nСумма к оплате: 1700руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00136 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "5г - 3700руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: AlphaPVP\nВес: 5г \nСумма к оплате: 3700руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00297 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "10г - 6000руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: AlphaPVP\nВес: 10г \nСумма к оплате: 6000руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,0048 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "0.3г - 400руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Амфетамин\nВес: 0,3г \nСумма к оплате: 400руб", reply_markup=markup)
        bot.send_message(message.chat.id, "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00033 BTC*", reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id, f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ", reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id, "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",reply_markup=markup)
    elif (message.text == "0.5г - 600руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Амфетамин\nВес: 0,5г \nСумма к оплате: 600руб", reply_markup=markup)
        bot.send_message(message.chat.id, "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00048 BTC*", reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id, f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ", reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id, "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",reply_markup=markup)
    elif (message.text == "1г - 900руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Амфетамин\nВес: 1г \nСумма к оплате: 900руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00072 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "2г - 1600руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Амфетамин\nВес: 2г \nСумма к оплате: 1600руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00128 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "5г - 3500руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Амфетамин\nВес: 5г \nСумма к оплате: 3500руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,0028 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "10г - 5500руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Амфетамин\nВес: 10г \nСумма к оплате: 5500руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00441 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "1г - 1100руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Мефедрон\nВес: 1г \nСумма к оплате: 1100руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00088 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "2г - 1800руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Мефедрон\nВес: 2г \nСумма к оплате: 1800руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00144 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "5г - 3800руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Мефедрон\nВес: 5г \nСумма к оплате: 3800руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,003 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "10г - 6200руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Мефедрон\nВес: 10г \nСумма к оплате: 6200руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,005 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "1г - 400руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Гашиш\nВес: 1г \nСумма к оплате: 400руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00032 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "2г - 800руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Гашиш\nВес: 2г \nСумма к оплате: 800руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00064 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "5г - 1600руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Гашиш\nВес: 5г \nСумма к оплате: 1600руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00128 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "10г - 2800руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Гашиш\nВес: 10г \nСумма к оплате: 2800руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,002245 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)

    elif (message.text == "1г - 1500руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Метамфетамин(Рацемат Гидрохлорид)\nВес: 1г \nСумма к оплате: 1500руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,0012 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "2г - 2800руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Метамфетамин(Рацемат Гидрохлорид)\nВес: 2г \nСумма к оплате: 2800руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00224 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "5г - 5600руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Метамфетамин(Рацемат Гидрохлорид)\nВес: 5г \nСумма к оплате: 5600руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00448 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "10г - 10000руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Метамфетамин(Рацемат Гидрохлорид)\nВес: 10г \nСумма к оплате: 10000руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,008 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "1г - 3500руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Метадон\nВес: 1г \nСумма к оплате: 3500руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,0028 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "2г - 6900руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Метадон\nВес: 2г \nСумма к оплате: 6900руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00553 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "5г - 14000руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Метадон\nВес: 5г \nСумма к оплате: 14000руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,001123 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "10г - 26000руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Метадон\nВес: 10г \nСумма к оплате: 26000руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,02 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "1г - 5000руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Кокаин(50-60%)\nВес: 1г \nСумма к оплате: 5000руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,004 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "2г - 9000руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Кокаин(50-60%)\nВес: 2г \nСумма к оплате: 9000руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,0072 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "5г - 20000руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Кокаин(50-60%)\nВес: 5г \nСумма к оплате: 20000руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,016 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "10г - 37000руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: Кокаин(50-60%)\nВес: 10г \nСумма к оплате: 37000руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,0297 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "2 марки - 3000руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: LSD-25\nКоличество: 2 марки \nСумма к оплате: 3000руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,0024 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "5 марок - 6000руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: LSD-25\nКоличество: 5 марок \nСумма к оплате: 6000руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,00481 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "10 марок - 10000руб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Товар: LSD-25\nКоличество: 10 марок \nСумма к оплате: 10000руб", reply_markup=markup)
        bot.send_message(message.chat.id,
                         "Внимание!\nОплата принимается только в BTC, по фиксированному курсу магазина! \n\nНынешний курс: 1 BTC = 20 000$\n\n*К оплате: 0,008 BTC*",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         f"🪙Номер счета для оплаты:\n*bc1qyzgze89skq9kmnkgajnnwlvkgjx9dd5ztt69f3*\n\nПополните данный счет ИМЕННО той суммой, которая Вам указана, указав в описании платежа: {uuid.uuid4().hex} ",
                         reply_markup=markup, parse_mode="Markdown")
        bot.send_message(message.chat.id,
                         "После осуществления платежа нажмите кнопку ОПЛАТИЛ, для подтверждения получения средств\nВнимание! Обработка Bitcoin платежа может занимать до 30-ти минут. Имейте терпение и не связывайтесь с саппортом в первые 30 минут после перевода средств.",
                         reply_markup=markup)
    elif (message.text == "👌ОПЛАТИЛ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👌ОПЛАТИЛ")
        btn2 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "🔎Проверка платежа...ожидайте", reply_markup=markup)
        time.sleep(5)
        bot.send_message(message.chat.id, "🤷‍♂Ваш платеж отсутствует в настоящий момент.\nПопробуйте проверить платеж снова, через несколько минут.", reply_markup=markup)
    elif (message.text == "Москва" or message.text == "СПБ" or message.text == "Петрозаводск" or message.text == "Челябинск" or message.text == "Новосибирск"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("AlphaPVP")
        btn2 = types.KeyboardButton("Амфетамин")
        btn3 = types.KeyboardButton("Кокаин(50-60%)")
        btn4 = types.KeyboardButton("Мефедрон")
        btn5 = types.KeyboardButton("Гашиш(Las-Vegas)")
        btn6 = types.KeyboardButton("LSD-25")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
        markup.add(back)
        bot.send_message(message.chat.id, text="Внимание! Клады находятся в пределах города, в любой точке! Район указать нельзя!\nВ вашем регионе в наличии:", reply_markup=markup)

    elif (message.text == "Омск" or message.text == "Екатеринбург" or message.text == "Казань" or message.text == "Воронеж" or message.text == "Нижний Новгород"or message.text == "Самара" or message.text == "Пермь"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("AlphaPVP")
        btn2 = types.KeyboardButton("Амфетамин")
        btn3 = types.KeyboardButton("Мефедрон")
        btn4 = types.KeyboardButton("Метамфетамин(Рацемат Гидрохлорид)")
        btn5 = types.KeyboardButton("Гашиш(Las-Vegas)")
        btn6 = types.KeyboardButton("Метадон")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2)
        markup.add(btn4)
        markup.add(btn6)
        markup.add(btn3, btn5)
        markup.add(back)
        bot.send_message(message.chat.id, text="Внимание! Клады находятся в пределах города, в любой точке! Район указать нельзя!\nВ вашем регионе в наличии:", reply_markup=markup)
    elif (message.text == "AlphaPVP"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("0.3г - 500руб")
        btn2 = types.KeyboardButton("0.5г - 700руб")
        btn3 = types.KeyboardButton("1г - 1000руб")
        btn4 = types.KeyboardButton("2г - 1700руб")
        btn5 = types.KeyboardButton("5г - 3600руб")
        btn6 = types.KeyboardButton("10г - 6000руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
        markup.add(back)
        bot.send_message(message.chat.id, "Выберите вес:", reply_markup=markup)
    elif (message.text == "👨‍💻Поддержка"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("💊Ассортимент")
        btn2 = types.KeyboardButton("💰Работа")
        btn3 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        markup.add(btn3)
        bot.send_message(message.chat.id, text="Саппорт: @pleasureshopsupport", reply_markup=markup)
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("💊Ассортимент")
        btn2 = types.KeyboardButton("💰Работа")
        btn3 = types.KeyboardButton("👨‍💻Поддержка")
        markup.add(btn1, btn2)
        markup.add(btn3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован...\nНапишите /start для повторного запуска бота.")

bot.polling(none_stop=True)
