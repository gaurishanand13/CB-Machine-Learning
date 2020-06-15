import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)


from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Bot, Update


TOKEN = "1101626318:AAGtRBJTK_TEyNJNKXfbSVTlf_vQTtIVFlY"


#Created an object of Flask class which will help us in handling the callback url's end points
app = Flask(__name__)

#This route will be executed first when the server is set up
@app.route('/')
def index():
    return "Hello!"



@app.route(f'/{TOKEN}', methods=['GET', 'POST'])
def webhook():
    """webhook view which receives updates from telegram"""
    # create update object from json-format request data . Here request.get_json() will get us the data in the form of json object
    update = Update.de_json(request.get_json(), bot)
    # process update
    dp.process_update(update)
    return "ok"




def start(bot,update):
    author = update.message.from_user.first_name
    reply_message = "Hi! {}".format(author)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=reply_message)
        
    
def help(bot,update):
    reply_message = "Hey! This is a help Text"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=reply_message)
        
        

def echo_text(bot, update):
    reply_message = update.message.text
    bot.send_message(
        chat_id=update.message.chat_id,
        text=reply_message)
        
        

def echo_sticker(bot, update):
    reply_sticker = update.message.sticker.file_id
    bot.send_sticker(
        chat_id=update.message.chat_id,
        text=reply_sticker)
        
    
def error(bot,update):
    logger.error("Update '%s' caused error '%s'", update, update.error)
    


if __name__ == "__main__":
    bot = Bot(TOKEN)
    bot.set_webhook("https://50a36366f4ae.ngrok.io/" + TOKEN)
    
    dp = Dispatcher(bot,None)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_error_handler(error)
    
    app.run(port=8443)
