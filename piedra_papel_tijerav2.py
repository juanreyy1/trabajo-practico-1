# piedra_papel_tijera.py
# Juego simple contra la computadora: primera versión

import random
from math import floor


# Variables
rondas_totales = 5
opciones = ["piedra", "papel", "tijera"]
ronda = 1
puntos_usuario = 0
puntos_pc = 0

def check_winner(puntos_usuario, puntos_pc, rondas_totales):
    """Chequea si alguien ya ganó por diferencia de puntos."""
    result = False
    
    # Verifica si el usuario ya no puede ser alcanzado
    if puntos_usuario >= (floor(rondas_totales/2)+1):  
        print("Ganaste la partida! Ya no puedes ser alcanzado.")
        result = True

    # Verifica si la PC ya no puede ser alcanzada
    elif puntos_pc    >= (floor(rondas_totales/2)+1):
        print("Ganó la PC la partida! Ya no puede ser alcanzada.")
        result = True

    # Devuelve el resultado
    return result

# Inicio del juego

print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")
print("Escribí tu jugada (piedra/papel/tijera).")

while ronda <= rondas_totales: 
    # Imprime la ronda actual y pide la jugada del usuario
    print(f"\nRonda {ronda}")
    jugada_usuario = input("Tu jugada: ").strip().lower()

    # Validación de la entrada del usuario
    if jugada_usuario not in opciones:
        print("Entrada no válida. Debe ser piedra, papel o tijera.")
        continue  

    # Jugada de la computadora
    jugada_pc = random.choice(opciones)
    print(f"La computadora eligió: {jugada_pc}")

    # Check de resultados de la ronda
    if jugada_usuario == jugada_pc:
        print("Empate.")
    elif (jugada_usuario == "piedra" and jugada_pc == "tijera") or \
         (jugada_usuario == "papel"  and jugada_pc == "piedra") or \
         (jugada_usuario == "tijera" and jugada_pc == "papel"):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1

    # Chequea si alguien ya ganó por diferencia de puntos
    if check_winner(puntos_usuario, puntos_pc, rondas_totales):
        break
    
    # Incrementa la ronda
    ronda += 1

# Resultado final
print("\n=== Resultado final ===")
print(f"Puntos del Usuario: {puntos_usuario} | Puntos de la PC: {puntos_pc}")

# Determina el ganador final
# Gana el usuario
if puntos_usuario > puntos_pc:
    print("¡Felicidades! Ganaste el juego.")
# Gana la PC
elif puntos_usuario < puntos_pc:
    print("La computadora ganó el juego.")
# Empate
else:
    print("Empate total.")
