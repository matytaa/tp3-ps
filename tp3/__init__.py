import numpy as np
from matplotlib import pyplot as plt

from tp3.funciones import generar_senal_cuadrada
from tp3.funciones import generar_seno
from tp3.funciones import calcular_transformada
from tp3.funciones import obtener_cantidad_de_muestras
from tp3.funciones import obtener_amplitud

precision = 500
lim_izq = -10
lim_der = 10
duracion = lim_der - lim_izq
T = 1

t, x = generar_senal_cuadrada(T, lim_izq, lim_der, precision)
t2, x2 = generar_senal_cuadrada(T, lim_izq, lim_der, 500)
instante_de_tiempo, valor_en_seno = generar_seno(lim_izq, lim_der, 1, 1, 0, precision)
instante_de_tiempo_acotado, valor_en_seno_acotado = generar_seno(lim_izq, lim_der, 1, 1, 0, 100)

X_w = calcular_transformada(x2)
mod_X = np.abs(X_w)[0:int(len(X_w)/2)]/(len(X_w)/2)
f = np.linspace(0, precision, duracion*precision, endpoint=None)[0:int(len(X_w)/2)]

#X_w_seno = calcular_transformada(valor_en_seno_acotado)
#modulo_X_seno = obtener_amplitud(X_w_seno)
#f_seno = np.linspace(0, precision, obtener_cantidad_de_muestras(precision, lim_der, lim_izq), endpoint=None)[0:int(len(X_w_seno) / 2)]

#fig, axes = plt.subplots(1, 2)

fig2, axes2 = plt.subplots(1, 2)

axes2[0].plot(t, x)
axes2[1].set_xlabel("t (seg)")
axes2[1].plot(f, mod_X)
axes2[1].set_xlabel("f (Hz)")

#axes[0].plot(instante_de_tiempo, valor_en_seno)
#axes[1].set_xlabel("t (seg)")
#axes[1].plot(f_seno, modulo_X_seno)
#axes[1].set_xlabel("f (Hz)")

plt.show()