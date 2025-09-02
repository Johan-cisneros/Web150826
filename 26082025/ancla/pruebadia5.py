import random

#palabras
palabras = ['gato', 'perro', 'pez', 'loro', "ratón","delfin"]
#elegir palabra al azar
palabra = random.choice(palabras)
palabra = palabra.lower()

#Variables
oculta = ["_"] * len(palabra)
intentos_maximos = 6
letras_usadas = []
intentos = 0

print("Empecemos a jugar a El Ahorcado")
print("La palabra a descubrir es: ")



def mostrar_estado():
    print(" ".join(oculta))
            
        
while intentos < intentos_maximos and "_" in oculta:
    mostrar_estado()
    letra = input("Adivina una letra: ").lower()
    
    if not letra.isalpha() or len(letra) != 1:
        print("Por favor, introduce una letra válida.")
        continue

    if letra in letras_usadas:
        print("Ya has usado esa letra. Intenta con otra.")
        continue

    letras_usadas.append(letra)

    if letra in palabra:
        print("Bien!!! la letra se encuentra en la palabra.")
        for i in range(len(palabra)):
            if palabra[i] == letra:
                oculta[i] = letra
    else:
        print("La letra no se encuentra en la palabra.")
        intentos += 1

    print(" ".join(oculta))
    print(f"Intentos restantes: {intentos_maximos - intentos}")

if "_" not in oculta:
    print("¡Felicidades! Has adivinado la palabra.")
else:
    print(f"Has perdido. La palabra era: {palabra}")
    intentos += 1
