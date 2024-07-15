from telegram.ext.updater import Updater 
from telegram.update import Update 
from telegram.ext.callbackcontext import CallbackContext 
from telegram.ext.commandhandler import CommandHandler 
from telegram.ext.messagehandler import MessageHandler 
from telegram.ext.filters import Filters 


from getipv6 import get_ipv6_address
from botconfig import accessToken

updater = Updater(accessToken, 
                  use_context=True) 

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello my friend, How can I help you today? \
            use /help to see the commands available" )

def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Available Commands:-
        /Ipbhej- to get the IP
        """)

def ip_bhej(update: Update, context: CallbackContext):
    update.message.reply_text(
        "ye hai ip '%s'." %get_ipv6_address())

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command")

def unknown_text(update: Update, context: CallbackContext): 
    update.message.reply_text( 
        "Sorry I can't recognize you , you said '%s'" % update.message.text) 

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('ipbhej', ip_bhej))
updater.dispatcher.add_handler(CommandHandler('ip', ip_bhej))
updater.dispatcher.add_handler(CommandHandler('bhej', ip_bhej))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))


updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))


updater.start_polling()

if __name__ == "__main__":
    updater.start_polling()