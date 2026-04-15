import matplotlib.pyplot as pyplot
import numpy as np

datos = input("porfavor ingrese los datos estadisticos:")
print(datos)
datos_procesados = []
errores = []


for x in datos.split(","):
    try:
        datos_procesados.append(float(x))
    except ValueError:
        errores.append(x)

print("Datos válidos:", datos_procesados)

if errores:
    print("Value Error:dato/s no cuantificable/s:", errores) 
    exit()



datos_procesados = datos.split(",")
datos_procesados = [float(x) for x in datos_procesados]
datos_procesados.sort()
cantidad_datos = len(datos_procesados)
if cantidad_datos < 5:
    print("lenght type error: se esperaban al menos 5 argumentos, se detectaron " + str(cantidad_datos))
    exit()
valor = input("Presione enter: ")



minimio = datos_procesados[0]
maximo = datos_procesados[-1]
#tengo hambre  comer pero no puedo:adjunto mi haambre aqui----> :(
Q1_aprox = (cantidad_datos + 1) / 4
Q1_aprox_original = Q1_aprox


if Q1_aprox == int(Q1_aprox):
    Q1_aprox = Q1_aprox
elif Q1_aprox*2 == int(Q1_aprox*2):
    Q1_aprox = [int(Q1_aprox), int(Q1_aprox)+1]
else:
    Q1_aprox = [int(Q1_aprox), int(Q1_aprox)+1]






Q2_aprox = (cantidad_datos + 1) / 2
Q2_aprox_original = Q2_aprox

if Q2_aprox == int(Q2_aprox):
    Q2_aprox = Q2_aprox
else:
    Q2_aprox = [int(Q2_aprox), int(Q2_aprox)+1]







Q3_aprox = 3 * (cantidad_datos + 1) / 4
Q3_aprox_original = Q3_aprox

if Q3_aprox == int(Q3_aprox):
    Q3_aprox = Q3_aprox
elif Q3_aprox*2 == int(Q3_aprox*2):
    Q3_aprox = [int(Q3_aprox), int(Q3_aprox)+1]
else:    
    Q3_aprox = [int(Q3_aprox), int(Q3_aprox)+1]



if type(Q1_aprox) == list:
    Q1 = datos_procesados[int(Q1_aprox[0])-1] + (Q1_aprox_original - int(Q1_aprox[0])) * (datos_procesados[int(Q1_aprox[1])-1] - datos_procesados[int(Q1_aprox[0])-1])
else:
    Q1 = datos_procesados[int(Q1_aprox)-1]

if type(Q2_aprox) == list:
    Q2 = datos_procesados[int(Q2_aprox[0])-1] + (Q2_aprox_original - int(Q2_aprox[0])) * (datos_procesados[int(Q2_aprox[1])-1] - datos_procesados[int(Q2_aprox[0])-1])
else:
    Q2 = datos_procesados[int(Q2_aprox)-1]

if type(Q3_aprox) == list:
    Q3 = datos_procesados[int(Q3_aprox[0])-1] + (Q3_aprox_original - int(Q3_aprox[0])) * (datos_procesados[int(Q3_aprox[1])-1] - datos_procesados[int(Q3_aprox[0])-1])
else:
    Q3 = datos_procesados[int(Q3_aprox)-1]

RIC = Q3 - Q1

Limite_inferior = Q1 - 1.5 * RIC
Limite_superior = Q3 + 1.5 * RIC

Valores_atipicos = []
for valor in datos_procesados:
    if valor < Limite_inferior or valor > Limite_superior:
        Valores_atipicos.append(valor)

print(datos_procesados)




x= np.array([Limite_inferior,Limite_inferior,Limite_inferior,Q1, #bigote inferior
             Q1,Q3,Q3,Q1,Q1, #caja
             Q3,Q3,Limite_superior,Limite_superior,Limite_superior #bigote superior
             ])
y= np.array([3,2,2.5,2.5, #bigote inferior
             4,4,1,1,4, #caja
             4,2.5,2.5,3,2 #bigote superior
             ])
puntosy= np.array([2.8 * np.random.rand() + 1 for i in range(len(Valores_atipicos))])
puntosx= np.array([valor for valor in Valores_atipicos])
color= "red"

Q2y= np.array([1,4])
Q2x= np.array([Q2,Q2])

pyplot.title("Diagrama de caja cls de mtmtcs")
pyplot.scatter(puntosx,puntosy,c=color, cmap="seismic")
pyplot.plot(Q2x,Q2y ,c="red", linestyle="--")
pyplot.plot(x,y)
pyplot.show()
print(Q2)
