from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
TOKEN: final = '6315213331:AAEDg0Vg0x0COQBd2_fS2xzkMKs0Y119EWI'
BOT_USERNAME: final = '@asmaa03_bot'
# pip install
# commands

async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am a history of Palestine bot that provides information about (1981-1995). Let\'s start now!')

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text('If you are facing a problem, please! use these it may help you! ')

async def palestine_1981_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1981:\n"
        "/info81 for news, battles, or massacres\n"
        "/characters81 for characters or Martyrs\n")

async def info81_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1981: ي عام 1981 ضمت إسرائيل القدس الشرقية وهضبة الجولان كجزءٍ من الدولة الإسرائيلية ضمّاً أحاديَ الجانب لم يعترف به المجتمع الدولي، أما بقية الضفة الغربية بالإضافة إلى كامل قطاع غزة فبقيت خاضعةً للحكم العسكري.")

async def characters81_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1981: [List the battles]")



async def palestine_1982_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1981:\n"
        "/info82 for news, battles, or massacres\n"
        "/characters82 for characters or Martyrs\n")

async def info82_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1982:\n https://ar.wikipedia.org/wiki/%D9%85%D8%AC%D8%B2%D8%B1%D8%A9_%D8%B5%D8%A8%D8%B1%D8%A7_%D9%88%D8%B4%D8%A7%D8%AA%D9%8A%D9%84%D8%A7\n  https://ar.wikipedia.org/wiki/%D9%85%D8%AC%D8%B2%D8%B1%D8%A9_%D8%B5%D8%A8%D8%B1%D8%A7_%D9%88%D8%B4%D8%A7%D8%AA%D9%8A%D9%84%D8%A7\n")

async def characters82_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1982:\n https://ar.wikipedia.org/wiki/%D9%85%D8%AC%D8%B2%D8%B1%D8%A9_%D8%B5%D8%A8%D8%B1%D8%A7_%D9%88%D8%B4%D8%A7%D8%AA%D9%8A%D9%84%D8%A7 ")


async def palestine_1983_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1983:\n"
        "/info83 for news, battles, or massacres\n"
        "/characters83 for characters or Martyrs\n")

async def info83_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1983: [Provide the news here]")

async def characters83_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1983: [List the battles]")


async def palestine_1984_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1984:\n"
        "/info84 for news, battles, or massacres\n"
        "/characters84 for characters or Martyrs\n")

async def info84_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1984: [Provide the news here]")

async def characters84_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1984: [List the battles]")


async def palestine_1985_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1985:\n"
        "/info85 for news, battles, or massacres\n"
        "/characters85 for characters or Martyrs\n")

async def info85_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1985: [Provide the news here]")

async def characters85_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1985: [List the battles]")


async def palestine_1986_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1986:\n"
        "/info86 for news, battles, or massacres\n"
        "/characters86 for characters or Martyrs\n")

async def info86_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1986: https://www.aljazeera.net/encyclopedia/2014/2/10/%D9%83%D8%AA%D8%A7%D8%A6%D8%A8-%D8%B9%D8%B2-%D8%A7%D9%84%D8%AF%D9%8A%D9%86-%D8%A7%D9%84%D9%82%D8%B3%D8%A7%D9%85")

async def characters86_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1986: https://www.aljazeera.net/encyclopedia/2010/12/9/%D8%B5%D9%84%D8%A7%D8%AD-%D8%B4%D8%AD%D8%A7%D8%AF%D8%A9\n https://www.aljazeera.net/encyclopedia/2010/12/9/%D8%B9%D8%B2-%D8%A7%D9%84%D8%AF%D9%8A%D9%86-%D8%A7%D9%84%D9%82%D8%B3%D8%A7%D9%85")
     

async def palestine_1987_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1987:\n"
        "/info87 for news, battles, or massacres\n"
        "/characters87 for characters or Martyrs\n")

async def info87_command(update: Update, context: CallbackContext):
      await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1987:https://www.aljazeera.net/midan/intellect/history/2024/1/7/%D8%A3%D8%B3%D8%B1%D8%A7%D8%B1-%D8%A7%D9%84%D8%B8%D9%87%D9%88%D8%B1-%D9%83%D9%8A%D9%81-%D9%86%D8%B4%D8%A3%D8%AA-%D8%AD%D8%B1%D9%83%D8%A9-%D8%AD%D9%85%D8%A7%D8%B3-%D9%88%D9%83%D8%AA%D8%A7%D8%A6%D8%A8 ")


async def characters87_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in palestine in 1987:  https://www.aljazeera.net/encyclopedia/2010/12/8/%D8%A3%D8%AD%D9%85%D8%AF-%D9%8A%D8%A7%D8%B3%D9%8A%D9%86 ")


async def palestine_1988_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1988:\n"
        "/info88 for news, battles, or massacres\n"
        "/characters88 for characters or Martyrs\n")

async def info88_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1988: [Provide the news here]")

async def characters88_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1988: [List the battles]")


async def palestine_1989_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1989:\n"
        "/info89 for news, battles, or massacres\n"
        "/characters89 for characters or Martyrs\n")

async def info89_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1989: [Provide the news here]")

async def characters89_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1989: [List the battles]")


async def palestine_1990_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1990:\n"
        "/info90 for news, battles, or massacres\n"
        "/characters90 for characters or Martyrs\n")

