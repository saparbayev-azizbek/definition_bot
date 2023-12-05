from defenation import diction
from googletrans import Translator
from aiogram import types, Bot, Dispatcher, executor


token = '6409037275:AAHUbS5I0hnR0avb1DiQ3dyeGKekvbqNJTE'
bot = Bot(token=token)
dp = Dispatcher(bot=bot)

def tarjimon(text):
    tarjima = Translator()
    resp = tarjima.translate(text=text, dest='uz', src='auto')
    return resp.text

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer('Assalomu alaykum')

@dp.message_handler()
async def definition(message: types.Message):

    if diction(message.text):
        res = diction(message.text)
        await message.answer(f"Definition of {message.text} is :\n{res['definitions']}\n")
    else:
        matn = tarjimon(message.text)
        await message.answer(f'{matn}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
