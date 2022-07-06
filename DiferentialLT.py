import numpy as np
#Input
print("Ingrese los coeficientes de su polinomio, incluidos los elementos 0 \n En la forma: a,a1,a2...,an")
Coeff=str(input("Coeficientes: "))
Coeff=np.array(Coeff.split(","), int)
# Matriz Asociada
INV=np.arange(len(Coeff)-1,0,-1)
MAT=np.zeros((len(Coeff)-1, len(Coeff)-1), dtype=int)
for i in range(len(INV)):
    for j in range(len(INV)):
        MAT[i][i]=INV[i]
Col=np.zeros(len(INV), dtype=int)
MAT=np.column_stack((MAT,Col))
#Producto
Coeff_n=np.matmul(MAT, Coeff, dtype=int)
print("Los coeficienets de la derivada del polinomio son:")
print(Coeff_n)