async def info90_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1990: [Provide the news here]")

async def characters90_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1990: [List the battles]")


async def palestine_1991_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1991:\n"
        "/info91 for news, battles, or massacres\n"
        "/characters91 for characters or Martyrs\n")

async def info91_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1991: [Provide the news here]")

async def characters91_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1991: [List the battles]")


async def palestine_1992_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1992:\n"
        "/info92 for news, battles, or massacres\n"
        "/characters92 for characters or Martyrs\n")

async def info92_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1992: [Provide the news here]")

async def characters92_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1992: [List the battles]")



async def palestine_1993_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1993:\n"
        "/info93 for news, battles, or massacres\n"
        "/characters93 for characters or Martyrs\n")

async def info93_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1993: [Provide the news here]")

async def characters93_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1993: [List the battles]")



async def palestine_1994_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1994:\n"
        "/info94 for news, battles, or massacres\n"
        "/characters94 for characters or Martyrs\n")

async def info94_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1994: [Provide the news here]")

async def characters94_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1994: [List the battles]")



async def palestine_1995_command(update: Update, context: CallbackContext):
    await update.message.reply_text("To see what happened in Palestine in 1995:\n"
        "/info95 for news, battles, or massacres\n"
        "/characters95 for characters or Martyrs\n")

async def info95_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the news,battles and massacres for Palestine in 1995: [Provide the news here]")

async def characters95_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Here are the characters or martyers in Palestine in 1995: [List the battles]")



# Responses
def handle_response (text : str) -> str :
    processed: str = text.lower()

    if 'hello' in processed:
        return ' hey there !'

    if 'how are you !' in processed:
        return 'I am fine what about you!'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    if 'i am fine too' in processed:
        return 'that is perfect!'
    if 'free palestine' in processed:
        return 'free palestine!'
    return' i did not understand what you wrote.....'

# Handing messages
async def handle_message(update: Update, context: CallbackContext):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'user({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
            print('Bot response:', response)
            await context.bot.send_message(update.message.chat_id, response)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot response:', response)
    await update.message.reply_text(response)


# Errors
async def error(update: Update, context: CallbackContext):
    print(f'Update {update} caused error {context.error}')

# polls the bot
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
 # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('1981', palestine_1981_command))
    app.add_handler(CommandHandler('info81', info81_command))
    app.add_handler(CommandHandler('characters81', characters81_command))
    app.add_handler(CommandHandler('1982', palestine_1982_command))
    app.add_handler(CommandHandler('info82', info82_command))
    app.add_handler(CommandHandler('characters82', characters82_command))
    app.add_handler(CommandHandler('1983', palestine_1983_command))
    app.add_handler(CommandHandler('info83', info83_command))
    app.add_handler(CommandHandler('characters83', characters83_command))
    app.add_handler(CommandHandler('1984', palestine_1984_command))
    app.add_handler(CommandHandler('info84', info84_command))
    app.add_handler(CommandHandler('characters84', characters84_command))
    app.add_handler(CommandHandler('1985', palestine_1985_command))
    app.add_handler(CommandHandler('info85', info85_command))
    app.add_handler(CommandHandler('characters85', characters85_command))
    app.add_handler(CommandHandler('1986', palestine_1986_command))
    app.add_handler(CommandHandler('info86', info86_command))
    app.add_handler(CommandHandler('characters86', characters86_command))
    app.add_handler(CommandHandler('1987', palestine_1987_command))
    app.add_handler(CommandHandler('info87', info87_command))
    app.add_handler(CommandHandler('characters87', characters87_command))
    app.add_handler(CommandHandler('1988', palestine_1988_command))
    app.add_handler(CommandHandler('info88', info88_command))
    app.add_handler(CommandHandler('characters88', characters88_command))
    app.add_handler(CommandHandler('1989', palestine_1989_command))
    app.add_handler(CommandHandler('info89', info89_command))
    app.add_handler(CommandHandler('characters89', characters89_command))
    app.add_handler(CommandHandler('1990', palestine_1990_command))
    app.add_handler(CommandHandler('info90', info90_command))
    app.add_handler(CommandHandler('characters90', characters90_command))
    app.add_handler(CommandHandler('1991', palestine_1991_command))
    app.add_handler(CommandHandler('info91', info91_command))
    app.add_handler(CommandHandler('characters91', characters91_command))
    app.add_handler(CommandHandler('1992', palestine_1992_command))
    app.add_handler(CommandHandler('info92', info92_command))
    app.add_handler(CommandHandler('characters92', characters92_command))
    app.add_handler(CommandHandler('1993', palestine_1993_command))
    app.add_handler(CommandHandler('info93', info93_command))
    app.add_handler(CommandHandler('characters93', characters83_command))
    app.add_handler(CommandHandler('1994', palestine_1994_command))
    app.add_handler(CommandHandler('info94', info94_command))
    app.add_handler(CommandHandler('characters94', characters94_command))
    app.add_handler(CommandHandler('1995', palestine_1995_command))
    app.add_handler(CommandHandler('info95', info95_command))
    app.add_handler(CommandHandler('characters95', characters95_command))

 # messages
    app.add_handler(MessageHandler(filters.Text, handle_message))
 # Errors
    app.add_error_handler(error)
 # polls the bot
    print('Polling....')
    app.run_polling(poll_interval=3)
