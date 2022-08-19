import telebot
import main

qualyDay_ = main.qualyDayLog()
#Chave da Api
KEY_API = ""
bot = telebot.TeleBot(KEY_API) #Iniciar bot

@bot.message_handler(commands=["set"])
def set(mensagem):
    entry = str(mensagem.text)
    fdate = qualyDay_.fEntry(entry)
    qualyDay_.writeLogFile("\n" + str(fdate[1]))
    msg = str(fdate[0])
    if (len(msg) == 0):
        msg = "Sucess"
    bot.send_message(mensagem.chat.id, msg)

@bot.message_handler(commands=["/now"])
def now(mensagem):
    pass
    #bot.send_message(mensagem.chat.id, msg)

@bot.message_handler(commands=["help"])
def help(mensagem):
    bot.send_message(mensagem.chat.id, '''[Dia_semana, H Inicio, H Fim, Tarefa]
     -s [0-6] -h 00:00 -hf 00:01 -t Name_Task    -> Set Date
    ''')

'''Bloco de Entrada do bot que responde qualquer mensagem'''
def direction(entry):
    fdate = qualyDay_.fEntry(entry)
    qualyDay_.writeLogFile("\n" + str(fdate[1]))
    return(str(fdate[0]))

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """ QualyDay Start
    /help - Instruções
    /set - set new date"""
    bot.reply_to(mensagem, texto)# marca a mensagem e envia


bot.polling() #loop Infinito do bot
