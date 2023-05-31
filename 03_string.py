#Strings

first_string = "Hola diavlo"
second_string = "Hola diavlo v2.0"

#tamaño de un string
print(len(first_string))

#interpolacion
print("Interpolacion {} y {}".format(first_string, second_string)) #sin formato de datos
print("Interpolacion %s y %s" %(first_string, second_string)) #con datos formateados
print(f"Interpolacion {first_string} y {second_string}") #interpolacion pura

lenguaje = "Python"
a,b,c,d,e,f = lenguaje
print(a)

# Cortar un string desde cierto indice hasta el final
lenguaje_parte = lenguaje[2:]
print(lenguaje_parte)

# Cortar un string desde cierto indice hasta un final
lenguaje_parte = lenguaje[2:4]
print(lenguaje_parte)

# Escribir el final de un string
lenguaje_parte = lenguaje[-1]
print(lenguaje_parte)

# Escribir al reves un string
lenguaje_parte = lenguaje[::-1]
print(lenguaje_parte)