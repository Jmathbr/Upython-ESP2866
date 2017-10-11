import json

file = 0
file = open("redes.json").read()

fileload = json.loads(file)

print("Redes salvas: ")
print (" ")

for cont in range (len(fileload)):
    print(fileload[cont]["SSID"])

remove = 3

fileload.pop(remove)
up = fileload

print (" ")
print("Lista de redes atualizada: ")
print (" ")

for cont in range (len(fileload)):
    print(up[cont]["SSID"])

file = open("redes.json","w")
file.write(json.dumps(up))
file.close()





