from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Импортируем созданные ранее файлы
from config import *
from keyboards import *
import texts


# --------------------------------------------------------#
# Ваш API токен
api = API
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
# --------------------------------------------------------#


# Обработчик команды start
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'✅ Добро пожаловать!\n\n' + texts.start, reply_markup=start_kb)

# Обработчик нажатия на кнопку "О нас"
@dp.message_handler(Text(equals=['ℹ️ О нас']))
async def about_us(message):
    await message.answer(texts.about_us, parse_mode='HTML', reply_markup=start_kb)

#Обработчик нажатия на кнопку "Цены"
@dp.message_handler(Text(equals=['📝 Цены']))
async def price(message):
    await message.answer('<b>Выберите интересующую вас услугу</b>', parse_mode='HTML', reply_markup=games_kb)

# Обработка кнопки "GTA 5"
@dp.callback_query_handler(text='GTA 5')
async def gta5(call):
    await call.message.answer(texts.game_gta5, parse_mode='HTML', reply_markup=buy_kb)
    await call.answer()

# Обработка кнопки "RDR 2"
@dp.callback_query_handler(text='RDR 2')
async def rdr2(call):
    await call.message.answer(texts.game_rdr2, parse_mode='HTML', reply_markup=buy_kb)
    await call.answer()

# Обработка кнопки "Sims 4"
@dp.callback_query_handler(text='Sims 4')
async def sims4(call):
    await call.message.answer(texts.game_sims4, parse_mode='HTML', reply_markup=buy_kb)
    await call.answer()

# Обработка кнопки "CS 2"
@dp.callback_query_handler(text='CS 2')
async def cs2(call):
    await call.message.answer(texts.game_cs2, parse_mode='HTML', reply_markup=buy_kb)
    await call.answer()

# Обработка кнопки "Battlefield 4"
@dp.callback_query_handler(text='Battlefield 4')
async def battlefield(call):
    await call.message.answer(texts.game_battlefield, parse_mode='HTML', reply_markup=buy_kb)
    await call.answer()

# Обработка кнопки "Atomic Heart"
@dp.callback_query_handler(text='Atomic Heart')
async def atomic_heart(call):
    await call.message.answer(texts.game_atomic_heart, parse_mode='HTML', reply_markup=buy_kb)
    await call.answer()

# Обработка кнопки "Cyberpunk"
@dp.callback_query_handler(text='Cyberpunk')
async def cyberpunk(call):
    await call.message.answer(texts.game_cyberpunk, parse_mode='HTML', reply_markup=buy_kb)
    await call.answer()

# Обработка кнопки "Roblox"
@dp.callback_query_handler(text='Roblox')
async def roblox(call):
    await call.message.answer(texts.game_roblox, parse_mode='HTML', reply_markup=buy_kb)
    await call.answer()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
