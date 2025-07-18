import os
from dotenv import load_dotenv

from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, CallbackContext

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    reply_keyboard = [["/help", "/menu"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    await update.message.reply_text(
        "Привет! Я учебный бот. Выбери команду ниже.", reply_markup=markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я бот с кнопками. Мои команды: /start, /help, /menu"
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    inline_keyboard = [
        [InlineKeyboardButton("Открыть сайт", url="https://www.python.org")],
        [InlineKeyboardButton("Нажми меня!", callback_data="click_button")]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard)
    await update.message.reply_text(
        "Это меню с онлайн кнопками. Выбери действие:", reply_markup=markup
    )
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "click_button":
        await query.message.edit_text("Ты нажал кнопку!")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")

    app.run_polling()

if __name__ == "__main__":
    main()