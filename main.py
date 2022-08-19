from asyncio import tasks
from calendar import weekday
import os
import datetime

'''Criar Arquivo de Log - Onde guarda os dados'''
weekday_ = ["Segunda - Feira","Terça - Feira","Quarta - Feira","Quinta- Feira","Sexta - Feira","Sabado","Domingo"]
print(datetime.datetime.today(),weekday_[datetime.datetime.today().weekday()])

path = "C:\Wordspace\Python/18 - PROJETOS\QualyDay/"


class qualyDayLog:
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
            cont = arq.readlines()
        return cont

    def writeLogFile(self,text):
        cont = self.readLogFile()
        fatherDict = {}
        for i in range(1,len(cont)+1):
            cont[i] = cont[i].replace("\n","")
            print(cont[i])
            fatherDict[str(i)] = dict(cont[i])
            print(fatherDict)
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
        Hour = 0
        try:
            if (iHour != None):
                if (":" in iHour):
                    Hour = datetime.time(int(iHour[:iHour.index(":")]),int(iHour[iHour.index(":") + 1:len(iHour)]))
                else:
                    Hour = datetime.time(int(iHour))
            erro = 1
        except:
            erro = 0
        return Hour,erro
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
            task = entry[entry.index("-t") + 2:]

            if (nWeekday.isdigit() == False or int(nWeekday) > 6 or int(nWeekday) < 0 or nWeekday == 'None'): 
                status += "<< Valor -s não especificado ou Invalido\n"
            else:
                fdate["nWeekday"] = int(nWeekday)
                iHour = self.extHour(iHour)
                if (iHour[1] == 1):
                    status +=  "<< Valor -h invalido"
                else:
                    if (iHour[0] != 0):
                        fdate["iHour"] = iHour[0]

                fHour = self.extHour(fHour)
                if (fHour[1] == 1):
                    status +=  "<< Valor -h invalido"
                else:
                    if (fHour[0] != 0):
                        fdate["iHour"] = fHour[0]
                fdate["task"] = task
        else:
            print("Entry Invalid")
            status += "Entry Invalid"
        print(status)
        return status,fdate
        
 



qualyDay_ = qualyDayLog()

date = "-s 0 -t psd"
fdate = qualyDay_.fEntry(date)
qualyDay_.writeLogFile(str(fdate[1]) + '\n')
