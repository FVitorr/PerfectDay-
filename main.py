import os
import datetime
import ast 

'''Criar Arquivo de Log - Onde guarda os dados'''
weekday_ = ["Segunda - Feira","Terça - Feira","Quarta - Feira","Quinta- Feira","Sexta - Feira","Sabado","Domingo"]
class date_:
    def __init__(self) -> None:
        pass
    def today(self):
        weekday_ = ["Segunda - Feira","Terça - Feira","Quarta - Feira","Quinta- Feira","Sexta - Feira","Sabado","Domingo"]
        return datetime.datetime.today(),datetime.datetime.today().weekday(),weekday_[datetime.datetime.today().weekday()]

#print(datetime.datetime.today(),weekday_[datetime.datetime.today().weekday()])

path = "C:\Wordspace\Python/18 - PROJETOS\QualyDay/"
weekadayInfo = date_().today()


class qualyDayLog:
    def __init__(self):
        #Iniciar base de dados
        nameFile = path + "log.bin"
        try:
            bd = open(nameFile,'rb')
        except:
            bd = open(nameFile,'wb')
            pass

        self.bd = nameFile

    def readLogFile(self):
        with open(self.bd,'rb') as arq:
            liner = arq.readlines()
        lines = []
        for i in liner:
            lines.append(i.decode("ascii"))
        return liner

        with open(self.bd,'rb') as arq:
            print(" -> Loaded log.bin ")
            unpickler = pickle.Unpickler(arq)
            print(unpickler)
            scores = unpickler.load()
        #print(scores)
        return scores

    def writeLogFile(self,text):
        res = text.encode("ascii")
        with open(self.bd,"ab") as arq:
            arq.write(res)
        return (1)

    def filter(self,key,text):
        arq = self.readLogFile()
        msg = "Nenhuma Tarefa para Hoje"
        cont = 0
        
        #Bloco para transformar o bd em um array de objetos
        task = {}
        for i in range(len(arq)):
            str_ = arq[i].decode("ascii").replace("\n","")
            dictionary = ast.literal_eval(str_) 
            task[cont] = dictionary
            cont += 1

        #buscar elementos
        #print(task)
        result = []
        for i in range(len(task)): #i representa as key
            if str(text) in str(task[i][key]):
                result.append(task[i])
                msg = "Tarefas para " + weekday_[weekadayInfo[1]]

        return (msg,result)
        
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

            if (nWeekday.isdigit() == False or int(nWeekday) > 7 or int(nWeekday) < 0 or nWeekday == 'None'): 
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

class format_:
    def __init__(self) -> None:
        pass
    def table(dict_):
        pass
 

if __name__ == "__main__":
    qualyDay_ = qualyDayLog()

    date = "-s 6 -t psd"
    fdate = qualyDay_.fEntry(date)
    qualyDay_.writeLogFile(str(fdate[1]) + '\n')

    print(qualyDay_.filter("nWeekday",6))

