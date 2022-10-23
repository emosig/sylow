from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

from sylows import *

updater = Updater("5358989366:AAH_bFpnAnWuOJ4ipUYCm65X8e8nTQZR0sw", use_context=True)

# --- functions used in conversation ---
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Ciao! Sono il bot di calcolare p-Sylows. Scrivi\
 /help per vedere gli opzioni disponibili.")

    return GENERAL

  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Opzioni disponibili :-
    /sylows - Cerco di dirti il più possibile sui p-sylow di un gruppo 
        dato l'ordine
    /test - For testing purposes """)


def sylows(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Scrivi l'ordine del gruppo:")
    #user_input = update.message.text
    #msglist = parser(int(user_input))
    # Using list comprehension
    #[update.message.reply_text(msg) for msg in msglist]
    
    return EXPECT_ORDER

def sylowsparser(update: Update, context: CallbackContext):
    msglist = parser(int(user_input))
    # Using list comprehension
    [update.message.reply_text(msg) for msg in msglist]

    return GENERAL
    
#test function
def test(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Test number input")
    return EXPECT_ORDER
    

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


#Entering the order of the desired group
def number_input_by_user(update: Update, context: CallbackContext):
    ord = update.message.text

    # saves the number
    context.user_data['ord'] = ord
    update.message.reply_text(f'The number is saved as {ord[:100]}')

    # parsing
    msglist = parser(int(ord))
    # Using list comprehension
    [update.message.reply_text(msg) for msg in msglist]

    return GENERAL

#Exiting of conversation handler
def cancel(update, context):

    update.message.reply_text('canceled')

    # end of conversation
    return ConversationHandler.END
  

dp = updater.dispatcher

#testing conversation handler
#For now only works linearly iterating through the states

# --- states use in conversation ---

GENERAL = 0
HELP = 1
SYLOWS = 21
SYLOWSPARSER = 20
TEST = 3
EXPECT_ORDER = 101

my_conversation_handler = ConversationHandler(
   entry_points=[CommandHandler('start', start)],
   states={
       GENERAL: [
           CommandHandler('help', help),
           CommandHandler('sylows', sylows),
           CommandHandler('test', test),
           MessageHandler(Filters.text, unknown)
       ],
       HELP: [
           CommandHandler('help', help),
           MessageHandler(Filters.text, unknown)
       ],
       SYLOWS: [
           CommandHandler('sylows', sylows),  # has to be before MessageHandler to catch `/cancel` as command, not as `text`
           MessageHandler(Filters.text, unknown)
       ],
       TEST: [
           CommandHandler('test', test),  # has to be before MessageHandler to catch `/cancel` as command, not as `comments`
           MessageHandler(Filters.text, unknown)
       ],
       EXPECT_ORDER: [
            #TAKING INTEGER INPUT FROM USER
           MessageHandler(Filters.text, number_input_by_user)
       ],
   },
   fallbacks=[CommandHandler('cancel', cancel)]
)                

dp.add_handler(my_conversation_handler)

#dp.add_handler(CommandHandler('test', test))
#dp.add_handler(CommandHandler('start', start))
#dp.add_handler(CommandHandler('help', help))
#dp.add_handler(CommandHandler('sylows', sylows))
#dp.add_handler(MessageHandler(Filters.text, unknown))
# Filters out unknown commands
#dp.add_handler(MessageHandler(Filters.command, unknown))  
# Filters out unknown messages.
#dp.add_handler(MessageHandler(Filters.text, unknown_text))

# --- run bot ---

updater.start_polling()
print('Running... [Press Ctrl+C to stop]')
updater.idle()
print('Stoping...')
updater.stop()  