from PIL import Image
import requests
import io
from io import BytesIO
import cv2
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf 


def categorizar(url,modelo):
    respuesta = requests.get(url)
    img = Image.open(BytesIO(respuesta.content))
    img = np.array(img).astype(float)/255

    img = cv2.resize(img,(224,224))
    prediccion = modelo.predict(img.reshape(-1,224,224,3))
    return np.argmax(prediccion[0],axis=-1)

if __name__ == "__main__":
    modelo = tf.keras.models.load_model('./Modelo_Guardado')
    #modelo.summary()
    url = 'https://cdn.mos.cms.futurecdn.net/xwk66FPAKm63fXsgJSoucn-1200-80.jpg' 
    response = requests.get(url)
    imagen_data = response.content
    imagen = Image.open(io.BytesIO(imagen_data))
    prediccion = categorizar(url,modelo)
    if prediccion == 0:
        plt.imshow(imagen)
        plt.axis('off')
        plt.title("Detectado como Real")
        plt.show()
    else:
        plt.imshow(imagen)
        plt.axis('off')
        plt.title("Detectado como DeepFake")
        plt.show()
