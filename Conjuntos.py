usuarios_data_science = [15, 23, 64, 88]
usuarios_machine_learning = [12, 15, 23, 99]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

print(set(assistiram))

for usuario in set(assistiram):
    usuario += 1
    print(usuario)