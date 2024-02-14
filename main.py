import aiogram
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InputMediaPhoto

import config
import database


api = config.API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


import handlers.Start
import handlers.Category
import handlers.Admin


dp.message_handler(lambda m: database.check_block(m.from_user.id))(handlers.Start.ban_message)
dp.callback_query_handler(lambda c: database.check_block(c.from_user.id))(handlers.Start.ban_callbackquery)

dp.message_handler(commands=['start'])(handlers.Start.start)
dp.message_handler(Text(equals=['ℹ️ О нас']))(handlers.Start.about_as)

dp.message_handler(Text(equals=['📝 Каталог']))(handlers.Category.costs)
dp.callback_query_handler(text='GTA 5')(handlers.Category.gta5)
dp.callback_query_handler(text='RDR 2')(handlers.Category.rdr2)
dp.callback_query_handler(text='Sims 4')(handlers.Category.sims4)
dp.callback_query_handler(text='Battlefield 4')(handlers.Category.battlefield4)
dp.callback_query_handler(text='Atomic Heart')(handlers.Category.atomic_heart)
dp.callback_query_handler(text='Cyberpunk')(handlers.Category.cyberpunk)
dp.callback_query_handler(text='Roblox')(handlers.Category.roblox)
dp.callback_query_handler(text='Другие предложения')(handlers.Category.other)
dp.callback_query_handler(text='back_to_preiskurant')(handlers.Category.back)

dp.message_handler(commands=['admin'])(handlers.Admin.start)
dp.callback_query_handler(text="statistick")(handlers.Admin.statistick)
dp.callback_query_handler(text="users")(handlers.Admin.users)
dp.callback_query_handler(text="mailing")(handlers.Admin.mailing)
dp.message_handler(state=handlers.Admin.admins.mailing_step1)(handlers.Admin.mailing1)
dp.message_handler(content_types=types.ContentTypes.PHOTO, state=handlers.Admin.admins.mailing_step2)(handlers.Admin.mailing2)
dp.callback_query_handler(text="block")(handlers.Admin.block)
dp.message_handler(state=handlers.Admin.admins.ban)(handlers.Admin.ban1)
dp.callback_query_handler(text="back_to_admin")(handlers.Admin.back_admin)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
