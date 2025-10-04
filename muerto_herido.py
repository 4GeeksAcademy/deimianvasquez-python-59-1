import random
# 1 - Cuando el juego arranca la máquina debe elgir un número entre 0 - 9
# 2 - Debe perdir al usuario que ingrese un número de tres dígitos, se lo pide por la terminal
# 3 - Si se acierta el número pero no la posición cuenta como un herido
# 4 - Si acierta posición y número cuenta como un muerto
# 4 - si tiene tres muertos gana


lista_numeros = [0,1,2,3,4,5,6,7,8,9]
seleccion_maquina = random.sample(lista_numeros, 3)

while True:
    muerto = 0
    herido = 0

    entrada_usuario = input("Ingresa un número de tres dígito: ")
    if len(entrada_usuario) != 3:
        print("El número debe ser de tres dígitos.")
        continue

    seleccion_usuario = []

    for num in entrada_usuario:
        seleccion_usuario.append(int(num))

    # print(seleccion_maquina, "Esta es la selección de la maquina")
    # print(seleccion_usuario, "Esta es la selección de la USuario")

    for index_maquina, valor_maquina in enumerate(seleccion_maquina):
        for index_usuario, valor_usuario in enumerate(seleccion_usuario):
            if index_maquina == index_usuario and valor_maquina == valor_usuario:
                muerto = muerto + 1
            elif valor_maquina == valor_usuario:
                herido = herido + 1

    if muerto == 3:
        print("GANAMOSSSSSSS!!!!!!")
        break
    
    print(f"Heridos: {herido} \nMuertos: {muerto}\n\n")





# # maquina
# 0-2
# 1-3
# 2-4 

# # usuario
# 0-2
# 1-3
# 2-4


# herido 0
# muerto 3 --> wins