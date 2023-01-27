import telebot
from telebot import types,util
from msgs import *
from decouple import config
from gtts import gTTS
import os
import cv2
import HandTrackingModule as htm
import easyocr
import warnings
warnings.filterwarnings("ignore")

BOT_TOKEN = config('BOT_TOKEN')
bot= telebot.TeleBot(BOT_TOKEN)
chat_id = -1001710843759

text_messages={
    "welcome": "welcome to DIA-BTS chatbot 😀\nsay help to see menu ",
    "welcomeNewMember" :
                u"hi, welcome to {name} in BTS DIA 🙋‍",
    "saying goodbye":
                u"{name} lift us 🥺"
}
##############################################################################################################################
@bot.message_handler(commands=["start","help"])
def startBot(message):
    bot.send_message(message.chat.id,text_messages["welcome"])
##############################################################################################################################
# saying Welcome to joined members
# saying goodbye to left members
@bot.chat_member_handler()
def handleUserUpdates(message:types.ChatMemberUpdated):
    newResponse = message.new_chat_member
    if newResponse.status == "member":
        bot.send_message(message.chat.id,text_messages["welcomeNewMember"].format(name=newResponse.user.first_name))
    if newResponse.status == "left":
        bot.send_message(message.chat.id,text_messages["saying goodbye"].format(name=newResponse.user.first_name))
##############################################################################################################################

# answering every message not just commands
def isMSg(message):
    return True
##############################################################################################################################

@bot.message_handler(content_types=['photo'])
def photo(message):
    #get the image
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    #download the image
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    new_file.close()
    #read the image by cv2
    img = cv2.imread("image.jpg")
    #detect hands, draw hands and send new image
    detector = htm.handDetector(maxHands=6, detectionCon=0.4)
    hands,img = detector.findHands(img)
    if len(hands)>0:
        cv2.imwrite("image.jpg",img)
        with open("image.jpg", "rb") as pic:
            bot.send_photo(message.chat.id, pic)
        pic.close()
    #delet the images
    os.remove('image.jpg')
    
    #read the content of image
    reader = easyocr.Reader(['en'],gpu=True)
    res = reader.readtext(img)
    #restruct the text
    text = ""
    for i in range(len(res)):
        text+=res[i][1]
        text+=" "
    #send the text and the audio if it possible
    try:
        spesh = gTTS(text = text, lang = "en")
        spesh.save("audio.mp3")
        bot.reply_to(message,text)
        return bot.send_audio(message.chat.id, audio=open('audio.mp3', 'rb')),os.remove('audio.mp3')
    #send "no text" if it not possible
    except :
        return bot.reply_to(message,"no text")
##############################################################################################################################

