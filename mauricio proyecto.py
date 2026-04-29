import matplotlib.pyplot as pyplot  # Importing the pyplot module from matplotlib for plotting graphs
import numpy as np  # Importing numpy for numerical operations

# Prompting the user to input statistical data as a comma-separated string
datos = input("porfavor ingrese los datos estadisticos:")
print(datos)  # Printing the raw input data

datos_procesados = []  # Initializing a list to store valid numerical data
errores = []  # Initializing a list to store invalid data

# Splitting the input data by commas and processing each value
for x in datos.split(","):
    try:
        datos_procesados.append(float(x))  # Attempting to convert the value to a float
    except ValueError:
        errores.append(x)  # Storing the value in errores if conversion fails

print("Datos válidos:", datos_procesados)  # Printing valid numerical data

if errores:
    print("Value Error:dato/s no cuantificable/s:", errores)  # Printing invalid data
    exit()  # Exiting the program if there are invalid data

# Re-splitting and converting the input data to floats
datos_procesados = datos.split(",")
datos_procesados = [float(x) for x in datos_procesados]
datos_procesados.sort()  # Sorting the numerical data in ascending order
cantidad_datos = len(datos_procesados)  # Calculating the number of data points

# Checking if there are at least 5 data points
if cantidad_datos < 5:
    print("lenght type error: se esperaban al menos 5 argumentos, se detectaron " + str(cantidad_datos))
    exit()  # Exiting the program if there are fewer than 5 data points

valor = input("Presione enter: ")  # Pausing for user input

# Calculating the minimum and maximum values
minimio = datos_procesados[0]  # Minimum value
maximo = datos_procesados[-1]  # Maximum value

# Calculating the first quartile (Q1)
Q1_aprox = (cantidad_datos + 1) / 4  # Approximate position of Q1
Q1_aprox_original = Q1_aprox  # Storing the original position for interpolation

# Determining if Q1 is an integer or needs interpolation
if Q1_aprox == int(Q1_aprox):
    Q1_aprox = Q1_aprox
elif Q1_aprox*2 == int(Q1_aprox*2):
    Q1_aprox = [int(Q1_aprox), int(Q1_aprox)+1]
else:
    Q1_aprox = [int(Q1_aprox), int(Q1_aprox)+1]

# Calculating the second quartile (Q2 or median)
Q2_aprox = (cantidad_datos + 1) / 2  # Approximate position of Q2
Q2_aprox_original = Q2_aprox  # Storing the original position for interpolation

if Q2_aprox == int(Q2_aprox):
    Q2_aprox = Q2_aprox
else:
    Q2_aprox = [int(Q2_aprox), int(Q2_aprox)+1]

# Calculating the third quartile (Q3)
Q3_aprox = 3 * (cantidad_datos + 1) / 4  # Approximate position of Q3
Q3_aprox_original = Q3_aprox  # Storing the original position for interpolation

if Q3_aprox == int(Q3_aprox):
    Q3_aprox = Q3_aprox
elif Q3_aprox*2 == int(Q3_aprox*2):
    Q3_aprox = [int(Q3_aprox), int(Q3_aprox)+1]
else:    
    Q3_aprox = [int(Q3_aprox), int(Q3_aprox)+1]

# Interpolating Q1 if necessary
if type(Q1_aprox) == list:
    Q1 = datos_procesados[int(Q1_aprox[0])-1] + (Q1_aprox_original - int(Q1_aprox[0])) * (datos_procesados[int(Q1_aprox[1])-1] - datos_procesados[int(Q1_aprox[0])-1])
else:
    Q1 = datos_procesados[int(Q1_aprox)-1]

# Interpolating Q2 if necessary
if type(Q2_aprox) == list:
    Q2 = datos_procesados[int(Q2_aprox[0])-1] + (Q2_aprox_original - int(Q2_aprox[0])) * (datos_procesados[int(Q2_aprox[1])-1] - datos_procesados[int(Q2_aprox[0])-1])
else:
    Q2 = datos_procesados[int(Q2_aprox)-1]

# Interpolating Q3 if necessary
if type(Q3_aprox) == list:
    Q3 = datos_procesados[int(Q3_aprox[0])-1] + (Q3_aprox_original - int(Q3_aprox[0])) * (datos_procesados[int(Q3_aprox[1])-1] - datos_procesados[int(Q3_aprox[0])-1])
else:
    Q3 = datos_procesados[int(Q3_aprox)-1]

# Calculating the interquartile range (IQR)
RIC = Q3 - Q1

# Calculating the lower and upper limits for outliers
limite_inferior = Q1 - 1.5 * RIC
Limite_superior = Q3 + 1.5 * RIC

# Identifying outliers
Valores_atipicos = []
for valor in datos_procesados:
    if valor < limite_inferior or valor > Limite_superior:
        Valores_atipicos.append(valor)

print(datos_procesados)  # Printing the sorted data

# Preparing data for the box plot
x= np.array([limite_inferior,limite_inferior,limite_inferior,Q1, # Bigote inferior
             Q1,Q3,Q3,Q1,Q1, # Caja
             Q3,Q3,Limite_superior,Limite_superior,Limite_superior # Bigote superior
             ])
y= np.array([3,2,2.5,2.5, # Bigote inferior
             4,4,1,1,4, # Caja
             4,2.5,2.5,3,2 # Bigote superior
             ])
puntosy= np.array([2.8 * np.random.rand() + 1 for i in range(len(Valores_atipicos))])  # Random y-coordinates for outliers
puntosx= np.array([valor for valor in Valores_atipicos])  # x-coordinates for outliers
color= "red"  # Color for outliers

# Preparing data for the median line
Q2y= np.array([1,4])
Q2x= np.array([Q2,Q2])

# Preparing data for the IQR line
RICLINEX= np.array([Q1, Q3])
RICLINEY= np.array([2.5, 2.5])

# Preparing data for the lower whisker
Bigote_inferior_x= np.array([limite_inferior,limite_inferior,limite_inferior,Q1])
Bigote_inferior_y= np.array([3,2,2.5,2.5])

# Preparing data for the upper whisker
Bigote_superior_x= np.array([Q3, Limite_superior, Limite_superior, Limite_superior])
Bigote_superior_y= np.array([2.5, 2.5,3,2])

# Plotting the box plot
pyplot.title("Diagrama de caja cls de mtmtcs")  # Setting the title of the plot
pyplot.scatter(puntosx,puntosy,c=color, cmap="seismic", label="Valores atipicos" + str(Valores_atipicos))  # Plotting outliers
pyplot.plot(Q2x,Q2y ,c="red", linestyle="--", label="Q2: " + str(Q2))  # Plotting the median line
pyplot.plot(x,y, label="Q1: " + str(Q1) + ", Q3: " + str(Q3))  # Plotting the box and whiskers
pyplot.plot(Bigote_inferior_x, Bigote_inferior_y, c="green", linestyle="-", label="Limite inferior: " + str(limite_inferior))  # Plotting the lower whisker
pyplot.plot(Bigote_superior_x, Bigote_superior_y, c="green", linestyle="-", label="Limite superior: " + str(Limite_superior))  # Plotting the upper whisker
pyplot.plot(RICLINEX, RICLINEY, c="black", linestyle="-.", label="RIC: " + str(RIC))  # Plotting the IQR line
pyplot.legend()  # Adding a legend to the plot
pyplot.show()  # Displaying the plot

print(Q2)  # Printing the median