import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇺🇦 Привіт! Я бот для керування чатом.\n\n"
        "Доступні команди:\n"
        "/help — допомога\n"
        "/stats — статистика\n"
        "/top — активні учасники"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Команди бота:\n\n"
        "📊 /stats — статистика чату\n"
        "🏆 /top — найактивніші учасники\n"
        "⚠️ /warn — попередження\n"
        "🔇 /mute — мут\n"
        "🚫 /ban — бан"
    )


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Статистика чату\n\n"
        "Функція статистики зараз налаштовується."
    )


async def top(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 Топ активних учасників\n\n"
        "Статистика поки збирається."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("top", top))

    print("Бот запущений!")

    app.run_polling()


if __name__ == "__main__":
    main()
