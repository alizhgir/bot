import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart
from config import TOKEN

dp = Dispatcher()

transliteration_dict = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ъ': 'IE', 
    'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'а': 'a', 'б': 'b', 'в': 'v',
    'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i',
    'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 
    'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ъ': 'ie', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia'
}

def transliterate(text: str) -> str:
    return ''.join(transliteration_dict.get(char, char) for char in text)

@dp.message(CommandStart())
async def send_welcome(message: Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    logging.info(f'{user_name=} {user_id=} sent message:{message.text}')
    text = f'Привет, {user_name}! Я произведу транслитерацию для тебя. Присылай данные :)'
    await message.reply(text)

@dp.message()
async def echo_handler(message: Message):
    await message.reply(transliterate(message.text))

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
