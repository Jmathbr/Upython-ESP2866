import network
import ujson
import time
import os
from machine import Pin

led = Pin(2,Pin.OUT)

class Connect:
    def __init__(self):
        print("Function Wlan")
    


    def wifi_manual(self):              # Connectando manualmente
    
        print("connectando Manualmente...")
        wlan = network.WLAN(network.STA_IF)             #Configurando wifi
        wlan.disconnect()                               #Garantindo que ele nao esta connectado a nenhuma rede

        if wlan.active() == False:                      #Checando se o wifi esta ativado para se connectar
            wlan.active(True)                           #se estiver inativo, ative

        while not wlan.isconnected():                   #deve retornar false, pois ele nao esta connectado a uma rede

            try:                                        #Checando se o arquivo ja existe
                arq = open("redes.json").read()
                print("Lista de redes encontrada...")

            except:                                     #Caso nao exista, crie um arquivo, insira uma rede e salve no arq
                print("Criando lista de redes...")
                print(" ")
                print("Redes disponiveis: ")
                print(" ")

                search = wlan.scan()

                for ss in range (len(search)):          #Leitura das redes disponiveis
                    print(search[ss][0])

                print(" ")
                rootssid = input("Insira o nome da rede: ")
                rootkey = input("Insira a senha: ")

                arq = open("redes.json","w")
                data = [{"SSID":rootssid,"KEY":rootkey}]
                arq.write(ujson.dumps(data))
                arq.close()
            
            arq = open("redes.json").read()             #Abra so para ler
            arqload = ujson.loads(arq)
            amount = int(len(arqload))                  #quantidade de redes salvas convertida para um n inteiro

            print("Redes Salvas: ")

            if amount > 0:                              #Para dar certo tem q haver ao menos uma rede 
                for cont in range (amount):             #mostrando as redes disponiveis salvas
                    cont = str(cont)
                    print(" ")
                    print("Rede: "+cont)
                    cont = int(cont)
                    print(arqload[cont]["SSID"])
            
            print(" ")
            option = int(input("Deseja se conectar a qual rede: "))             #Rede para a connecçao

            if (option>=0)and(option<=amount):                                  #A rede tem q ser de 0 ao ultimo vetor
                wlan.connect(arqload[option]["SSID"],arqload[option]["KEY"])    #tente connectar
                for i in range(30):                                             #resposta visual
                    if(i%5 == 0 ):
                        print("...")
                    led.value(1)
                    time.sleep_ms(300)
                    led.value(0)
                    time.sleep_ms(300)
                    if wlan.isconnected() == True:                      #Fique checando se a conneccao foi estabelecida
                        print("Conneccao estabelecida... ")
                        print("Dados coletados: ")
                        print(wlan.ifconfig())
                        break                                           #caso seja estabelecida sai do loop

            else:
                print(" ")
                print("Option indisponivel")
            if wlan.isconnected() == False:
                print("Nao consegui estabelecer coneccao, repita o processo por favor")
                print(" ")
            loop = input("Deseja repetir o processo de coneccao: YES (y), NO (n)")
            if loop == "y":
                print("\n" * 25)
                wlan.disconnect()



    def wifi_save(self):    # Metodo de salvar dados

        wlan = network.WLAN(network.STA_IF)             #Configurando wifi novamente

        arq = open("redes.json").read()                 #abrindo arquivo listas
        arqload = ujson.loads(arq)

        print("Redes disponveis: ")
        search = wlan.scan()
        for ss in range (len(search)):          #Leitura das redes disponiveis
            print(search[ss][0])

        newssid = input("Insira a nova rede: ") 
        newkey = input("insira a senha: ")

        newdata = {"SSID":newssid,"KEY":newkey}

        arqload.append(newdata)                 #add novo dado a lista redes

        print ("Nova rede adicionada, sua lista atualizada e: ")
        for i in range (len(arqload)):                  #mostrando lista atualizada
            print(arqload[i]["SSID"])
            print(" ")

        arq = open("redes.json","w")
        arq.write(ujson.dumps(arqload))                 #sobrecrevendo lista antiga com a nova lista atualizada
        arq.close()                                     #fechando arq a fim de evitar bugs
    


    def wifi_remove(self):      #metodo de remover dados
        arq = open("redes.json").read()         #abrindo arquivo que contem as listas

        arqload = ujson.loads(arq)
        amount = int(len(arqload))

        print("Redes disponiveis")
        for i in range (amount):        #mostrando as redes
            i = str(i)                  #inversao de um inteiro para string
            print(" ")                  # o objetivo e poder concatenar o texto com isso
            print("Rede: "+i)           # entao basta converter para string
            i = int(i)                  # obrigatoriamente tem que trasformar em um inteiro logo apos
            print(arqload[i]["SSID"])   # caso contrario ira dar erro
        print("  ")
        remove = int(input("Qual rede deseja remover: "))
        arqload.pop(remove)             #retorna o valor removido

        stramount = str(len(arqload))
        print("Lista de redes atualizada...")
        print("Sua lista contem: "+stramount+" Redes")

        amount = int(len(arqload))
        for i in range (amount):        #printa a nova lista
            i = str(i)
            print(" ")
            print("Rede: "+i)
            i = int(i)
            print(arqload[i]["SSID"])
        
        arq = open("redes.json","w")        #escrevendo a nova lista no arquivo
        arq.write(ujson.dumps(arqload))
        arq.close()

    def wifi_menu(self):

        try:
            arq = open("redes.json").read()
        except:
            print("Verificado, primeira vez debugando o cod")
            print("Irei mandalo para a configuraçao incial")
            print("connect manualmente")
            #chame a funçao wifi_manual

        print("Menu:")
        print(" ")
        print("Connection Manual: Digite (M)")
        print("Save new network: Digite (S)")
        print("Remove a network : Digite (R)")
        print("Exit: Digite (E)")
        option = input("Option:. ")
        #Fazer um loop para chamar as funcoes acima