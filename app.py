import tkinter as tk
import customtkinter as ctk
from PIL import Image
import requests
import io
from io import BytesIO
import cv2
import urllib.request
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tensorflow as tf 

class VentanaPrincipal():
    def __init__(self) -> None:
        self.ban_url_controller = False
        self.ban_img_controller = False
        #Inicializando la ventana
        self.window = ctk.CTk()
        #Creando el titulo de la aplicación
        self.window.title('Jornada de Iniciación Cientifica')
        #Inicializando el tamaño de la aplicación
        self.window.geometry('1000x600')

        #Creando los widgets de la aplicación:
        #Widgets label principal
        self.lb_TITLE = ctk.CTkLabel(self.window,text='PROTOTIPO DETECTOR DEEPFAKE',text_color="white",font=("Arial",30,"bold"))
        self.lb_TITLE.pack()
        #Widgets buttom principales
        self.btn_dfURL = ctk.CTkButton(self.window,text="DETECTAR DEEPFAKE URL",text_color="white",width=600,font=("Arial",15,"bold"),command=self.func_verify_url)
        self.btn_dfURL.pack()
        self.btn_dfIMG = ctk.CTkButton(self.window,text="DETECTAR DEEPFAKE IMAGEN",text_color="white",width=600,font=("Arial",15,"bold"),command=self.func_verify_img)
        self.btn_dfIMG.pack()
        self.btn_dfEVAL = ctk.CTkButton(self.window,text="EVALUAR DEEPFAKE",text_color="white",width=600,font=("Arial",15,"bold"),state= "disable",command=self.load_model)
        self.btn_dfEVAL.pack()
        #Bucle repetetivo para ejecutar el código tkinter
        self.window.mainloop()
    
    def func_verify_url(self):
        if self.ban_url_controller == False:
            self.btn_dfEVAL._state = "normal"
            self.frame_url = ctk.CTkFrame(self.window)
            self.frame_url.pack(pady=20)
            self.lb_URL = ctk.CTkLabel(self.frame_url,text='INSERTE EL URL AQUÍ',text_color="red",font=("Arial",15,"bold"))
            self.lb_URL.pack()
            self.txtbox_URL = ctk.CTkEntry(self.frame_url,width=600)
            self.txtbox_URL.pack()
            self.ban_url_controller = True
        
        if self.ban_img_controller == True:
            self.frame_img.pack_forget()
            self.ban_img_controller = False
    
    def func_verify_img(self):
        if self.ban_img_controller == False:
            self.btn_dfEVAL._state = "normal"
            self.frame_img = ctk.CTkFrame(self.window)
            self.frame_img.pack()
            self.lb_IMG = ctk.CTkLabel(self.frame_img,text='LA IMAGEN DEBE ESTAR EN FORMATO .JPG',text_color="red",font=("Arial",15,"bold"))
            self.lb_IMG.pack()
            self.btn_addIMG = ctk.CTkButton(self.frame_img,text="AÑADIR IMAGEN",text_color="white",width=600,height=100,font=("Arial",15,"bold"))
            self.btn_addIMG.pack()
            self.ban_img_controller = True
        
        if self.ban_url_controller == True:
            self.frame_url.pack_forget()
            self.ban_url_controller = False
    
    def categorizar_modelo(self,url,modelo):
        self.respuesta = requests.get(url)
        self.img = Image.open(BytesIO(self.respuesta.content))
        self.img = np.array(self.img).astype(float)/255
        self.img = cv2.resize(self.img,(224,224))
        self.prediccion = modelo.predict(self.img.reshape(-1,224,224,3))
        return np.argmax(self.prediccion[0],axis=-1)
    
    def load_model(self):
        self.modelo = tf.keras.models.load_model('./Modelo_Guardado')
        self.url = 'https://cdn.mos.cms.futurecdn.net/xwk66FPAKm63fXsgJSoucn-1200-80.jpg' 
        self.response = requests.get(self.url)
        self.imagen_data = self.response.content
        self.imagen = Image.open(io.BytesIO(self.imagen_data))
        self.prediccion = self.categorizar_modelo(self.url,self.modelo)
        
        fig, ax = plt.subplots()
        ax.imshow(self.imagen)
        ax.set_title('Predicción: {}'.format(self.prediccion))
        ax.axis('off')
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.draw()

        # Ubicar el objeto tkinter en la ventana
        canvas.get_tk_widget().pack()





if __name__ == "__main__":
    app = VentanaPrincipal()