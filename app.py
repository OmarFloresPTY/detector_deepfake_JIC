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
        self.frame_img_show_model_IMG = None
        self.ban_url_controller = False
        self.ban_img_controller = False
        self.ban_show_img_URL = False
        self.ban_show_img_IMG = False
        self.window = ctk.CTk()
        self.window.title('V.1.0.-Jornada de Iniciación Científica 2023')
        self.window.geometry('1000x600')
        self.lb_TITLE = ctk.CTkLabel(self.window,text='PROTOTIPO DETECTOR DEEPFAKE',text_color="white",font=("Arial",30,"bold"))
        self.lb_TITLE.pack(pady=(10,40))
        self.btn_dfURL = ctk.CTkButton(self.window,text="DETECTAR DEEPFAKE URL",text_color="white",width=600,font=("Arial",15,"bold"),command=self.func_verify_url)
        self.btn_dfURL.pack(pady=7)
        self.btn_dfIMG = ctk.CTkButton(self.window,text="DETECTAR DEEPFAKE IMAGEN",text_color="white",width=600,font=("Arial",15,"bold"),command=self.func_verify_img)
        self.btn_dfIMG.pack(pady=7)
        self.home_img_path = "./utils/home.jpg"
        self.home_img = Image.open(self.home_img_path)
        self.home_img = self.home_img.resize((1000, 600))
        self.tk_home_img = ImageTk.PhotoImage(self.home_img)
        self.label_home_img = tk.Label(self.window, image=self.tk_home_img)
        self.label_home_img.pack(pady=(90,0))
        self.label_home_img.config(borderwidth=0)
        self.window.mainloop()
    
    def func_verify_url(self):
        if self.ban_url_controller == False:
            self.frame_url = ctk.CTkFrame(self.window)
            self.frame_url.pack(pady=20)
            self.lb_URL = ctk.CTkLabel(self.frame_url,text='INSERTE EL URL AQUÍ',text_color="red",font=("Arial",15,"bold"))
            self.lb_URL.pack()
            self.txtbox_URL = ctk.CTkEntry(self.frame_url,width=600)
            self.txtbox_URL.pack()
            self.btn_dfEVAL_URL = ctk.CTkButton(self.frame_url,text="EVALUAR DEEPFAKE",text_color="white",width=600,font=("Arial",15,"bold"),command=self.mostrar_imagen_URL)
            self.btn_dfEVAL_URL.pack()
            self.fun_img_home_refresh()
            self.ban_url_controller = True
        
        if self.ban_img_controller == True:
            self.frame_img.pack_forget()
            self.ban_img_controller = False

    def func_verify_img(self):
        if self.ban_img_controller == False:
            self.frame_img = ctk.CTkFrame(self.window)
            self.frame_img.pack()
            self.lb_IMG = ctk.CTkLabel(self.frame_img,text='LA IMAGEN DEBE ESTAR EN FORMATO .JPG .PNG',text_color="red",font=("Arial",15,"bold"))
            self.lb_IMG.pack()
            self.btn_addIMG = ctk.CTkButton(self.frame_img,text="SELECCIONAR ARCHIVO",fg_color="#4F4F4F",text_color="white",width=600,height=100,font=("Arial",15,"bold"),command=self.obtener_ruta_IMG)
            self.btn_addIMG.pack()
            self.btn_dfEVAL_IMG = ctk.CTkButton(self.frame_img,text="EVALUAR DEEPFAKE",text_color="white",width=600,font=("Arial",15,"bold"),command=self.mostrar_imagen_IMG)
            self.btn_dfEVAL_IMG.pack()
            self.fun_img_home_refresh()
            self.ban_img_controller = True
        
        if self.ban_url_controller == True:
            self.frame_url.pack_forget()
            self.ban_url_controller = False
       
    def obtener_ruta_IMG(self):
        self.ruta_archivo = filedialog.askopenfilename()

    def categorizar_URL(self, url, modelo):
        self.url = url
        self.respuesta = requests.get(self.url)
        self.img = Image.open(BytesIO(self.respuesta.content))
        self.img = np.array(self.img).astype(float)/255
        self.img = cv2.resize(self.img,(224,224))
        self.prediccion = modelo.predict(self.img.reshape(-1,224,224,3))
        return np.argmax(self.prediccion[0],axis=-1)
    
    def mostrar_imagen_URL(self):
        self.label_home_img.pack_forget()
        if self.ban_show_img_URL == True:
            self.frame_img_show_model_URL.pack_forget()
            self.ban_show_img_URL = False

        if self.ban_show_img_URL == False:
            self.frame_img_show_model_URL = ctk.CTkScrollableFrame(self.frame_url,width=1920,height=1000,fg_color='transparent')
            self.frame_img_show_model_URL.pack()

            self.modelo = tf.keras.models.load_model('./Modelo_Guardado')
            self.url = self.txtbox_URL.get()
            self.prediccion = self.categorizar_URL(self.url, self.modelo)
            self.response = requests.get(self.url)
            self.imagen_data = self.response.content
            self.imagen = Image.open(io.BytesIO(self.imagen_data))
            
            self.tk_image = ImageTk.PhotoImage(self.imagen)
            self.label_imagen = tk.Label(self.frame_img_show_model_URL, image=self.tk_image)
            self.label_imagen.image = self.tk_image
            if self.prediccion == 0:
                self.label_prediccion = ctk.CTkLabel(self.frame_img_show_model_URL, text="DETECTADO COMO REAL",text_color="#24FF00",font=("Arial",20,"bold"))
            else:
                self.label_prediccion = ctk.CTkLabel(self.frame_img_show_model_URL, text="DETECTADO COMO DEEPFAKE",text_color="#24FF00",font=("Arial",20,"bold"))
            self.label_prediccion.pack()
            self.label_imagen.pack()
            self.ban_show_img_URL = True

    def categorizar_IMG(self, imagen, modelo):
        self.imagen = imagen
        self.modelo = modelo
        self.img = np.array(self.imagen).astype(float)/255
        self.img = cv2.resize(self.img,(224,224))
        self.prediccion = self.modelo.predict(self.img.reshape(-1,224,224,3))
        return np.argmax(self.prediccion[0],axis=-1)
    
    def mostrar_imagen_IMG(self):
        self.label_home_img.pack_forget()
        if self.ban_show_img_IMG == False:
            if self.frame_img_show_model_IMG is not None:
                self.frame_img_show_model_IMG.destroy()
                self.ban_show_img_IMG = False

            self.frame_img_show_model_IMG = ctk.CTkFrame(self.frame_img,fg_color='transparent',width=1000)
            self.frame_img_show_model_IMG.pack()

            self.modelo = tf.keras.models.load_model('./Modelo_Guardado')
            self.image_path = self.ruta_archivo
            self.imagen = Image.open(self.image_path)
            self.imagen = self.imagen.resize((1000,600))
            self.prediccion = self.categorizar_IMG(self.imagen,self.modelo)

            self.tk_image = ImageTk.PhotoImage(self.imagen,width=10,height=10)
            self.label_imagen = tk.Label(self.frame_img_show_model_IMG, image=self.tk_image)
            self.label_imagen.image = self.tk_image
            if self.prediccion == 0:
                self.label_prediccion = ctk.CTkLabel(self.frame_img_show_model_IMG, text="DETECTADO COMO REAL",text_color="#24FF00",font=("Arial",20,"bold"))
            else:
                self.label_prediccion = ctk.CTkLabel(self.frame_img_show_model_IMG, text="DETECTADO COMO DEEPFAKE",text_color="#24FF00",font=("Arial",20,"bold"))
            
            self.label_prediccion.pack()
            self.label_imagen.pack()

    def func_img_home(self):
        self.home_img_path = "./utils/home.jpg"
        self.home_img = Image.open(self.home_img_path)
        self.home_img = self.home_img.resize((1000, 600))
        self.tk_home_img = ImageTk.PhotoImage(self.home_img)
        self.label_home_img = tk.Label(self.window, image=self.tk_home_img)
        self.label_home_img.pack(pady=(90,0))
        self.label_home_img.config(borderwidth=0)
    
    def fun_img_home_refresh(self):
        self.label_home_img.pack_forget()
        self.func_img_home()

if __name__ == "__main__":
    app = VentanaPrincipal()