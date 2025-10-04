list_name = ["Eylin", "Marta", "Carlos", "Deimian","Jesús", "Verónica", "Deimian", "Hector", "Deimian", "Alejandro", "Deimian"] # Evaluar si se muta


# def saludar(name):
#     return f"Hola ¿qué tal {name}?"


result = list(map(lambda name: f"Hola ¿qué tal {name}?", list_name))
# print(result)

result_two = list(filter(lambda item : len(item) < 6, list_name))
print(result_two)

# def sum(num1 = 0, num2 = 0):
#     return num1 + num2


# def sum(*args):
#     print(args)
#     total = 0

#     for item in args:
#         total = total + item

#     return total
    

# def saluda(**kwargs):
#     print(kwargs)
   
#     return f"Hola ¿qué tal {kwargs.get("name", "no encontre")} {kwargs["lastname"]}?"


# print(saluda(lastname="Vásquez", name="Deimian" ))

# print(saluda(name="Juana", lastname="Delgado"))



sum_lambda = lambda num1, num2 : num1+num2

print(sum_lambda(10,58))