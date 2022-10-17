print("¡Adivina la respuesta correcta!")

print("En que año tuvo lugar la pandemia del coronavirus")
print("a) 2018")
print("b) 2020")
print("c) 2022")

respuesta = None

respuesta = input("Introduce una de las opciones (a, b, c): ")

while (respuesta !="a" and respuesta !="b" and respuesta!="c"):
	respuesta = input ("Introduce una de las opciones (a, b, c): ")

if (respuesta == "a" or respuesta=="c"):
	print("Has fallado :(")
elif  respuesta =="b":
	print ("Has acertado :)")


print("Gracias por jugar <3")
