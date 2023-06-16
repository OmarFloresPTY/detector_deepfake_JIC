import customtkinter as ctk
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
        self.btn_dfEVAL = ctk.CTkButton(self.window,text="EVALUAR DEEPFAKE",text_color="white",width=600,font=("Arial",15,"bold"),state=ctk.DISABLED)
        self.btn_dfEVAL.pack()
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
    
    def func_verify_img(self):
        if self.ban_img_controller == False:
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
    
if __name__ == "__main__":
    app = VentanaPrincipal()