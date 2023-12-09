import os
from pytube import YouTube
from tqdm import tqdm

def clear_screen():
    # Función para limpiar la pantalla según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def download_video(url, index):
    try:
        clear_screen()  # Limpia la pantalla

        print(f"Descargando #{index}: {url}")

        yt = YouTube(url)

        # Extraer solo el audio
        video = yt.streams.filter(only_audio=True).first()

        # Descargar el archivo
        out_file = video.download()

        # Guardar el archivo como MP3
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # Resultado exitoso
        print(f"{yt.title} se ha descargado exitosamente como MP3 en la carpeta:", os.path.abspath('.'))
        print("")

    except Exception as e:
        print(f"Ocurrió un error al descargar el video: {str(e)}")
        input("Presiona Enter para continuar...")  # Espera a que el usuario presione Enter

def main():
    file_path = "./links.txt"  # Ruta al archivo de texto con los enlaces
    with open(file_path, "r") as file:
        links = file.read().splitlines()  # Lee los enlaces desde el archivo

    i = 1
    for link in links:
        print(f"Descargar #{i}")
        download_video(link, i)
        i += 1

main()
