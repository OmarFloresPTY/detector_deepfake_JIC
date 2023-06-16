import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image,ImageTk
import requests
import io
from io import BytesIO
import cv2
import urllib.request
import numpy as np
import tensorflow as tf 

class VentanaPrincipal():
    def __init__(self) -> None:
        #Son variables que se inicializan
        self.frame_img_show_model_IMG = None
        self.ban_url_controller = False
        self.ban_img_controller = False
        self.ban_show_img_URL = False
        self.ban_show_img_IMG = False
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
        #self.btn_dfEVAL = ctk.CTkButton(self.window,text="EVALUAR DEEPFAKE",text_color="white",width=600,font=("Arial",15,"bold"),command=self.mostrar_imagen_IMG)
        #self.btn_dfEVAL.pack()
        #Bucle repetetivo para ejecutar el código tkinter
        self.window.mainloop()
    
    def func_verify_url(self):
        if self.ban_url_controller == False:
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

        self.btn_dfEVAL_URL = ctk.CTkButton(self.frame_url,text="EVALUAR DEEPFAKE",text_color="white",width=600,font=("Arial",15,"bold"),command=self.mostrar_imagen_URL)
        self.btn_dfEVAL_URL.pack()

    def func_verify_img(self):
        if self.ban_img_controller == False:
            self.frame_img = ctk.CTkFrame(self.window)
            self.frame_img.pack()
            self.lb_IMG = ctk.CTkLabel(self.frame_img,text='LA IMAGEN DEBE ESTAR EN FORMATO .JPG',text_color="red",font=("Arial",15,"bold"))
            self.lb_IMG.pack()
            self.btn_addIMG = ctk.CTkButton(self.frame_img,text="SELECCIONAR ARCHIVO",text_color="white",width=600,height=100,font=("Arial",15,"bold"),command=self.obtener_ruta_IMG)
            self.btn_addIMG.pack()
            self.ban_img_controller = True
        
        if self.ban_url_controller == True:
            self.frame_url.pack_forget()
            self.ban_url_controller = False
        self.btn_dfEVAL_IMG = ctk.CTkButton(self.frame_img,text="EVALUAR DEEPFAKE",text_color="white",width=600,font=("Arial",15,"bold"),command=self.mostrar_imagen_IMG)
        self.btn_dfEVAL_IMG.pack()
        
    def obtener_ruta_IMG(self):
        self.ruta_archivo = filedialog.askopenfilename()

    def categorizar_URL(self, url, modelo):
        self.respuesta = requests.get(self.url)
        self.img = Image.open(BytesIO(self.respuesta.content))
        self.img = np.array(self.img).astype(float)/255
        self.img = cv2.resize(self.img,(224,224))
        self.prediccion = modelo.predict(self.img.reshape(-1,224,224,3))
        return np.argmax(self.prediccion[0],axis=-1)
    
    def mostrar_imagen_URL(self):
        if self.ban_show_img_URL == True:
            self.frame_img_show_model_URL.pack_forget()
            self.ban_show_img_URL = False

        if self.ban_show_img_URL == False:
            self.frame_img_show_model_URL = ctk.CTkFrame(self.window)
            self.frame_img_show_model_URL.pack()

            self.modelo = tf.keras.models.load_model('./Modelo_Guardado')
            self.url = self.txtbox_URL.get()
            self.prediccion = self.categorizar_URL(self.url, self.modelo)
            self.response = requests.get(self.url)
            self.imagen_data = self.response.content
            self.imagen = Image.open(io.BytesIO(self.imagen_data))
            
            #Añadir imagen en Tkinter
            self.tk_image = ImageTk.PhotoImage(self.imagen)
            self.label_imagen = tk.Label(self.frame_img_show_model_URL, image=self.tk_image)
            self.label_imagen.image = self.tk_image  # Guardar una referencia para evitar que la imagen se borre
            self.label_imagen.pack()
            if self.prediccion == 0:
                self.label_prediccion = tk.Label(self.frame_img_show_model_URL, text="Detectado como Real")
            else:
                self.label_prediccion = tk.Label(self.frame_img_show_model_URL, text="Detectado como DeepFake")
            self.label_prediccion.pack()
            self.ban_show_img_URL = True

    def categorizar_IMG(self, imagen, modelo):
        self.img = np.array(self.imagen).astype(float)/255
        self.img = cv2.resize(self.img,(224,224))
        self.prediccion = self.modelo.predict(self.img.reshape(-1,224,224,3))
        return np.argmax(self.prediccion[0],axis=-1)
    
    def mostrar_imagen_IMG(self):
        if self.ban_show_img_IMG == False:
            if self.frame_img_show_model_IMG is not None:
                self.frame_img_show_model_IMG.destroy()
                self.ban_show_img_IMG = False

            self.frame_img_show_model_IMG = ctk.CTkFrame(self.window)
            self.frame_img_show_model_IMG.pack()

            self.modelo = tf.keras.models.load_model('./Modelo_Guardado')
            self.image_path = self.ruta_archivo
            self.imagen = Image.open(self.image_path)
            self.prediccion = self.categorizar_IMG(self.imagen,self.modelo)

            #Añadir imagen en Tkinter
            self.tk_image = ImageTk.PhotoImage(self.imagen)
            self.label_imagen = tk.Label(self.frame_img_show_model_IMG, image=self.tk_image)
            self.label_imagen.image = self.tk_image  # Guardar una referencia para evitar que la imagen se borre
            self.label_imagen.pack()
            if self.prediccion == 0:
                self.label_prediccion = tk.Label(self.frame_img_show_model_IMG, text="Detectado como Real")
            else:
                self.label_prediccion = tk.Label(self.frame_img_show_model_IMG, text="Detectado como DeepFake")
            self.label_prediccion.pack()
            self.ban_show_img_IMG == True

if __name__ == "__main__":
    app = VentanaPrincipal()