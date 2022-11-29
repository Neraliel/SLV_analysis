# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 08:27:13 2021

@author: regie
"""

"""
TP1 - Computation of the storm surge associated with Xynthia
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df_LC = pd.read_csv('Data_Xynthia_20100228_02H.dat', delim_whitespace=True, names=['lon_deg', 'lat_deg', 'bathy', 'wind', 'SLP'])

R = 6378206.4  # m
P = 2*np.pi*R

r = R*np.sin(df_LC.lat_deg.values[0]*np.pi/180)
p = 2*np.pi*r

lon_m = np.zeros(len(df_LC.lon_deg))
lat_m = np.zeros(len(df_LC.lat_deg))

for i in range(len(lon_m)):
    lat_m[i] = (df_LC.lat_deg.values[i]-df_LC.lat_deg.values[0])*p/360
    lon_m[i] = (df_LC.lon_deg.values[i]-df_LC.lon_deg.values[0])*p/360

df_LC['lat_m'] = lat_m
df_LC['lon_m'] = lon_m

L = df_LC.lon_m.max()-df_LC.lon_m.min()
print()


# Question 2
rho_air = 1.25
Cd = 0.0035
rho_mer = 1030
ts = rho_air*Cd*df_LC.wind**2

surf_stress = ts/(rho_mer*df_LC.bathy)  # on néglige l'élévation
plt.figure()
plt.plot(surf_stress)

# Question
# on veut calculer la surge du vent

elev = np.zeros(len(ts))
for i in range(len(elev)-1):
    elev[i+1] = ((lon_m[i+1]-lon_m[i])*ts[i]) / \
        (rho_mer*9.81*(df_LC.bathy[i]+elev[i]))+elev[i]

plt.figure()
plt.plot(lon_m, elev, label='vent seul')

df_LC.SLP = df_LC.SLP/100

surge_pressure = (1013-df_LC.SLP)/100

for j in range(len(elev)):
    elev[j] = elev[j]+surge_pressure[j]

plt.plot(lon_m, elev, label='vent et IB')
plt.legend()
