import os
import PySimpleGUI as sg
import threading
import function
import inicial
import time
from datetime import datetime
import PySimpleGUI as sgq
import shutil
import PySimpleGUI as sg

contador_falha = 0
stations = inicial.data_inicial()
files = inicial.files()
diretorio = inicial.log()

#set the theme for the screen/window
sg.theme("LightBlue")
#define layout
layout=[[sg.Text('Waiting ACTION...', key='RESULT')],
        [sg.ProgressBar(50, orientation='h', size=(20, 20), border_width=4, key='progbar',bar_color=['Blue','Green'])],
        [sg.Output(size=(50, 20), key = 'SAIDA')],
        [sg.Submit(key='btnSubmit'), sg.Cancel()]]
#Define Window

window =sg.Window("Label Server",layout, resizable = False)
#Read  values entered by user

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'btnSubmit':
        def running():
            window.find_element('RESULT').Update('PROCESSING...')
            window.find_element('SAIDA').Update('')
            inicio = datetime.now()
            print(inicio)
            contador_falha = 0
            ciclo = 0
            size_stations = len(stations)
            for station in stations:
                ciclo = ciclo + 1
                valor = (ciclo/size_stations) * 50
                window['progbar'].update_bar(valor)
                print(station)
                try:                 
                    for file in files:
                        print(file) 
                        
                        source=r'labelserver.txt'
                        source=source.replace("labelserver.txt", file)
                        #source=r'LABEL_SERVER_HGU_SV.txt'
                        destination=r'destino\labelserver.txt'
                        destination=destination.replace("labelserver.txt", file)
                        destination=destination.replace("destino", station)
                        shutil.copyfile(source, destination)
                        
                    print('COPIADO PARA ' + station + 'com sucesso!')
                    
                except:
                    contador_falha = contador_falha + 1
                    print('ACONTECEU UM ERRO AO COPIAR PARA ' + station)
            print('\n\nTotal de Falhas: ' + str(contador_falha))
            resume = window.find_element(key='SAIDA').Get()
            function.saveLog(resume)
            
            window.find_element('RESULT').Update('FINISHED')
        t1 = threading.Thread(target=running, daemon=True, kwargs={})
        t1.start()
window.close()