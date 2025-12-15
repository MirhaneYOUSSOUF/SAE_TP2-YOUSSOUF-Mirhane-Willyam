import csv
from pylab import figure, show, bar
from datetime import datetime
import numpy as np
from matplotlib import pyplot as plt

# Liste pour stocker les données
Donnees1 = []

# Lecture du fichier CSV
with open('Donnees.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        Donnees1.append(row)
#print(Donnees1)

Altitude=[[Donnees1[i+1][3]] for i in range(len(Donnees1)-1)]
#print(Altitude)
Altitude2 = [float(altitude[0]) for altitude in Altitude]
#print(Altitude2)

Pressure=[[Donnees1[i+1][8]] for i in range(len(Donnees1)-1)]
#print(Pressure)
Pressure2 = [float(pressure[0]) for pressure in Pressure]
#print(Pressure2)

#plt.plot(Altitude2, Pressure2, label='Pression en fonction de laltitude')
# Ajouter un titre et des labels aux axes
#plt.title('Courbe de la Pression en fonction de lAltitude')
#plt.xlabel('Altitude')
#plt.ylabel('Pression')
# Afficher la grille
#plt.grid(True)
# Afficher le graphique
#plt.show()

Speed=[[Donnees1[i+1][15]] for i in range(len(Donnees1)-1)]
#print(Speed)
Speed2= [float(speed[0]) for speed in Speed]
#print(Speed2)

Longitude=[[Donnees1[i+1][2]] for i in range(len(Donnees1)-1)]
#print(Longitude)
Longitude2=[float(longitude[0]) for longitude in Longitude]
#print(Longitude2)

#plt.plot(Longitude2, Speed2, label='La vitesse en fonction de la longitude')
# Ajouter un titre et des labels aux axes
#plt.title('Courbe de la vitesse en fonction de la longitude')
#plt.xlabel('Longitude')
#plt.ylabel('Speed')
# Afficher la grille
#plt.grid(True)
# Afficher le graphique
#plt.show()

Inside_temp=[[Donnees1[i+1][5]] for i in range(len(Donnees1)-1)]
#print(Inside_temp)
Inside_temp2= [float(inside[0]) for inside in Inside_temp]
print(Inside_temp2)

Outside_temp=[[Donnees1[i+1][6]] for i in range(len(Donnees1)-1)]
#print(Outside_temp)
Outside_temp2=[float(outside[0]) for outside in Outside_temp]
#print(Outside_temp2)

plt.plot(Inside_temp2, Outside_temp2, label='Inside temp en fonction de Outside_temp')
# Ajouter un titre et des labels aux axes
plt.title('Courbe de Inside_temp en fonction de Outside_temp')
plt.xlabel('Inside')
plt.ylabel('Outside')
# Afficher la grille
plt.grid(True)
# Afficher le graphique
plt.show()

	

#Altitude2=[]
#for i in range(len(Altitude)):
	#f=float(Altitude)
	#Altitude2.append(f)
#print(Altitude2)
# Affichage du graphique
#figure()
#bar(Datetime, Altitude)  # Bar chart avec les dates et altitudes
#show()

