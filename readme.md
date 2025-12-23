# Piedra, Papel o Tijera en Python

## Autor
Juan Manuel Reynoso

## Descripción
Este programa implementa el juego clásico "Piedra, Papel o Tijera" en Python, permitiendo que un usuario juegue contra la computadora.

El jugador puede elegir cuántas rondas desea jugar (entre 1 y 100).  
El juego se desarrolla bajo la modalidad **“mejor de N”**, lo que significa que la partida puede finalizar antes si alguno de los participantes alcanza la cantidad mínima de puntos necesaria para asegurar la victoria.

La computadora elige su jugada de manera aleatoria en cada ronda, y el programa valida todas las entradas del usuario para evitar errores.

## Funcionalidades principales
- Selección de cantidad de rondas por parte del usuario.
- Validación de entradas (jugadas y número de rondas).
- Elección aleatoria de jugadas para la computadora.
- Conteo de puntos del usuario y de la computadora.
- Finalización anticipada del juego cuando ya hay un ganador.
- Mostrar el resultado final de la partida.

## Reglas del juego
- Piedra gana a Tijera.
- Tijera gana a Papel.
- Papel gana a Piedra.
- Si ambos eligen la misma opción, es empate.

## Requisitos
- Python instalado en el sistema. (Cualquier version)

## Cómo ejecutar el programa

1. Descargar el repositorio.
2. Abrir una terminal en la carpeta donde se encuentra el archivo.
3. Ejecutar el siguiente comando:

```bash
python nombre_del_archivo.py
