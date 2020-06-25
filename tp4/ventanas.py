import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from scipy import signal

from tp3.funciones import calcular_transformada
from tp3.funciones import calcular_antitransformada


def levantar_audio(file):
    spf440 = wave.open(file, "r")
    signal = spf440.readframes(-1)
    signal = np.fromstring(signal, "Int16")
    if spf440.getnchannels() == 2:
        print("Just mono files")
        sys.exit(0)
    return signal

def calcular_transformada_sonido(a_signal):
    return calcular_transformada(a_signal)

def calcular_modulo(transform_signal):
    return np.abs(transform_signal)[0:int(len(transform_signal) / 2)] / (len(transform_signal) / 2)

signal_440 = levantar_audio("audios/sen_440Hz_1s.wav")
signal_500 = levantar_audio("audios/sen_500Hz_1s.wav")
fs = 44100

transform_signal_440 = calcular_transformada(signal_440)
module_signal_440 = calcular_modulo(transform_signal_440)

transform_signal_500 = calcular_transformada(signal_500)
module_signal_500 = calcular_modulo(transform_signal_500)

suma = transform_signal_440 + transform_signal_500
suma_mod = module_signal_440 + module_signal_500

anti_tf_suma = calcular_antitransformada(suma)

boxcar = signal.boxcar
bartlett = signal.bartlett
hamming = signal.hamming

n = len(suma)
boxcar = anti_tf_suma*boxcar(n)
sbar = anti_tf_suma*bartlett(n)
shamm = anti_tf_suma*hamming(n)

tf_boxcar = calcular_transformada(boxcar)
mod_boxcar = calcular_modulo(tf_boxcar)
f2 = np.linspace(0, fs, fs, endpoint=None)[0:int(len(tf_boxcar)/2)]

tf_bar = calcular_transformada(sbar)
mod_bar = calcular_modulo(tf_bar)
f3 = np.linspace(0, fs, fs, endpoint=None)[0:int(len(tf_bar)/2)]


tf_hamm = calcular_transformada(shamm)
mod_hamm = calcular_modulo(tf_hamm)
f4 = np.linspace(0, fs, fs, endpoint=None)[0:int(len(tf_hamm)/2)]


f = np.linspace(0, fs, fs, endpoint=None)[0:int(len(suma) / 2)]

fig2, axes2 = plt.subplots(1, 4)
axes2[0].plot(f, suma_mod)
axes2[0].set_xlabel("f (Hz) - fourier")

axes2[1].plot(f2, mod_boxcar)
axes2[1].set_xlabel("f (Hz) - rectangular")

axes2[2].plot(f3, mod_bar)
axes2[2].set_xlabel("f (Hz) - triangular")

axes2[3].plot(f4, mod_hamm)
axes2[3].set_xlabel("f (Hz) - hamming")
plt.show()