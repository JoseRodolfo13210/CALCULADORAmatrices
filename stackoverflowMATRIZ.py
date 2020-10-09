import numpy as np

#Creamos funciones para la calculadora
def multi(A,B):
    resultado = np.dot(A,B)
    print(resultado)

def suma(A,B):
    matriz_suma = A + B
    print(matriz_suma)

def resta(A,B):
    matriz_suma = A - B
    print(matriz_suma)

#Generamos matrices aleatorias para probar funciones
A = np.array([[1,2],[3,4]],float)

B = np.array([[5,6],[7,8]],float)

#Probamos funciones
multi(A,B)
suma(A,B)
resta(A,B)


