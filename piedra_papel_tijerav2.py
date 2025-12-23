import random
#Importo el modulo para elegir jugadas aleatorias de la computadora

opciones = ["piedra", "papel", "tijera"]    #Creacion de lista con jugadas validas 

print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")
print("Escribí tu jugada (piedra/papel/tijera).")

#Inicio del contador de rondas en 1 
ronda = 1
puntos_usuario = 0
puntos_pc = 0

# Pedir rondas con validación (1 a 100)
while True:
    try:
        rondas_totales = int(input("¿Cuántas rondas querés jugar? Elegí un número entre 1 y 100: ")) #Pido al usuario cuantas rondas quiere jugar y lo transformo en entero
        if 1 <= rondas_totales <= 100:    #Validacion del rango permitido
            break
        else:
            print("Entrada inválida. Debe estar entre 1 y 100.")
    except ValueError:
        print("Entrada inválida. Tenés que escribir un número entero.")

dif = rondas_totales // 2 + 1  # Calcula cuántas rondas debe ganar alguien para asegurarse la victoria

while ronda <= rondas_totales: #Se repite el bucle mientras no supere las rondas totales 
    print(f"\nRonda {ronda}")

    jugada_usuario = input("Tu jugada: ").strip().lower()   #Jugada usuario sin espacios extras y lo paso a minusculas 
    while jugada_usuario not in opciones:
        print("Entrada no válida. Debe ser piedra, papel o tijera.")
        jugada_usuario = input("Tu jugada: ").strip().lower()

    jugada_pc = random.choice(opciones)   #La computadora elige una jugada al azar de la lista.
    print(f"La computadora eligió: {jugada_pc}")

    if jugada_usuario == jugada_pc:     
        print("Empate.")
    #Combinaciones donde gana el usuario        
    elif (jugada_usuario == "piedra" and jugada_pc == "tijera") or \
         (jugada_usuario == "papel" and jugada_pc == "piedra") or \
         (jugada_usuario == "tijera" and jugada_pc == "papel"):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1 #Suma uno a la computadora 

    # corte anticipado: alguien ya llegó al mínimo necesario para ganar
    if puntos_usuario == dif or puntos_pc == dif:
        print("La partida termina porque alguien alcanzó los puntos necesarios para ganar.")
        break
    ronda += 1

print("\n=== Resultado final ===")
print(f"Puntos del Usuario: {puntos_usuario} | Puntos de la PC: {puntos_pc}")
#Informe del resultado final 
if puntos_usuario > puntos_pc:
    print("¡Felicidades! Ganaste el juego.")
elif puntos_usuario < puntos_pc:
    print("La computadora ganó el juego.")
else:
    print("Empate total.")