@bot.message_handler(func=isMSg)
def reply(message):
    words = message.text.split()

    if words[0].lower() in ["who" , "what" ] :
        return bot.reply_to(message,"i am just a simple bot say help to see me")
    if words[0].lower() in hi :
        return bot.reply_to(message,"hey how is going!")
    if words[0].lower() == "help" :
        return bot.reply_to(message,hlp)
    if words[0].lower() in info :
        return bot.reply_to(message,infos)
    if words[0].lower() in subjects :
        return bot.reply_to(message,"- S1\n- Interviews")
    if words[0].lower() == "s1" :
        return bot.reply_to(message,s1),bot.reply_to(message,"mention the subject to see their resources!")
    if words[0].lower() == "s1" :
        return bot.reply_to(message,"mention the subject to see their resources !")

    if words[0].lower() in inters :
        return bot.reply_to(message,interview1),bot.reply_to(message,interview2),bot.reply_to(message,interview3),bot.reply_to(message,interview4),bot.reply_to(message,interview5),bot.reply_to(message,interview6),bot.reply_to(message,interview7),bot.reply_to(message,interview8),bot.reply_to(message,interview9), bot.reply_to(message,"Interviews : https://www.udrop.com/7Kx4/ML.rar")
    if words[0].lower() == "algorithms":
        return bot.reply_to(message,"algorithms : https://www.udrop.com/7KwS/1_algorithmes.rar")
    if words[0].lower() == "computer":
        return bot.reply_to(message,"computer structure : https://www.udrop.com/7KwU/1_AO.rar")
    if words[0].lower() == "databases":
        return bot.reply_to(message,"DataBases : https://www.udrop.com/7KwV/BDR.rar")
    if words[0].lower() == "math":
        return bot.reply_to(message,"Math : https://www.udrop.com/7KwW/1_math.rar")
    if words[0].lower() == "applied":
        return bot.reply_to(message,"Applied mathematics : https://www.udrop.com/7Kx0/MIA.rar")
    if words[0].lower() == "python":
        return bot.reply_to(message,"Python : https://www.udrop.com/7KwX/1_python.rar")
    if words[0].lower() == "operating":
        return bot.reply_to(message,"Operating systems : https://www.udrop.com/7KwY/1_SysExploit.rar")
    if words[0].lower() == "frensh":
        return bot.reply_to(message,"Frensh : https://www.udrop.com/7Kx3/FR.rar")
    if words[0].lower() == "english":
        return bot.reply_to(message,"English : https://www.udrop.com/7Kx2/ANG.rar")
    if words[0].lower() == "entrepreneurship" or words[0].lower() =="economics" :
        return bot.reply_to(message,"Entrepreneurship & Economics : https://www.udrop.com/7Kx1/entreprenariat.rar")
    if words[0].lower() == "arabic":
        return bot.reply_to(message,"Arabic : NULL")


    if words[0].lower() in ecole :
        return bot.reply_to(message,kindy)
    if words[0].lower() in coor :
        return bot.reply_to(message,coordinator)
    if words[0].lower() in creators :
        return bot.reply_to(message,creator)

    if words[0].lower() in cvs:
        return bot.reply_to(message,cv_menu),bot.reply_to(message,me)

    if words[0].lower() in ["def","definition"] :
        return bot.reply_to(message,w_cv)

    if words[0].lower() in ["work","how","works"]:
        return bot.reply_to(message,cv_w)

    if words[0].lower() in ["examples","example","ex"]:
        return bot.reply_to(message,exmp)

    if words[0].lower() in ["cv2","opencv","lib"]:
        return bot.reply_to(message,ocv)


    if words[0].lower() in ["say","قل","dire"] :

        if words[0].lower() in ["say","dire"] :
            if words[-1].lower() in ["ar","arabic","arabia","arabie","بالعربية","fr","frensh","francais","français","en","english","anglais","eng"]:
                text = words[1:-2]
            else:
                text = words[1:]
            # initialize an empty string
            txt = ""
            # traverse in the string
            for ele in text:
                txt += ele
                txt += " "
        if words[0].lower() == "قل" :
            if words[-1].lower() in ["ar","arabic","arabia","arabie","بالعربية","fr","frensh","francais","français","en","english","anglais","eng"]:
                text = words[1:-1]
            else :
                text = words[1:]
            # initialize an empty string
            txt = ""
            # traverse in the string
            for ele in text:
                txt += ele
                txt += " "

        if words[-1].lower() in ["en","english","anglais","eng"]:
            lng = "en"
        elif words[-1].lower() in ["fr","frensh","francais","français"]:
            lng = "fr"
        elif words[-1].lower() in ["ar","arabic","arabia","arabie","بالعربية"]:
            lng = "ar"
        else :
            lng = "ar"

        spesh = gTTS(text = txt, lang = lng)
        spesh.save("audio.mp3")

        return bot.send_audio(message.chat.id, audio=open('audio.mp3', 'rb')),os.remove('audio.mp3')



    else:
        return bot.reply_to(message,'i do not understand !\nplease say (help) to see the menu.')
##############################################################################################################################

bot.infinity_polling(allowed_updates=util.update_types)
