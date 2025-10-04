# Enunciado:
# Crea una función que reciba una frase y determine si es un palíndromo.
# Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda, ignorando espacios y comas.

# 📌 Ejemplo:
# Entrada: "Anita lava la tina" → Salida: "Es un palíndromo"
# Entrada: "Hola mundo" → Salida: "No es un palíndromo"


def palindromo(word):
    word = word.replace(" ", "").lower()
    # word_reverse = word[::-1]

    word_reverse = list(word)
    word_reverse.reverse()
    # print(word_reverse)
    
    # word_reverse = []
    # for index in range(len(word) -1,-1, -1):
    #     word_reverse.append(word[index])
    
    word_reverse = "".join(word_reverse)
    # # print(word_reverse)

    if word == word_reverse:
        return True
    
    return False



def run():
    word = input("Ingrese una palabra: ")
    result = palindromo(word)

    if result:
        print(f"La palabra {word} es palíndromo")
    else:
        print(f"La palabra {word} NO es palíndromo")


if __name__ =="__main__":
    run()

