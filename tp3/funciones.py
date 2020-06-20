import numpy as np
import scipy

def generar_senal_cuadrada(T, t_inicial, t_final, fs):
    cantidad_de_muestras = obtener_cantidad_de_muestras(fs, t_final, t_inicial)
    eje_t = np.linspace(t_inicial, t_final, cantidad_de_muestras, endpoint=None)

    senal = [0 for x in range(cantidad_de_muestras)]
    for indice, t in enumerate(eje_t):
        # 0 < t < T/2 -> tiene que valer 1
        # T/2 < t < T -> tiene que valer -1
        for k in range(t_inicial, t_final):

            if k <= t <= k + T/2:
                senal[indice] = 1
            elif k + T/2 < t <= k + T:
                senal[indice] = -1

    return eje_t, senal

def calcular_transformada(x_t):
    X_w = scipy.fft.fft(x_t)
    return X_w

def obtener_cantidad_de_muestras(precision, t_final, t_inicial):
    cantidad_muestras = (t_final - t_inicial) * precision
    return cantidad_muestras

def obtener_amplitud(X_w):
    return np.abs(X_w)[0:int(len(X_w) / 2)] / (len(X_w) / 2)