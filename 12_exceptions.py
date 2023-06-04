# excepciones
num1 = 5
num2 = 54
num2 = "7"

try:
    print(num1 + num2)
except Exception as error:
    print(error)
else:
    print("Si no existio una excepcion, continua la ejecucion")
finally:
    print("Se ejecuta independiente exista o no excepcion o exito")