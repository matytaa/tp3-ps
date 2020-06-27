from scipy import signal

def filtrar_pasa_bajos(senal, fs, frecuencia_de_corte):
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

def calcular_transformada(signal_domain_time):
    signal_domain_frecuency = signal.fft.fft(signal_domain_time)
    return signal_domain_frecuency

def calcular_antitransformada(signal_domain_frecuency):
    signal_domain_time = signal.fft.ifft(signal_domain_frecuency)
    return signal_domain_time