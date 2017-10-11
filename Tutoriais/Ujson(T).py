#NO esp a biblioteca json se chama Ujson na minha versao do esp
import ujson #Importando biblioteca Json 


#Criando um arquivo e add informaçoes

ls = open("lista.json","w")                          #criando arquivo
data = []                                            # lista para colocar dentro do arquivo
ls.write(ujson.dumps(data))                          # escreva no arquivo json a informaçao dentro de data
ls.close()                                           # dumps, cria um texto apartir de um objeto json 

#Add uma nova inforaçao ao arquivo

newid = 'sif'
newpass = '12345678'

arq = open("lista.json","r+")                        #abrindo em modo leitura escrita
new_data = {"ID":newid,"KEY":newpass}                #novos parametros

conv = ujson.loads(arq.read())                       #trasforma texto em objeto
conv.append(new_data)                                #add novos parametros ao objeto que vc tem acima
arq.seek(0)                                          #parametro 0 fundamental
arq.write(ujson.dumps(conv))                         # escrevendo-os
arq.close()

#Lendo arquivos

arq = open('lista.json','r+').read()
arq = ujson.loads(arq)
print (arq[0]["ID"])
