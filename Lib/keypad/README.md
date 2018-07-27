Recomendación: Si se usa un GPIO de solo entrada, se debe conectar una resistencia al pin y a tierra.

# Librería keypad para MicroPython

Esta librería permite hacer uso de una matriz 4x4, en MicroPython. 

## Uso

```python
import keypad

key = keypad.getkey()
print(key)
```
Espera a que se presione un botón y retorna el string.

```python
import keypad

key = keypad.getkey_(timeout=500)
print(key)
```
Espera a que se presione un botón, durante el valor de timeout en ms (Default = 500). Si no se presiona la tecla en el tiempo, retorna un string vacío "".
