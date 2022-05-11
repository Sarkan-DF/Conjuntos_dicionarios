usuarios = {5, 65, 85, 44, 15, 47, 88}
print(len(usuarios))

usuarios.add(18)
print(usuarios)
print(len(usuarios))

usuarios = frozenset(usuarios)

print(type(usuarios))
usuarios.add(16) #Não é possivel usar add pq o conjunto foi congelado "frozenset"