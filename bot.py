import telepot
from learn import learnName, checkName, learnPhrase, checkPhrase
from tokenBot import returnToken

bot = telepot.Bot(returnToken()) # Receives the Token of a function in token.py

learningName = None

def receivingMsg(msg):
    global learningName
    contentType, chatType, chatID = telepot.glance(msg)
    #print(bot.getUpdates())

    if (contentType == 'photo'): # Get a picture and send it back
        file_id = msg['photo'][-1]['file_id']
        namePhoto = './' + file_id + '.png'
        bot.download_file(file_id, namePhoto)
        bot.sendPhoto(chatID, open(namePhoto, 'rb'))
    
    elif (contentType == 'text'):
        text = msg['text']

        #Commands
        if('/start' == text.lower()):
            bot.sendMessage(chatID, "Bot em teste, não nos responsabilizamos por nada")

        elif('/pillarmen' == text.lower()):
            bot.sendPhoto(chatID, 'AgADAQADdagxGwfsuUVgQqWXa1HcFYACCzAABLbXnaNoCQQ-cr0EAAEC',caption="AiaiaiaiAiaiaiaiAiaiaiaiAiaiaiaiAiaiaiaiAiaiaiai")
            bot.sendAudio(chatID, 'CQADAQADYwADB-y5RadjBP5GTVpwAg')

        elif('/aprende' in text.lower()):
            separator = text.find("=")
            userPhrase = text[9:separator].lower()
            botPhrase = text[separator+1:]
            learnPhrase(userPhrase, botPhrase)
            bot.sendMessage(chatID, "Aprendi a frase")

        elif('/nome' in text.lower()):
            bot.sendMessage(chatID, "Sou Renan's, o bot que vai dominar o mundo, e o seu nome qual é?")
            learningName = True

        #Answers
        elif(learningName != None):
            name = learnName(str(chatID),text)
            learningName = None
            bot.sendMessage(chatID, "Aprendi seu nome " + name)

        elif('meu nome' in text.lower()):
            name = checkName(str(chatID))
            if(name != None):
                bot.sendMessage(chatID, "Seu nome é " + name)
            else:
                bot.sendMessage(chatID, "Não seu sei nome")

        elif("ada" == text.lower()):
            for i in range(5):
                bot.sendMessage(chatID, "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
                bot.sendMessage(chatID, "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤")

        #Math operations
        elif("+" in text):
            try:
                operator = text.find("+")
                x = float(text[:operator])
                y = float(text[operator+1:])
                bot.sendMessage(chatID, x + y)
            except:
                bot.sendMessage(chatID, "Me envie somente números")
        elif("*" in text):
            try:
                operator = text.find("*")
                x = float(text[:operator])
                y = float(text[operator+1:])
                bot.sendMessage(chatID, x * y)
            except:
                bot.sendMessage(chatID, "Me envie somente números")
        elif("-" in text):
            try:
                operator = text.find("-")
                x = float(text[:operator])
                y = float(text[operator+1:])
                bot.sendMessage(chatID, x - y)
            except:
                bot.sendMessage(chatID, "Me envie somente números")
        elif("/" in text):
            try:
                operator = text.find("/")
                x = float(text[:operator])
                y = float(text[operator+1:])
                bot.sendMessage(chatID, x / y)
            except:
                bot.sendMessage(chatID, "Me envie somente números")

        #Check phrases
        else:
            phrase = checkPhrase(text.lower())
            if(phrase):
                bot.sendMessage(chatID, phrase)
            else:
                bot.sendMessage(chatID, "Tendi foi nada")

    else:
        bot.sendMessage(chatID, "Ainda não fui programado para isso")

#Main       
bot.message_loop(receivingMsg)

print('Running...')
while(True):
    stop = input('Stop? ')
    if(stop == 'y'):
        break
    pass