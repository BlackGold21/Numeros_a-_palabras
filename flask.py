from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

def convertir_numero_a_palabra(numero):
    # Aquí va la lógica de conversión de números a palabras.
    pass

@app.route('/convertir', methods=['POST'])
def convertir_y_hablar():
    data = request.get_json()
    numero = data.get('numero')
    texto = convertir_numero_a_palabra(numero)
    
    # Generar audio
    tts = gTTS(text=texto, lang='es')
    tts.save("numero_en_palabras.mp3")
    
    # Devuelve la respuesta con el texto y el archivo de audio
    return jsonify({'texto': texto, 'audio': 'numero_en_palabras.mp3'})

if __name__ == '__main__':
    app.run(debug=True)
