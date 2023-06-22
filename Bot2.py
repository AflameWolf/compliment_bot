import logging
import os
import time
from aiogram import Bot, Dispatcher, executor, types
import DB


logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("BOTAPI"))
dp = Dispatcher(bot)



"""Клиентская часть"""
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Запуск бота")
    user_id = message.from_user.id
    while True:
        send = DB.mongo_find_and_update({"not_told": "true"}, {"not_told": "folse"})
        if send != None:
            await bot.send_message(user_id, send["compliment"])
        else:
            await bot.send_message(user_id, "Кажется у меня закончились комплименты")
            print("Кажется у меня закончились комплименты")
            break
        time.sleep(3600)
# """ Запуск """
# executor.start_polling(dp, skip_updates=True)
