from asyncio import tasks
from calendar import weekday
import os
import datetime

'''Criar Arquivo de Log - Onde guarda os dados'''
weekday_ = ["Segunda - Feira","Terça - Feira","Quarta - Feira","Quinta- Feira","Sexta - Feira","Sabado","Domingo"]
print(datetime.datetime.today(),weekday_[datetime.datetime.today().weekday()])

path = "C:\Wordspace\Python/18 - PROJETOS\QualyDay/"


class qualyDay:
    def __init__(self):
        #Iniciar base de dados
        try:
            bd = open(path + "log.txt","r")
        except:
            bd = open(path + "log.txt","w")

        bd.close()
        self.bd = path + "log.txt"

    def readLogFile(self):
        with open(self.bd,"r") as arq:
            print(" -> Loaded log.txt ")
            cont = arq.readline()
        return cont

    def writeLogFile(self,text):
        with open(self.bd,"a") as arq:
            arq.writelines(text)

    def extValue(self,entry,parameter = "-s"):
        try:
            add = 2

            if (len(parameter) >= 3): add = 3

            value = entry[entry.index(parameter) + add:]
            if (value[0] != '-'):
                value = value[:value.index("-")]
            else:
                value = "None"
        except:
            value = "None"
        return value

    def extHour(self,iHour):

        try:
            if (iHour != None):
                if (":" in iHour):
                    Hour = datetime.time(int(iHour[:iHour.index(":")]),int(iHour[iHour.index(":") + 1:len(iHour)]))
                else:
                    Hour = datetime.time(int(iHour))
        except:
            Hour = 'None'
        return Hour
    def fEntry(self,entry): # Retorno ["Dia_semana","Hora Inicio","Hora Fim","Tarefa"]
        #Linha de Comando
        '''
            -s Dia_semana -h Hora Inicio -hf Hora Fim -t Tarefa
            -s [0-6] -h 10:30 -hf Hora Fim -t Tarefa
            Parametros Obrigatorios: -s -t
        '''
        status = ""
        entry_ = str(entry).lower()
        entry_ = entry.replace(' ','')
        #Separar entry 
        fdate = {}
        if ('-s' in entry_ and '-t' in entry_):

            nWeekday = self.extValue(entry_,"-s")
            iHour = self.extValue(entry_,"-h")
            fHour = self.extValue(entry_,"-hf")
            print(fHour)
            task = entry[entry.index("-t") + 2:]

            if (nWeekday.isdigit() == False or int(nWeekday) > 6 or int(nWeekday) < 0): status += "<< Valor -s não especificado ou Invalido\n"
            else: fdate["nWeekday"] = nWeekday

            iHour = self.extHour(iHour)
            if (iHour == 'None'):
                status +=  "<< Valor -h invalido"
            else:
                fdate["iHour"] = iHour

            fHour = self.extHour(fHour)
            if (fHour == 'None'):
                status +=  "<< Valor -hf invalido"
            else:
                fdate["fHour"] = fHour

            fdate["task"] = task
        else:
            print("Entry Invalid")
        print(status)
        print(fdate)
        return status
 


    
qualyDay_ = qualyDay()
qualyDay_.writeLogFile("\ntest3")

qualyDay_.fEntry("-s 8 -h 23:90 -hf 20:30 -t Algoritmo II")
