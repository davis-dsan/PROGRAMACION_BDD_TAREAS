print ("Numero Mayor")
num1 = int(input("Ingrese el Primer numero: \n"))
num2 = int(input("Ingrese el Segundo numero: \n"))
num3 = int(input("Ingrese el Tercer numero: \n"))
if (num1 > num2):
    mayor = num1
else:
    mayor = num2

if (num3 > mayor):
    mayor = num3

print ("El numero mayor es: ", mayor)