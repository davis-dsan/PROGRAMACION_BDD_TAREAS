a = int(input("Ingresar el primer numero"))
b = int(input("Ingresar el segundo numero"))
c = int(input("Ingresar el tercer numero"))

if a > b and b > c:
    print("El numero mayor es: ", a, "\nEl numero medio es: ",b, "\nEl numero menor es: ", c)
elif b > a and a > c:
    print("El numero mayor es: ", b, "\nEl numero medio es: ",a, "\nEl numero menor es: ", c)
elif c > a and a > b:
    print("El numero mayor es: ", c, "\nEl numero medio es: ",a, "\nEl numero menor es: ", b)
elif c > b and b > a:
    print("El numero mayor es: ", c, "\nEl numero medio es: ",b, "\nEl numero menor es: ", a)
elif a > c and c > b:
    print("El numero mayor es: ", a, "\nEl numero medio es: ",c, "\nEl numero menor es: ", b)
elif b > c and c > a:
    print("El numero mayor es: ", b, "\nEl numero medio es: ",c, "\nEl numero menor es: ", a)
else:
    print("Error, los numeros son iguales")