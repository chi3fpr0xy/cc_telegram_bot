# Bot setup
import telebot
bot = telebot.TeleBot(open('token.txt', 'r').read())

# Logging
import logging
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

# Global objects
# TODO: Specify author's Telegram ID
author = {
    'id': '@Skipp3r',
    'email': 'chi3fpr0xy@gmail.com'
}

AUTHORIZED_USERS = [author['id']]

error_message = ''
with open('error.txt', 'r') as error:
    error_message = str(error.readlines())


# Helpers

def authorized(userId):
    return True if userId in AUTHORIZED_USERS else False

def warn(message):
    bot.reply_to(message, 'NOT A CITIZEN!\n\nhttps://www.youtube.com/watch?v=UOkpO--XtH0')


# Help messages

@bot.message_handler(commands=['start'])
def send_welcome(message):
    start_text = '''
        Halt, stranger! I'm Lothar, paladin of the king. I am to explain all newcomers the new laws. See /help for details
        \nWARNING! This is currently a beta. To access the full version, go to https://cc.somesecretcorp.com
    '''
    bot.reply_to(message, start_text + "\nShould there be any errors, text " + author['id'])

@bot.message_handler(commands=['help'])
def print_help(message):
    # TODO: write help message
    help_text = '''
    Available commands:
    /start - shows greeting
    /help - shows this message
    /authorize <email> - grants access to some functions
    \nREQUIRES AUTH:
    /request_ddos <website> - push the website to our target list
    /check_bot <id> - checks if the bot is available
    '''
    bot.reply_to(message, help_text)


# Real commands

@bot.message_handler(commands=['authorize'])
def auth(message):
    print(message.text.split(' ')[1])
    if message.text.split(' ')[1] == author['email']:
        AUTHORIZED_USERS.append(message.chat.id)
        bot.reply_to(message, 'You are now authorized! Now you can use /request_ddos')

@bot.message_handler(commands=['request_ddos'])
def check(message):
    if 'somesecretcorp' in message.text.split(' ')[1]:
        bot.reply_to(message, 'I will consider this an offense!')
    elif authorized(message.chat.id):
        # TODO: Add the real functions
        bot.reply_to(message, 'OK! I\'ve scheduled this task')
    else:
        warn(message)

@bot.message_handler(commands=['check_bot'])
def bot_check(message):
    if not authorized(message.chat.id):
        warn(message)
        return
    
    m = message.text.split(' ')
    if len(m) <= 1:
        bot.reply_to(message, 'Please specify bot ID')
        return
    id_to_check = int(m[1])
    if id_to_check in range(20, 50):
        bot.reply_to(message, 'Bot is alive and working')
    else:
        bot.reply_to(message, 'Bot not found')
    

# Entry point

def main():
    bot.polling()

if __name__ == "__main__":
    main()

