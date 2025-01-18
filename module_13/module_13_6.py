"""
'Инлайн клавиатуры'
module_13_6.py
"""
"""
Упрощенный вариант формулы Миффлина-Сан Жеора:
для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.
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

r_button_calculate = KeyboardButton(text="Рассчитать")
r_button_info = KeyboardButton(text="Информация")
r_kb = ReplyKeyboardMarkup(resize_keyboard=True)
r_kb.row(r_button_calculate, r_button_info)

i_button_calculate = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
i_button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
i_kb = InlineKeyboardMarkup()
i_kb.row(i_button_calculate, i_button_formulas)


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
