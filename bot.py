#Установите необходимые библиотеки
# pip install -U freeGPT
# pip install python-telegram-bot

from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Bot
from freeGPT import Client

# Ключи бота
bot_key = 'тут ключ от вашего бота'
bot = Bot(token=bot_key)
print('running the bot...')

####################       КОМАНДЫ /start  #######################################

async def start(update, context):
    await update.message.reply_text('тут текст команды старт')
    
#####################    ОСНОВНАЯ ФУНКЦИЯ     ####################################
    
async def ask(update, context):
    try:
        otvet = Client.create_completion("gpt3_5", update.message.text)
     
    except Exception as e:
        await update.message.reply_text('что-то пошло не так. попробуйте позже')
        print(e)
        return
    await update.message.reply_text(otvet)
            
##################  КОНЕЦ ОСНОВНОЙ ФУНКЦИИ   ####################################
# Запуск бота
if __name__ == '__main__':
    application = Application.builder().token(bot_key).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ask))
    application.run_polling(1.0)
