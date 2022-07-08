from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'xin chao {update.effective_user.first_name}')
    
def help_command(update: Update, context: CallbackContext):
   update.message.reply_text("Bạn muốn tôi giúp gì? \n 1. Kể truyện cười-> /click_here")


def click_here(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Nhà phê bình : – Ôi! Cái gì thế này! Đây đúng là một tuyệt tác! Quá hoàn hảo! Quá tinh tế. \n Họa sĩ: – Gì vậy? À đó là chỗ tôi chùi cọ cho sạch sơn đấy!")

updater = Updater('5402495110:AAHcqMRa5FsQav_SYnVBP7YOjT8_cvUQPRE')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(CommandHandler("click_here", click_here))

updater.dispatcher.add_handler(CommandHandler("help", help_command))

updater.start_polling()

updater.idle()