import inicial
import time
import PySimpleGUI as sgq
import shutil
import random

def saveLog(resumo):
    
    keytest = random.randint(1000,9999)
    filename = 'log\\'+str(keytest)+'.txt'
    with open(filename, "w") as logfile:
        
        logfile.write(resumo)
        logfile.close()
    return 
    