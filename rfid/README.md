# Libreria para modulo MFRC522

Libreria para el uso del modulo RFID [MFRC522](http://www.nxp.com/documents/data_sheet/MFRC522.pdf), con MicriPython. Modificada del repositorio [micropython-mfrc522](https://github.com/wendlers/micropython-mfrc522) del usuario wendlers.

Esta libreria soporta las tarjetas ESP8266, Wipy y la Sparkfun ESP32 Thing.

## Uso

Lo primero es cargar los modulos ``mfrc522.py`` y ``rfid.py``.

Las conexiones para cada tarjeta se muestran acotinuacion:

| Señal     | GPIO ESP8266 | GPIO WiPy      | ESP32 Thing | Notas                                 |
| --------- | ------------ | -------------- | ----------- | ------------------------------------- |
| sck       | 0            | "GP14"         | 18          |                                       |
| mosi      | 2            | "GP16"         | 23          |                                       |
| miso      | 4            | "GP15"         | 19          |                                       |
| rst       | 5            | "GP22"         | 22          |                                       |
| cs        | 14           | "GP14"         | 2           |Marcado como SDA en tarjetas RFID-RC522|

### Escritura

Para escribir un dato de 16 bits en una direccion de una tarjeta RFID se usa la funcion ``do_write(addr,name)``. Donde ``addr``es la direción donde se escribe, y ``name`` el dato de 16 bits.

Ejemplo de la escritura del nombre Juan en la dirección 8:

```python
>>> import rfid
>>> rfid.do_write(8,"Juan")
            Juan
[32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 74, 117, 97, 110]
Data written to card
>>> 
```

### Lectura

Para leer un dato de 16 bits en una direccion de una tarjeta RFID se usa la funcion ``do_read(addr)``. Donde ``addr``es la direción que se quiere leer.

Ejemplo de la lectura del nombre escrito en el ejemplo anterior:

```python
>>> import rfid
>>> rfid.do_read(8)
'Juan'
>>> 
```
