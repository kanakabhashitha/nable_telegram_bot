from typing import Final
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6708571176:AAFo8UrI5FHY9VkRZq4usyqHOcLJgl_qvTs'
BOT_USERNAME: Final = '@nablesupport_bot'

# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting me! I am a N*able support assistant')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messages = [
        'I am a N*able support assistant!',
        'Please type below services category then I can help you.',
        '1. IoT',
        '2. Network',
        '3. Agility',
        '4. System'
    ]

    for message in messages:
        await asyncio.sleep(1)  
        await update.message.reply_text(message)

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is custom command')

# Responses

def handel_responses(text:str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return "Hey there!"
    
    if 'how are you' in processed:
        return "I am good!"
    
    if 'iot' in processed:
        return "IoT (Internet of Things):Nable's IoT services empower your business with seamless connectivity and intelligent data insights. Harness the power of connected devices to enhance efficiency, monitor assets in real-time, and unlock new possibilities for automation."
    
    if 'network' in processed:
        return "Network Solutions:Elevate your network infrastructure with Nable's cutting-edge solutions. We provide robust and scalable network architectures, ensuring secure and efficient communication. Experience enhanced connectivity, reduced downtime, and optimized performance for your business operations."
    
    if 'agility' in processed:
        return "Agility Services:Nable's Agility services redefine the way your business adapts to change. Embrace flexibility and responsiveness with agile methodologies. Our solutions empower you to quickly pivot, innovate, and stay ahead in today's dynamic business landscape."
    
    if 'system' in processed:
        return "System Optimization:Optimize your systems with Nable's expertise. From streamlining processes to improving resource utilization, our System Optimization services ensure your IT infrastructure performs at its peak. Enhance reliability, reduce bottlenecks, and achieve maximum efficiency."

    return 'I do not understand what you wrote...'

async def handel_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type} : "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handel_responses(new_text)
        else:
            return
        
    else:
        response: str = handel_responses(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # message
    app.add_handler(MessageHandler(filters.TEXT, handel_message))

    # errors
    app.add_error_handler(error)

    # polls the bot
    print('Polling bot...')
    app.run_polling(poll_interval=3)