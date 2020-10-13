import telepot
from telepot.loop import MessageLoop
import reseving_mails_test
import time
import os
import datetime
import Do_This
import pir
import full_body_detec_time
import mail
import cv2


def handle(msg):
    global ALART
    global telegramText
    global chat_id
    # Receiving the message from telegram
    chat_id = msg['chat']['id']
    # Getting text from the message
    telegramText = msg['text'].lower()
    print('Message received from ' + str(chat_id))
    if True:
        # Comparing the incoming message to send a reply according to it
        print(telegramText)
        if telegramText == '/help':
            bot.sendMessage(chat_id, 'I see you need some help:')
            bot.sendMessage(chat_id, '/hi : if youre lonely. ')
            bot.sendMessage(chat_id, '/pic : Takes a picture')
            bot.sendMessage(chat_id, '/time : Who needs a watch.')
            bot.sendMessage(chat_id, '/stop : shut-down.')
            bot.sendMessage(chat_id, '/alarm : Makes a sound.')
            bot.sendMessage(chat_id, '/enable : Enable security system.')
            bot.sendMessage(chat_id, '/mail :  Read your last mail.')
            bot.sendMessage(chat_id, '/video : Short video (15sec).')

        elif telegramText == '/start':
            bot.sendMessage(chat_id, 'Welcome to my python-project!!')
            bot.sendMessage(chat_id, 'IF you want to check the commands just write down :   /help')

        elif telegramText == '/hi':
            bot.sendMessage(chat_id, str("Hi I'm a bot :) , how can I help? "))

        elif telegramText == '/time':
            bot.sendMessage(chat_id, str(f" The Time and Date now are : {time.asctime()}"))


        elif telegramText == '/stop':
            bot.sendMessage(chat_id, str("Total shutdown!"))
            os.system("shutdown -h now")

        elif telegramText == '/alarm':
            bot.sendMessage(chat_id, str("The alarm is working now"))
            Do_This.make_sound()


        elif telegramText == '/mail':
            if reseving_mails_test.receiving_mail():
                bot.sendMessage(chat_id, str("Your last email is from: " + mail.FROM))
                bot.sendMessage(chat_id, str("The subject is :" + mail.SUB))
                bot.sendMessage(chat_id, str("The body of the email is: " + mail.BODY))

        elif telegramText == '/pic':
            bot.sendMessage(chat_id, str("Takes a picture. please wait"))
            Do_This.Photo()
            bot.sendPhoto(chat_id, photo=open('img.jpg', 'rb'))

        elif telegramText == '/video':
            bot.sendMessage(chat_id, str("Taking a short video for 15 sec"))
            Do_This.Video(10)
            bot.sendVideo(chat_id=chat_id, video=open('output.mp4', mode='rb'))

        elif telegramText == '/enable':
            bot.sendMessage(chat_id, str("Its on!"))
            if pir.motion_check(pir.Pir_Pin):
                bot.sendMessage(chat_id, str("The motion detector detected something, Checking it"))
                if full_body_detec_time.body_detection(20):
                    bot.sendMessage(chat_id, str("I saw someone!! see it yourself"))
                    bot.sendPhoto(chat_id, photo=open('intruder.jpg', 'rb'))
                    bot.sendVideo(chat_id=chat_id, video=open('output2.mp4', mode='rb'))
                else:
                    bot.sendMessage(chat_id, str("I saw nothing, But you can check the video your self"))
                    bot.sendVideo(chat_id=chat_id, video=open('output2.mp4', mode='rb'))
                    cv2.destroyAllWindows()


if __name__ == '__main__':
    print('Listening....')
    # Connect to our bot
    bot = telepot.Bot(
        'YOUR TOKEN HERE')
    # Start listening to the telegram bot and whenever a message is received, the handle function will be called
    MessageLoop(bot, handle).run_as_thread()
