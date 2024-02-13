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
from utils import *
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
    text = "Текст с использованием ссылки \-ок"
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



# список id людей, которые будут иметь доступ к панели администратора
admins = [504997812, 1046276866]

# Добавляем новую команду /admin
@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):

    # Проверяем есть ли айди пользователя в списке admins
    if message.from_user.id in admins:

        # Если есть, то открываем панель
        await message.answer("Вы открыли панель администратора", parse_mode="HTML", reply_markup=admin_panel)

    else:

        # Если нет, то говорим об этом
        await message.answer("Вы не администратор", parse_mode="HTML", reply_markup=None)

# Обработка кнопки "👨‍👩‍👦‍👦 Пользователи"
@dp.callback_query_handler(text="users")
async def users(call: types.CallbackQuery):

    # Вызываем написанную ранее функцию, которая возвращает строку с выводом пользователей бота
    await call.message.answer(show_users())

    await call.answer()

# Обработка кнопки "📊 Статистика"
@dp.callback_query_handler(text="statistics")
async def statistics(call: types.CallbackQuery):

    # Вызываем написанную ранее функцию, которая возвращает количество пользователей
    await call.message.answer(f"Количество пользователей: {show_statistics()}")

    await call.answer()

# Создадим машину состояний
class UserState(StatesGroup):
    id = State()

# Обработчик кнопки "⛔️ Блокировка"
@dp.callback_query_handler(text="block_user")
async def block_user(call: types.CallbackQuery):

    # Просим ввести id пользователя для блокировки
    await call.message.answer(f"Введите id пользователя для блокировки")

    # Запоминаем ответ пользователя
    await UserState.id.set()

    await call.answer()


# Обработчик введённого администратором id
@dp.message_handler(state=UserState.id)
async def fsm_handler(message: types.Message, state: FSMContext):

    # Получаем введённое пользователем сообщение
    input_id = message.text

    # Вызываем функцию для блокировки
    add_user_to_block(input_id)

    # Отвечаем, что пользователь был заблокирован
    await message.answer(f"Пользователь с id: {input_id}, был заблокирован")

    # Закрываем машину состояний
    await state.finish()

#Обработчик кнопки "✅ Разблокировка"
@dp.callback_query_handler(text="unlock_user")
async def unlock_user(call: types.CallbackQuery):

    #Просим ввести id пользователя
    await call.message.answer(f"Введите id пользователя для разблокировки")

    #Запоминаем в машину состояний
    await UserState.id.set()

    await call.answer()


# Обработчик введённого администратором id
@dp.message_handler(state=UserState.id)
async def fsm_handler(message: types.Message, state: FSMContext):

    # Получаем введённое пользователем сообщение
    input_id = message.text

    # Вызывааем функцию для разблокировки
    unlock_users(input_id)

    # Сообщаем об успешной разблокировке
    await message.answer(f"Пользователь с id: {input_id}, был разблокирован")

    # Закрываем машину состояний
    await state.finish()






# Декоратор
def check_user_in_block(user_id):
    pass


@dp.message_handler()
async def repeat(message: types.Message):

    # Получаем id пользователя, который отправил сообщение
    user_id = int(message.from_user.id)

    #Передаём id в функцию для проверки.
    #Если статус пользователя 1, то ...
    if check_user_in_block(user_id) == 1:
        await message.answer("Вы были заблокированы")

    #Если статус пользователя 0, то просто что-нибудь отправляем
    else:
        await message.answer("Продолжайте пользоваться ботом", reply_markup=None)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
