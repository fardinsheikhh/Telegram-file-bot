from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8030582006:AAEGFWqkGjB16fY8jXSoRUkXBB_5cbBdJjw"

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document or update.message.photo[-1] if update.message.photo else None
    if not file:
        await update.message.reply_text("لطفاً یک فایل یا عکس بفرست!")
        return

    telegram_file = await file.get_file()
    await update.message.reply_text(f"✅ لینک مستقیم:\n{telegram_file.file_path}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_file))
    print("🤖 ربات شروع شد!")
    app.run_polling()