import os

# Ruta del video que deseas reproducir
video_path = "/home/fernando/Videos/el_arte_de_nacer.mp4"

# Comando para reproducir el video en bucle en pantalla completa
command = f"vlc --fullscreen --loop '{video_path}'"

# Ejecuta el comando para reproducir el video
os.system(command)