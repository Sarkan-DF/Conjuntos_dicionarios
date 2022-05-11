aparicoes = {"nome" : 1 , "amo" : 2, "e" : 1, "minha" : 2}
# print(aparicoes["amo"])

print(aparicoes.get("igor"))

aparicoes["cecilia"] = 5 #incluir item no dicionario
print(aparicoes)

aparicoes["cecilia"] = 2 #modificar item do dicionario
print(aparicoes)

del aparicoes["cecilia"] #Deletar item do dicionario
print(aparicoes)

print("amo" in aparicoes) #Verificar se item está no dicionario
print("cecilia" in aparicoes) #Verificar se item está no dicionario

for elementos in aparicoes: #Iterando pelas chaves do dicionario
    print(elementos)

for elementos in aparicoes.values(): #Iterando pelos valores do dicionario
    print(elementos)

for elementos in aparicoes.items(): #Iterando pelos itens completos do dicionario
    print(aparicoes)

for chave, valor in aparicoes.items(): #desempacotando dicionario;
    print(chave, "=", valor)