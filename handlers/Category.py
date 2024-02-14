from aiogram.types import InputMediaPhoto

import texts.category
from keyboards import *


async def costs(message):
    with open('files/media/info.jpg', "rb") as img:
        await message.answer_photo(img, '<b>Выберите интересующую вас услугу</b>',
                                   parse_mode='HTML', reply_markup=catalog_kb)


async def gta5(call):
    with open('files/media/manikur.jpg', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.game_gta5, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def rdr2(call):
    with open('files/media/pedikur.jpg', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.game_rdr2, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def sims4(call):
    with open('files/media/narast.png', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.game_sims4, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()

async def battlefield4(call):
    with open('files/media/narast.png', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.game_battlefield, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()

async def atomic_heart(call):
    with open('files/media/narast.png', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.game_atomic_heart, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()

async def cyberpunk(call):
    with open('files/media/narast.png', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.game_cyberpunk, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()

async def roblox(call):
    with open('files/media/narast.png', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.game_roblox, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()

async def other(call):
    with open('files/media/other.png', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.other, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def back(call):
    with open('files/media/info.jpg', "rb") as img:
        mes = InputMediaPhoto(media=img, caption='<b>Выберите интересующую вас услугу</b>', parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=catalog_kb)
    await call.answer()
