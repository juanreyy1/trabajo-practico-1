# Piedra, Papel o Tijera

Juego simple de **Piedra, Papel o Tijera** desarrollado en **Python**, donde el usuario juega contra la computadora bajo la modalidad **“mejor de N rondas”**.

---

## Autor

**Juan Manuel Reynoso**

---

## Descripción del programa

Este programa permite jugar al clásico juego de **Piedra, Papel o Tijera** contra la computadora.  
El usuario ingresa su jugada en cada ronda y la computadora elige la suya de forma aleatoria.

El juego finaliza cuando:
- Se completan todas las rondas;
- Alguno de los jugadores alcanza una cantidad de puntos tal que el otro ya no puede alcanzarlo (mejor de N).

Al finalizar, se muestra el resultado final y el ganador.

---

## Reglas del juego

- Piedra le gana a Tijera  
- Tijera le gana a Papel  
- Papel le gana a Piedra  
- Si ambos eligen lo mismo, es empate  

---

## Funcionamiento general

1. Se define la cantidad total de rondas.
2. El usuario ingresa su jugada (`piedra`, `papel` o `tijera`).
3. La computadora elige una jugada al azar.
4. Se comparan las jugadas y se asignan puntos.
5. Se verifica si alguno ya ganó la partida por diferencia de puntos.
6. Al finalizar, se muestra el resultado final.

---

## Requisitos

- Python (cualquier version)
- No requiere librerías externas (solo módulos estándar de Python).

---

## Cómo ejecutar el programa

1. Guardar el archivo con el nombre:
2. Abrir una terminal en la carpeta donde se encuentra el archivo.
3. Ejecutar el siguiente comando:

```bash
python piedra_papel_tijera.py


