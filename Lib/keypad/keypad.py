from machine import Pin
import utime

filas = [ 13, 12, 14, 27 ]
columnas = [ 26, 25, 35, 34 ]

pin_fila = [ Pin(nombre_pin, mode=Pin.OUT) for nombre_pin in filas ]

pin_columna = [ Pin(nombre_pin, mode=Pin.IN, pull=Pin.PULL_DOWN) for nombre_pin in columnas ]

caracter = ["1", "2", "3", "A", "4", "5", "6", "B", "7", "8", "9", "C", "*", "0", "#", "D"]


espera = 40 // len(filas)

def getkey():
    while True:

        letra = 0

        for fila in pin_fila:
            fila.value(1)

            utime.sleep_ms(espera)

            for columna in pin_columna:
                if columna.value():
                    #print(caracter[letra])
                    return caracter[letra]
                letra += 1
            fila.value(0)

def getkey_(timeout = 500):
    timeoutaux = 0
    while True:

        letra = 0

        for fila in pin_fila:
            fila.value(1)

            utime.sleep_ms(espera)
            timeoutaux += 1

            for columna in pin_columna:
                if columna.value():
                    #print(caracter[letra])
                    return caracter[letra]
                letra += 1
            fila.value(0)

        if timeoutaux >= timeout//espera:
            return ""


def define_caracter(vector):
    if len(vector) == 16:
        caracter = vector
    else:
        print("error: Deben ser 16 caracteres")

def define_pines(vector):
    if len(vector) == 8:
        filas = vector[0:4]
        columnas = vector[4:8]

        pin_fila = [ Pin(nombre_pin, mode=Pin.OUT) for nombre_pin in filas ]

        pin_columna = [ Pin(nombre_pin, mode=Pin.IN, pull=Pin.PULL_DOWN) for nombre_pin in columnas ]

    else:
        print("error: Deben ser 8 pines")