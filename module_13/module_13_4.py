"""
'Машина состояний'
module_13_4.py
"""
"""
Упрощенный вариант формулы Миффлина-Сан Жеора:
для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.
"""

import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

#  token API
from my_new_0_bot.my_0_bot.tg_token import t

api = t
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=['Calories'])  # Возраст
async def set_age(message):
    await message.answer('Введите свой возраст:')
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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)