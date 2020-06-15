import logging

#Enable Logging --> Therefore writing the down line will enable the logs => everyTime a function or something is executed where asctime is the Time at which
#that function is executed and name is the name of the function whereas levelname is the level of that function executed and message tells what actually was executed.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)






from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
TOKEN = "1101626318:AAGtRBJTK_TEyNJNKXfbSVTlf_vQTtIVFlY"


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
        
        
#If some text is received as input , then we will give back the same message as output to the user(actually bot will give that). Therefore we called it as echo of text
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
    #Therefore if some error is there, instead of showing it we will log it.
    logger.error("Update '%s' caused error '%s'", update, update.error)
    



def main():

    #This is the Updater which gets us the update at every frequent intervals of time i.e it gets us the update if any message is received by the BOT.
    updater = Updater(TOKEN)
    
    #Therefore now we will handling any message which is received by the bot. These messages/commands will come as UPDATE to us(i.e someone has send the message to bot)
    #Handling of this update is done by the dispatcher.
    dp = updater.dispatcher
    #Note - Now there can be 2 types of messages ->
    """
    1) Commands  - If an user makes some commands to a Telegram Bot. By default every command in telegram starts with a '/'. Therefore all the messages which start
    with '/' will be treated as a command. For now our bot will be able to process only 2 types of commands one is start (i.e '/start') and the other is help(i.e
    '/help'). Therefore if the user writes anyother command (i.e a message which starts with '/' , then it will be an error)
    """
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    #Here start and help are the functions which will be executed when these commands will be will be made to the bot
    
    
    #Therefore all other messages which don't start with '/' are considered as normal text messages . Now these normal messages can be further divided to handle -
    #1) If a bot receives a normal text , then it will be executing echo_text()
    #2) If a bot receives a sticker , then it will be executing echo_sticker()
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    
    #But if some error is received on handling the message , then this error function will be executed which will log this error out
    dp.add_error_handler(error)
    
    
    updater.start_polling()
    logger.info("Started polling...")
    updater.idle()




if __name__ == "__main__":
    main()
