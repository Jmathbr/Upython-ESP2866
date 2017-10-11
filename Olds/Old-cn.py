import network
import ujson
import time
import os
from machine import Pin
class Connect:
    def __init__(self):
        print ("Iniciando o sistema WLAN")
    
    def wifi_auto(self):
        print ("Configurando WLAN...")
        led = Pin(2,Pin.OUT)
        cont = 0
        wlan = network.WLAN(network.STA_IF)
        wlan.disconnect()
        active = wlan.active()
        while not wlan.isconnected():
            active = wlan.active()
            if(active == False):
                wlan.active(True)

            arq = None

            try:
                arq = open("redes.json","r").read()
                print("Arquivo Redes.json achado")
                print(" ")
            
            except:

                print("Criando arquivo redes.json")
                print(" ")
                rootssid = input("Insira o nome da Rede: ")
                rootkey = input("Insira a senha: ")
                arq = open("redes.json","w")
                data = [{"SSID":rootssid, "KEY":rootkey}]
                arq.write(ujson.dumps(data))
                arq.close()

            arq =open("redes.json","r+").read()
            arq = ujson.loads(arq)
            qnt_data = len(arq)
            print ("Numero de redes salvas: ")
            print (qnt_data)

            while qnt_data > 0:
                qnt_data = qnt_data - 1
                ssid = arq[qnt_data]["SSID"]
                key = arq[qnt_data]["KEY"]
                print("Connectando-se a rede: "+ssid)
                print(" ")
                print("Senha da rede: "+key)
                print(" ")
                wlan.connect(ssid,key)
                for cont in range (40):
                    if(cont%5 == 0 ):
                        print(".")
                    led.value(1)
                    time.sleep_ms(100)
                    led.value(0)
                    time.sleep_ms(100)
                    if(wlan.isconnected()==True):
                        break
                    if(cont == 39):
                        print("Estado de connecçao: ")
                        print(wlan.isconnected())
                        print(" ")
                        print("Tempo de connecçao expirado, tentarei outra rede...")
                        print(" ")
                if(wlan.isconnected()== True):
                    print("Estado de connecçao: ")
                    print(wlan.isconnected())
                    print(" ")
                    print("Informaçoes da rede: ")
                    print(wlan.ifconfig())
                    print(" ")
                    break
            save = input("Deseja cadastrar uma nova rede: YES (y) , NO (n) : ")
            print(" ")
            if(save == "y"):
                print("Redes Disponiveis: ")
                print(" ")
                print(wlan.scan())
                print(" ")
                arq = open("redes.json","r+")
                newssid = input("Nome da rede: ")
                print(" ")
                newkey = input ("senha: ")
                print(" ")
                new_data = {"SSID":newssid, "KEY":newkey}
                conv = ujson.loads(arq.read())
                conv.append(new_data)
                arq.seek(0)
                arq.write(ujson.dumps(conv))
                arq.close()

            strong = input("Deseja repetir o processo: YES (y) , NO (n) : ")
            if(strong == "n"):
                print(" ")
                print("Processo finalizado com sucesso!")
                break

    def remove(self):

        #criando a caixa que guarda temporariamente os dados
        track = open("track.json","w")
        emp = []
        track.write(ujson.dumps(emp))
        track.close()

        #Ligar a coleta de dados do arquivo dentro do esp
        arq = open("redes.json","r+").read()
        arq = ujson.loads(arq)

        #Ultima posicao do vetor
        amount = len(arq) -1
        #Numero de dados dentro do vetor
        for i in range (len(arq)):
            i = str(i)
            print("Rede: "+i)
            i = int(i)
            print(arq[i]["SSID"])
            print("")

        remove = int(input("Deseja remover qual rede: "))
        track = open("track.json","r+")

        pos = 0
        pos2 = 0
        cont = 0
        cont2 = 0
        if (remove >=0)and(remove <=amount):

            if (remove == amount):
                #Condicao feita somente para excluir o ultimo dados add
                for cont in range (amount):

                    track = open("track.json","r+")

                    saveid = arq[cont]["SSID"]
                    savekey = arq[cont]["KEY"]
                    newdata = {"SSID":saveid,"KEY":savekey}

                    conv = ujson.loads(track.read())
                    conv.append(newdata)
                    track.seek(0)
                    track.write(ujson.dumps(conv))
                    track.close()
                    
            else:

                for cont in range (amount):
                    if(cont < remove):
                        track = open("track.json","r+")

                        saveid = arq[cont]["SSID"]
                        savekey = arq[cont]["KEY"]
                        newdata = {"SSID":saveid,"KEY":savekey}

                        conv = ujson.loads(track.read())
                        conv.append(newdata)
                        track.seek(0)
                        track.write(ujson.dumps(conv))
                        track.close()

                    else:
                        pos = remove + cont2
                        
                        track = open("track.json","r+")

                        saveid = arq[pos+1]["SSID"]
                        savekey = arq[pos+1]["KEY"]
                        
                        newdata = {"SSID":saveid,"KEY":savekey}

                        conv = ujson.loads(track.read())
                        conv.append(newdata)
                        track.seek(0)
                        track.write(ujson.dumps(conv))
                        track.close()

                        cont2 = cont2 + 1

                        if(cont == amount-1):
                            break
        
        else:
            print("Numero invalido")
            os.remove("track.json")

        try:
            track = open("track.json").read()
            track = ujson.loads(track)
            qnt = int(len(track))
        except ValueError:
            print("...")
        if qnt > 0:
            os.remove("redes.json")
            os.rename ("track.json","redes.json")
            arq = open("redes.json").read()
            arq = ujson.loads(arq)
            print("rede atualizada : ")
            print(arq)