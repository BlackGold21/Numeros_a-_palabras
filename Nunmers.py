from gtts import gTTS
import os

def convertir_numero_a_palabra(numero):
    unidades = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    especiales = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
    decenas = ['', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
    centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']

    if numero < 0 or numero > 999:
        return 'Número fuera de rango'
    
    if numero < 10:
        return unidades[numero]
    elif numero < 20:
        return especiales[numero - 10]
    elif numero < 100:
        decena = numero // 10
        unidad = numero % 10
        return decenas[decena] + ('' if unidad == 0 else ' y ' + unidades[unidad])
    else:
        centena = numero // 100
        resto = numero % 100
        if resto == 0:
            return 'cien' if centena == 1 else centenas[centena]
        return centenas[centena] + ' ' + convertir_numero_a_palabra(resto)

def generar_audio(texto):
    tts = gTTS(text=texto, lang='es')
    tts.save("numero_en_palabras.mp3")
    os.system("start numero_en_palabras.mp3")  # En Windows
    # En Linux o MacOS, cambiar por: os.system("mpg321 numero_en_palabras.mp3")

# Ejemplo de uso:
numero = 123
texto = convertir_numero_a_palabra(numero)
print(f"El número {numero} se escribe como: {texto}")
generar_audio(texto)

