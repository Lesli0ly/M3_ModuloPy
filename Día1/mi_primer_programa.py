# Este código imprime el famoso hola mundo
print ("hola mundo")
nombre = input("ingrese su nombre:")
print("Tu nombre es",nombre)
print(f"Tu nombre es {nombre}")
edad = input("Ingrese su Edad:  ")
print("Tu tienes",edad,"años")
print(type(edad))
#string.format
print("".format())
print("Hola {}, El año es {} del mes {} y el dia {}".format(nombre,año,mes,dia))

Israel Palma Quezada 18:36
print("Hola %s, El año es %s del mes %d y el dia %d" %(nombre, año, mes,dia))
