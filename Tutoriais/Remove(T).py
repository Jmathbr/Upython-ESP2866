import json
                                        # Para remover um dado do vetor

file = 0                                # setando o zero
file = open("teste.json").read()        # abrindo o arquivo em modo leitura
arq = json.loads(file)                  # convertendo em objeto
print(arq[1])                              # printando o que tem dentro do arquivo

rm = 2                                  # posiccao do vetor que deseja remover

arq.pop(rm)                             # funcao que remove o vetor

vecup = arq                             # guardando o vetor atualizado com a remocao q foi inserida
print(vecup)                            # printando esse vetor atualizado


file = 0                                # setando o file como zerom para que nao pegue lixo

file = open("teste.json","w")           # abrindo em modo escrever, que vai acabando sobrescrever o arquivo antigo
file.write(json.dumps(vecup))           # escrevendo o vetor atualizado dentro do arquivo teste
file.close()                            # fechando aquivo teste

                                        # Para add um novo vetor

file = open("teste.json").read()        # abrindo so para ler
fileload = json.loads(file)             # conversao para obj
x= 4                                    # o    q vai ser adicionado
fileload.append(x)                      # add ao final do vetor

print(fileload)

file = open("teste.json","w")           # abrindo para sobescrever o arq antigo
file.write(json.dumps(fileload))        # sobrescrevendo com novos dados
file.close()

file = open("teste.json").read()
fileloads = json.loads(file)
print(len(fileloads))