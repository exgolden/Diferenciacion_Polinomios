import numpy as np
#Input
print("Ingrese los coeficientes de su polinomio, incluidos los elementos 0 \n En la forma: a,a1,a2...,an")
Coeff=str(input("Coeficientes: "))
Coeff_l=Coeff.split(",")
# Matriz Asociada
Mat=np.zeros((len(Coeff_l), len(Coeff_l)), dtype=int)
for i in range(len(Coeff_l)):
    for j in range(len(Coeff_l)):
        Mat[i][i]=Coeff_l[i]
Row=np.zeros(len(Coeff_l), dtype=int)
Mat=np.append(Mat, [Row], axis=0)
#Producto
Coeff_n=np.matmul(Mat, np.array(Coeff_l, dtype=int), dtype=int)
print("Los coeficienets de la derivada del polinomio son:")
print(Coeff_n[0:-1])