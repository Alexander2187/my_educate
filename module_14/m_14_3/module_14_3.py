"""
Цель: подготовить Telegram-бота для взаимодействия с базой данных.
Задача "Витамины для всех!":
"""

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#  token API
from my_new_0_bot.my_0_bot.tg_token import t

api = t
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

#
r_button_calculate = KeyboardButton(text="Рассчитать")
r_button_info = KeyboardButton(text="Информация")
r_button_buy = InlineKeyboardButton(text='Купить')

r_kb = ReplyKeyboardMarkup(resize_keyboard=True)
r_kb.row(r_button_calculate, r_button_info)
r_kb.add(r_button_buy)

#
i_button_calculate = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
i_button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')

i_kb = InlineKeyboardMarkup()
i_kb.row(i_button_calculate, i_button_formulas)

#
i_button_product_1 = InlineKeyboardButton(text='Product1', callback_data="product_buying")
i_button_product_2 = InlineKeyboardButton(text='Product2', callback_data="product_buying")
i_button_product_3 = InlineKeyboardButton(text='Product3', callback_data="product_buying")
i_button_product_4 = InlineKeyboardButton(text='Product4', callback_data="product_buying")

i_kb_buying = InlineKeyboardMarkup()
i_kb_buying.row(i_button_product_1, i_button_product_2, i_button_product_3, i_button_product_4)


class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=r_kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=i_kb)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer("Здесь должен быть какой-то очень информативный текст... \nНо его пока нет...")


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for num in range(1, 5):
        await message.answer(f'|\nProduct{num} | Описание: описание {num} | Цена: {num * 100}')
        with open(f'pictures_mp/{num}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=i_kb_buying)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5 \n'
                              'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161 ')


@dp.callback_query_handler(text='calories')
async def set_age(call):  # Возраст
    await call.message.answer('Введите свой возраст:')
    await UserStates.age.set()


@dp.message_handler(state=UserStates.age)
async def set_growth(message, state):  # Рост
    await state.update_data(age=float(message.text))
    await message.answer(f"Введите свой рост в см:")
    await UserStates.growth.set()


@dp.message_handler(state=UserStates.growth)
async def set_weight(message, state):  # Вес
    await state.update_data(growth=float(message.text))
    await message.answer(f"Введите свой вес в кг:")
    await UserStates.weight.set()


@dp.message_handler(state=UserStates.weight)
async def send_calories(message, state):  # Калории
    await state.update_data(weight=float(message.text))
    data = await state.get_data()
    # data may be saved
    men_calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
    women_calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] - 161
    await message.answer(f"Норма калорий для:\n"
                         f"мужчины: {men_calories}\n"
                         f"женщины: {women_calories}")
    # finish state
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
