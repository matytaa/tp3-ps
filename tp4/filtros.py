from tp4.ventanas import levantar_audio
from tp4.ventanas import frecuencia_de_muestreo
from tp3.funciones import calcular_transformada
from tp3.funciones import calcular_antitransformada
import matplotlib.pyplot as plot
import numpy as np

def filtro_pasa_bajos(senal, fs, frecuencia_de_corte):
    media = obtener_media(frecuencia_de_corte, fs, len(senal))
    tf_signal = calcular_transformada(senal)
    samples_signal_filter = []
    for muestra in range(0, int(len(senal)/2)):
        if es_mayor_a_la_media(muestra, media):
            ignorar_muestra(samples_signal_filter)
        else:
            agregar_muestra(muestra, samples_signal_filter, tf_signal)

    for muestra in range(int(len(senal)/2), len(senal)):
        if not es_mayor_a_la_media(muestra, len(senal) - media):
            ignorar_muestra(samples_signal_filter)
        else:
            agregar_muestra(muestra, samples_signal_filter, tf_signal)

    signal_filter = calcular_antitransformada(samples_signal_filter)
    return signal_filter


def agregar_muestra(muestra, samples_signal_filter, tf_signal):
    samples_signal_filter.append(tf_signal[muestra])

def ignorar_muestra(samples_signal_filter):
    samples_signal_filter.append(complex(0, 0))

def obtener_media(frecuencia_de_corte, fs, signal_size):
    return int(frecuencia_de_corte * signal_size / fs)

def es_mayor_a_la_media(muestra, media):
    return muestra > media

signal_440, fs_440 = levantar_audio("audios/sen_440Hz_1s.wav")
signal_500, fs_500 = levantar_audio("audios/sen_500Hz_1s.wav")

fs = frecuencia_de_muestreo(fs_440, fs_500)

transform_signal_440 = calcular_transformada(signal_440)
transform_signal_500 = calcular_transformada(signal_500)

suma_signals = transform_signal_440 + transform_signal_500

anti_tf_suma_signals = calcular_antitransformada(suma_signals)
f = np.linspace(0, fs, fs, endpoint=None)[0:int(len(suma_signals) / 2)]
frecuencia_de_corte = 256
filter_signal = filtro_pasa_bajos(anti_tf_suma_signals, fs, frecuencia_de_corte)


eje_t = np.linspace(0, len(anti_tf_suma_signals), fs, endpoint=None)
figura, axes = plot.subplots(1, 2)
axes[0].plot(eje_t, anti_tf_suma_signals)
axes[0].set_xlabel("t - original signal")

eje_t = np.linspace(0, len(filter_signal), fs, endpoint=None)
axes[1].plot(eje_t, filter_signal)
axes[1].set_xlabel("t - filter signal")
plot.show()