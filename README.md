# Prototipo inteligente para la identificación de imágenes falsificadas en el contexto panameño 🥸📷🚫🐍

## **Resumen** 📖
 El proyecto implica la construcción de una aplicación basada en Python que utiliza el modelo pre-entrenado Mobilenetv2 para identificar imágenes falsas, específicamente DeepFakes, en el contexto panameño. A través de este proyecto, se busca generar conciencia sobre la importancia de la ciberseguridad, el cuidado de los datos personales y la lucha contra la desinformación, con el objetivo de proteger a las personas y las instituciones de los posibles riesgos asociados a la manipulación de imágenes.

## **Pre-requisitos e Instalación** 💻
¿Qué necesitas para probar el prototipo?
1. **_Si no eres Programador (Método Fácil)_**:
* Descarga el ejecutable .exe del prototipo desde [Mega](https://mega.nz/file/dL8AnIZK#UgkYFeWFhivBebtw2MRT1XFQE1hYRze_yH9BHjnq5sc).

2. **_Si eres Programador_**:
* Clona el repositorio en tu computador.
```
git clone https://github.com/OmarFloresPTY/detector_deepfake_JIC.git
```
* Crea un entorno virtual desde cero.
```
py -m <nombre-del-entorno> venv
.\<nombre-del-entorno>\Scripts\activate
```
* Instala las dependencias en tu entorno virtual.
```
pip install -r requirements.txt
```
* Ejecuta el programa.

## **Construido con 🛠️**
A continuación se muestran las herramientas utilizadas para crear el proyecto.

<img src="https://i.ibb.co/1s0XknW/Tecnolog-as-Indentificadas-librer-as-principales.png" alt="Tecnolog-as-Indentificadas-librer-as-principales" border="5" />

Documentación oficial de cada herramienta:
* [Python 3.11](https://www.python.org/)
* [TensorFlow](https://www.tensorflow.org/)
* [TensorFlow Hub](https://www.tensorflow.org/hub?hl=es-419)
* [CustomTkinter](https://customtkinter.tomschimansky.com)
* [OpenCV](https://opencv.org/)
* [Keras](https://keras.io/)

## **Diseño Conceptual de la construcción del prototipo** 🗺️🧑‍💻
Para entender un poco el flujo de preparación o elaboración del prototipo se presenta el siguiente gráfico:
<img src="https://i.ibb.co/4f7C5n6/Diagrama-Conceptual.png" alt="Diagrama-Conceptual" border="0" />

### *_Algunas Características adicionales del prototipo_*:
* El proyecto es compatible con la versión actual de Python 3.11.3, lo cual garantiza su compatibilidad con las últimas versiones de la herramienta.
* Está disponible para ser ejecuta desde un .exe en Windows 10 y 11.
* El programa fue desarrollado para funcionar en una interfaz gráfica, lo que permite una interacción más amigable y visual con el usuario.
* La programación de la interfaz está bajo el paradigma de la programación orientada a objetos.
#### *Librerías utilizadas en el proyecto:*

- `filedialog`: filedialog es un módulo de la librería tkinter que proporciona funciones para interactuar con el sistema de archivos del usuario, permitiendo seleccionar archivos o directorios a través de cuadros de diálogo.
- `customtkinter`: customtkinter es una librería personalizada (probablemente creada por el usuario o alguien más) que extiende las funcionalidades de tkinter y ofrece componentes de interfaz gráfica adicionales o personalizados. Al importarla como `ctk`, se renombra para facilitar su uso en el código.

- `PIL`: PIL (Python Imaging Library) es una librería muy popular para el procesamiento de imágenes en Python. Al importar Image y ImageTk, podemos utilizar las funciones y clases proporcionadas por PIL para cargar y manipular imágenes.

- `requests`: requests es una librería de Python que simplifica el envío de solicitudes HTTP. Proporciona una interfaz fácil de usar para interactuar con servicios web y realizar solicitudes GET, POST, etc.

- `io`: io es un módulo de Python que proporciona clases y funciones para manejar la entrada y salida de datos. Se utiliza en este caso para trabajar con datos binarios.

- `BytesIO`: BytesIO es una clase en el módulo io que permite tratar datos binarios como si fueran archivos en memoria. Es útil para leer y escribir datos binarios, como imágenes, en un entorno de memoria.

- `cv2`: cv2 es una librería de código abierto para el procesamiento de imágenes y visión por computadora en Python. Proporciona funciones para cargar, manipular y analizar imágenes y videos.

- `urllib.request`: urllib es un módulo de Python que proporciona funciones para trabajar con URL y realizar solicitudes web. urllib.request se utiliza en este caso para cargar imágenes desde una URL.

- `numpy`: numpy es una librería de Python ampliamente utilizada para realizar cálculos numéricos y manipulación de matrices. Proporciona una estructura de datos de matriz multidimensional y funciones matemáticas para realizar operaciones eficientes en matrices.

- `tensorflow`: tensorflow es una librería de aprendizaje automático de código abierto desarrollada por Google. Permite la creación y entrenamiento de redes neuronales y se utiliza ampliamente en tareas de procesamiento de imágenes, reconocimiento de voz, procesamiento de lenguaje natural y más. Al importarla como `tf`, se renombra para facilitar su uso en el código.

## **Capturas de Pantalla** 📷
A continuación se presentarán las diferentes salidas que otorga el sistema al usuario.

### **Ventana Principal**
<img src="https://i.ibb.co/N9xs2v6/Prototipo-2.png" border="0" />

### **Titulo y botones principales**
<img src="https://i.ibb.co/5M0SrVV/widget01.png" alt="widget01" border="0" />

### **Frame No.1 para insertar URL, label, textbox y boton para evaluar**
<img src="https://i.ibb.co/KrsgFzx/widget02.png" alt="widget02" border="0" />

### **Frame No.2 para insertar IMG, label,boton para buscar imagen y boton para evaluar**
<img src="https://i.ibb.co/cDqgwy5/widget03.png" alt="widget03" border="0" />

### **Frame No.3 salida de la evaluación al usuario, label e imagen**
<a href="https://ibb.co/WK2Q12V"><img src="https://i.ibb.co/VBqd8qw/Prototipo-1.png" alt="Prototipo-1" border="0" /></a>

## Autores ✒️
En el proyecto participaron los siguientes autores.
* Omar Flores:
    * correo institucional: [omar.flores@utp.ac.pa](omar.flores@utp.ac.pa)
    * linkedin: [omarabdielflores](https://www.linkedin.com/in/omarabdielflores/)
* Dante Della Togna:
    * correo institucional: [dante.dellatogna@utp.ac.pa](dante.dellatogna@utp.ac.pa)
    * linkedin: [dante-della-togna](https://www.linkedin.com/in/dante-della-togna-31201b1b5/)
    * github: [dantedellatogna](https://github.com/dantedellatogna)
* Ashly Arroyo:
    * correo institucional: [ashly.arroyo@utp.ac.pa](ashly.arroyo@utp.ac.pa)

## Licencia 📎
Este proyecto está bajo la Licencia MIT License Copyright (c) 2023 Omar Flores

---
⌨️ con ❤️ por [Omar Flores](https://github.com/OmarFloresPTY) 😊
