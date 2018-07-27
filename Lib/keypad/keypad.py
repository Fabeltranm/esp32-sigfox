from machine import Pin
import time

filas = [ 13, 12, 14, 27 ]
columnas = [ 26, 25, 35, 34 ]

pin_fila = [ Pin(nombre_pin, mode=Pin.OUT) for nombre_pin in filas ]

pin_columna = [ Pin(nombre_pin, mode=Pin.IN, pull=Pin.PULL_DOWN) for nombre_pin in columnas ]

matriz = [["1", "2", "3", "A"]
		 ,["4", "5", "6", "B"]
		 ,["7", "8", "9", "C"]
		 ,["*", "0", "#", "D"]]


espera = 160 // len(filas)

def get_pin_value():

	valores = [pin_columna[0].value(),pin_columna[1].value(),pin_columna[2].value(),pin_columna[3].value()]
	#valores1 = [pin_fila[0].value(),pin_fila[1].value(),pin_fila[2].value(),pin_fila[3].value()]
	#print(valores)
	#print(valores1)
	try:
		index_t = valores.index(1)
		return index_t + 1
	except:
		return None

def getkey():

	for p in pin_fila:
		p.value(0)

	while True:

		lfila = -1

		for fila in pin_fila:
			lfila += 1
			fila.value(1)
			#print(lfila)

			time.sleep_ms(espera)

			index1 = get_pin_value()

			if index1:
				time.sleep_ms(10)
				index2 = get_pin_value()

				if index1 == index2:
					fila.value(0)
					return matriz[lfila][index1-1]

			fila.value(0)



def getkey_(timeout = 500):
	timeoutaux = time.ticks_ms()
	while True:

		if time.ticks_ms() > timeoutaux + timeout:
			break

		lfila = -1

		for fila in pin_fila:
			lfila += 1
			fila.value(1)
			#print(lfila)

			time.sleep_ms(espera)

			index1 = get_pin_value()

			if index1:
				time.sleep_ms(10)
				index2 = get_pin_value()

				if index1 == index2:
					return matriz[lfila][index1-1]

			fila.value(0)


def define_pines(vector):
    if len(vector) == 8:
        filas = vector[0:4]
        columnas = vector[4:8]

        pin_fila = [ Pin(nombre_pin, mode=Pin.OUT) for nombre_pin in filas ]

        pin_columna = [ Pin(nombre_pin, mode=Pin.IN, pull=Pin.PULL_DOWN) for nombre_pin in columnas ]

    else:
        print("error: Deben ser 8 pines")