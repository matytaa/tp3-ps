import numpy as np
from matplotlib import pyplot as plt

from tp3.funciones import generar_senal_cuadrada
from tp3.funciones import generar_seno
from tp3.funciones import calcular_transformada
from tp3.funciones import obtener_cantidad_de_muestras
from tp3.funciones import obtener_amplitud

precision = 500
fs = 20
lim_izq = -10
lim_der = 10
duracion = lim_der - lim_izq
T = 1

t, x = generar_senal_cuadrada(T, lim_izq, lim_der, precision)
t2, x2 = generar_senal_cuadrada(T, lim_izq, lim_der, fs)

X_w = calcular_transformada(x)
X2_w = calcular_transformada(x2)

mod_X = np.abs(X_w)[0:int(len(X_w)/2)]/(len(X_w)/2)
mod_X2 = np.abs(X2_w)[0:int(len(X2_w)/2)]/(len(X2_w)/2)

f = np.linspace(0, precision, duracion*precision, endpoint=None)[0:int(len(X_w)/2)]
f2 = np.linspace(0, fs, duracion*fs, endpoint=None)[0:int(len(X2_w)/2)]

fig, axes = plt.subplots(1, 2)
fig2, axes2 = plt.subplots(1, 2)

axes[0].plot(t, x)
axes[1].set_xlabel("t (seg)")
axes[1].plot(f, mod_X)
axes[1].set_xlabel("f (Hz)")

axes2[0].plot(t2, x2)
axes2[1].set_xlabel("t (seg)")
axes2[1].plot(f2, mod_X2)
axes2[1].set_xlabel("f (Hz)")

plt.show()