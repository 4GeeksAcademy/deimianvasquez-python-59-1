import random


# num_random = random.randint(1, 10)
# print(num_random)

# list_name = ["Eylin", "Marta", "Carlos", "Deimian","Jesús", "Verónica", "Deimian", "Hector", "Deimian", "Alejandro", "Deimian"] # Evaluar si se muta


# list_name[0] ="Juanita"
# list_name[3] = "Externocleidomastoideo"
# # print(len(list_name))
# # print(list_name[len(list_name)-1])
# # print(list_name[-1])
# # print(list_name[0])
# # print(list_name[3])

# list_name.append("Eliana")
# list_name.insert(1, "Esteban")
# # result = list_name.pop()
# list_name.remove("Deimian")
# print(list_name)
# result = list_name.count("Deimian")
# print(result)
# del list_name[2:5]
# print(list_name)


list_name = ["Eylin", "Marta", "Carlos", "Deimian","Jesús", "Verónica", "Deimian", "Hector", "Deimian", "Alejandro", "Deimian"] # Evaluar si se muta

# count = len(list_name)-1
# print(len(list_name)-1)

# while count >= 0:
#     print(f"Hola ¿qué tal {list_name[count]}?")
#     count = count -1



# while True: 
#     print("""
#         Selecciona una opción valida

#         1- Sumar
#         0- Salir
#     """)
#     opcion = input("Ingrese una operación: ")
#     try:
#         opcion = int(opcion)
#         if opcion == 1:
#             num1 = int(input("Ingresar el número 1: "))
#             num2 = int(input("Ingresar el número 2: "))

#             print(f"El total de la suma es: {num1+num2}")
#         else:
#             print("Gracias por venir")
#             break

#     except Exception as err:
#        print("Debe enviar una opción valida ")
 

# for name in list_name:
#     print(name)

# for index in range(len(list_name)-1, -1, -1 ):
#     print(f"{list_name[index]} : {index}")


# human = {
#     "fullname" : "Juanito Peña",
#     "age": 20,
# }

# for key, value in human.items():
#     print(f"{key} : {value}")


# for index, value in enumerate(list_name):
#     print(f"{index} : {value}")


# MAP
# def saludar(item):
#     return f"{item} : {len(item)}"


# result = list(map(saludar, list_name))

# for item in result:
#     print(item)


# FILTER

# def result_filter(item): 
#     return item == "Deimian"


# result = list(filter(result_filter, list_name))
# print(result)


result =  [f"Hola ¿qué tal {item}?" for item in list_name if len(item) <= 6 ]
print(result)