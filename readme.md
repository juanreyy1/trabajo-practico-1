{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 TimesNewRomanPSMT;}
{\colortbl;\red255\green255\blue255;\red53\green53\blue53;}
{\*\expandedcolortbl;;\cssrgb\c27100\c27100\c27100;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs33\fsmilli16658 \cf2 READ.ME\

\fs23\fsmilli11759 # Piedra, Papel o Tijera \'97 Juego en Python\
ALUMNO = Juan Manuel Reynoso\
Este programa implementa el cl\'e1sico juego *Piedra, Papel o Tijera* para jugar\
contra la computadora.\
Est\'e1 pensado como una serie al mejor de **N** rondas (por defecto, 5). Si el\
n\'famero de rondas indicado\
es par, el programa lo ajusta al siguiente impar para garantizar que siempre\
haya un ganador.\
Adem\'e1s, **corta de forma anticipada** cuando matem\'e1ticamente el rival ya no\
puede alcanzarte, incluso\
si nadie lleg\'f3 a\'fan a las victorias necesarias.\
#\'bfC\'f3mo funciona?\
- **Modo \'93mejor de N\'94**: se calcula `victorias_necesarias = N // 2 + 1`.\
- **Ajuste de par a impar**: si `N` es par, se convierte en `N + 1`.\
- **Corte anticipado**: si la diferencia de puntos es mayor a las rondas\
restantes, la serie se define antes.\
- **Validaci\'f3n de entrada**: solo se aceptan `piedra`, `papel` o `tijera` (no se\
consume ronda ante entradas inv\'e1lidas).\
- **Empates**: se contabilizan, pero no suman puntos a ning\'fan jugador.}