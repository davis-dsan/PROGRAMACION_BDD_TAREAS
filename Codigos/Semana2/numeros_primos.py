numero = int(input("Favor escriba un numero: "))
variable1 = 1
variable2 = 0

while variable1 <= numero:
    if  numero % variable1 == 0:
        variable2 = variable2 + 1
    variable1 = variable1 + 1
if variable2 == 2:
    print("El numero es primo. ")
else:
    print("El numero no es primo. ")