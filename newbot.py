import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command


# 1.Токен
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


# 2.Обработка Start сообшений
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Отправь свое ФИО и я пришлю тебе его транслитом'
    logging.info(f'{user_name} {user_id} {text} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)


TRANSLIT_DICT = {
    'А': 'A', 'а': 'a',
    'Б': 'B', 'б': 'b',
    'В': 'V', 'в': 'v',
    'Г': 'G', 'г': 'g',
    'Д': 'D', 'д': 'd',
    'Е': 'E', 'е': 'e',
    'Ё': 'E', 'ё': 'e',
    'Ж': 'Zh', 'ж': 'zh',
    'З': 'Z', 'з': 'z',
    'И': 'I', 'и': 'i',
    'Й': 'Y', 'й': 'y',
    'К': 'K', 'к': 'k',
    'Л': 'L', 'л': 'l',
    'М': 'M', 'м': 'm',
    'Н': 'N', 'н': 'n',
    'О': 'O', 'о': 'o',
    'П': 'P', 'п': 'p',
    'Р': 'R', 'р': 'r',
    'С': 'S', 'с': 's',
    'Т': 'T', 'т': 't',
    'У': 'U', 'у': 'u',
    'Ф': 'F', 'ф': 'f',
    'Х': 'Kh', 'х': 'kh',
    'Ц': 'Ts', 'ц': 'ts',
    'Ч': 'Ch', 'ч': 'ch',
    'Ш': 'Sh', 'ш': 'sh',
    'Щ': 'Shch', 'щ': 'shch',
    'Ъ': '', 'ъ': '',
    'Ы': 'Y', 'ы': 'y',
    'Ь': '', 'ь': '',
    'Э': 'E', 'э': 'e',
    'Ю': 'Yu', 'ю': 'yu',
    'Я': 'Ya', 'я': 'ya'
}


# Функция транскрипции
def transliterate(text: str) -> str:
    result = []
    for char in text:
        translit_char = TRANSLIT_DICT.get(char, char)
        result.append(translit_char)
    return ''.join(result)


# 3.Обработка всех сообщений   
@dp.message()
async def send_fullname(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    fullname_cyrillic = message.text.strip()
    fullname_translete = transliterate(fullname_cyrillic)
    logging.info(f'{user_name} {user_id} прислал: {fullname_cyrillic}')
    logging.info(f'Отправлено {fullname_translete}')
    await message.answer(text=f'ФИО на латыне:\n{fullname_translete}')

# 4.Пуллинг
if __name__ == '__main__':
    dp.run_polling(bot)
