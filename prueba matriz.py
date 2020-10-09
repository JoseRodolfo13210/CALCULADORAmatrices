filas = int(input ("Introduzca el numero de filas de sus matrices: "))
columnas = int(input ("Introduzca el numero de columnas de sus matrices: "))


A=[[0 for i in range (filas)] for j in range (columnas)]
B=[[0 for i in range (filas)] for j in range (columnas)]
R=[[0 for i in range (filas)] for j in range (columnas)]

print ("Matriz 1")
for i in range (columnas):
    for j in range(filas):
        A[i][j]= int (input("Ingresar datos de matriz 1: "))

print ("Matriz 2")
for i in range (columnas):
    for j in range(filas):
        B[i][j]= int (input("Ingresar datos de matriz 2: "))


for i in range (columnas):
    for j in range(filas):
        R[i][j]=A[i][j]+B[i][j]

print("El resultado es: ")

for i in range (columnas):
    for j in range (filas):
        print (R[i][j])

