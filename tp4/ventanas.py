import matplotlib.pyplot as plot
import numpy as np
import wave
import sys
from scipy import signal

from tp3.funciones import calcular_transformada
from tp3.funciones import calcular_antitransformada


def levantar_audio(file):
    spf = wave.open(file, "r")
    signal = spf.readframes(-1)
    samples = spf.getframerate()
    signal = np.fromstring(signal, "Int16")
    if spf.getnchannels() == 2:
        print("Just mono files")
        sys.exit(0)
    return signal, samples

def calcular_transformada_sonido(a_signal):
    return calcular_transformada(a_signal)

def calcular_modulo(transform_signal):
    return np.abs(transform_signal)[0:int(len(transform_signal) / 2)] / (len(transform_signal) / 2)

def frecuencia_de_muestreo(fs_signal, fs_another_signal):
    if (fs_signal >= fs_another_signal):
        return fs_signal
    return fs_another_signal

signal_440, fs_440 = levantar_audio("audios/sen_440Hz_1s.wav")
signal_500, fs_550 = levantar_audio("audios/sen_500Hz_1s.wav")

fs = frecuencia_de_muestreo(fs_440, fs_550)

transform_signal_440 = calcular_transformada(signal_440)
module_signal_440 = calcular_modulo(transform_signal_440)

transform_signal_500 = calcular_transformada(signal_500)
module_signal_500 = calcular_modulo(transform_signal_500)

suma_signals = transform_signal_440 + transform_signal_500
modulo_suma_signals = module_signal_440 + module_signal_500

anti_tf_suma_signals = calcular_antitransformada(suma_signals)
f = np.linspace(0, fs, fs, endpoint=None)[0:int(len(suma_signals) / 2)]

n = len(suma_signals)

boxcar = signal.boxcar
s_boxcar = anti_tf_suma_signals * boxcar(n)
tf_boxcar = calcular_transformada(s_boxcar)
modulo_boxcar = calcular_modulo(tf_boxcar)
f_boxcar = np.linspace(0, fs, fs, endpoint=None)[0:int(len(tf_boxcar) / 2)]

bartlett = signal.bartlett
s_bartlett = anti_tf_suma_signals * bartlett(n)
tf_bartlett = calcular_transformada(s_bartlett)
modulo_bartlett = calcular_modulo(tf_bartlett)
f_bartlett = np.linspace(0, fs, fs, endpoint=None)[0:int(len(tf_bartlett) / 2)]

hamming = signal.hamming
s_hamming = anti_tf_suma_signals * hamming(n)
tf_hamming = calcular_transformada(s_hamming)
modulo_hamming = calcular_modulo(tf_hamming)
f_hamming = np.linspace(0, fs, fs, endpoint=None)[0:int(len(tf_hamming) / 2)]

figura, axes = plot.subplots(1, 4)
axes[0].plot(f, modulo_suma_signals)
axes[0].set_xlabel("f (Hz) - fourier")

axes[1].plot(f_boxcar, modulo_boxcar)
axes[1].set_xlabel("f (Hz) - rectangular")

axes[2].plot(f_bartlett, modulo_bartlett)
axes[2].set_xlabel("f (Hz) - triangular")

axes[3].plot(f_hamming, modulo_hamming)
axes[3].set_xlabel("f (Hz) - hamming")

plot.show()

# Plot the spectrogram
plot.specgram(suma_signals,Fs=fs)
plot.xlabel("time")
plot.ylabel('Frequency')

plot.show()
