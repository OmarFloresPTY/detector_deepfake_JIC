from PIL import Image
import requests
from io import BytesIO
import cv2
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf 


def categorizar(url):
    respuesta = respuesta.get(url)
    img = Image.open(BytesIO(respuesta.content))
    img = np.array(img).astype(float)/255

    img = cv2.resize(img,(224,224))

if __name__ == "__main__":
    modelo = tf.keras.models.load_model('./Modelo_Guardado')
    modelo.summary()  
