from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📝 Прейскурант'),
            KeyboardButton(text='ℹ️ О нас')
        ],
    ], resize_keyboard=True
)


catalog_kb = InlineKeyboardMarkup(
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
            InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_preiskurant"),
        ],
    ]
)


AdminPanel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👥 Пользователи", callback_data="users"),
        ],
        [
            InlineKeyboardButton(text="📊 Статистика", callback_data="statistick"),
        ],
        [
            InlineKeyboardButton(text="✉️ Рассылка", callback_data="mailing"),
        ],
        [
            InlineKeyboardButton(text="❌ Блокировка", callback_data="block"),
        ],
    ]
)

back_to_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_admin"),
        ],
    ]
)
