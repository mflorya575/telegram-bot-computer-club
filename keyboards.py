from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📝 Цены'),
            KeyboardButton(text='ℹ️ О нас')
        ],
    ], resize_keyboard=True
)


games_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='GTA 5', callback_data='GTA 5'),
        ],
        [
            InlineKeyboardButton(text='RDR 2', callback_data='RDR 2'),
        ],
        [
            InlineKeyboardButton(text='Sims 4', callback_data='Sims 4'),
        ],
        [
            InlineKeyboardButton(text='Battlefield 4', callback_data='Battlefield 4'),
        ],
        [
            InlineKeyboardButton(text='Atomic Heart', callback_data='Atomic Heart'),
        ],
        [
            InlineKeyboardButton(text='Cyberpunk', callback_data='Cyberpunk'),
        ],
        [
            InlineKeyboardButton(text='Roblox', callback_data='Roblox'),
        ],
    ]
)


buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛍 Купить", url="https://t.me/jlosos1856"),
        ],
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data="price"),
        ],
    ]
)


# Инлайн клавиатура администратора
admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨‍👩‍👦‍👦 Пользователи", callback_data="users"),
        ],
        [
            InlineKeyboardButton(text="📊 Статистика", callback_data="statistics"),
        ],
        [
            InlineKeyboardButton(text="⛔️ Блокировка", callback_data="block_user"),
            InlineKeyboardButton(text="✅ Разблокировка", callback_data="unlock_user"),
        ],
    ]
)
