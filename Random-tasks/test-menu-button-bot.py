from aiogram import Bot, Dispatcher, types
import json
import os
import asyncio

from aiogram.client.default import DefaultBotProperties

import asyncio
import logging

# Вставьте свой токен
API_TOKEN = '6846539746:AAF34NjOx5-srspWsgULStcCwWfMAp_JADE'


default = DefaultBotProperties(parse_mode='HTML')

# Создаем объект бота и диспетчера
bot = Bot(token=API_TOKEN, default=default)

dp = Dispatcher()


async def set_bot_commands():
    # Получаем путь к директории, в которой находится скрипт
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Путь к JSON-файлу
    json_path = os.path.join(script_dir, 'bot_commands.json')
    
    with open(json_path, 'r', encoding='utf-8') as file:
        commands = json.load(file)

    await bot.set_my_commands([types.BotCommand(**cmd) for cmd in commands])


async def main():
    await set_bot_commands()

    # Очищаем состояния и удаляем необработанные до запуска функции maim() апдейты
    await bot.delete_webhook(drop_pending_updates=True)
    # Запускаем бота
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG)
    
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Бот остановлен')