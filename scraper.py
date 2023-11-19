import os
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

def is_valid_image_extension(url):
    # Verifica si la URL termina en alguna de las extensiones válidas
    return any(url.endswith(ext) for ext in [".jpg", ".jpeg", ".png"])

def download_images1():
    response = requests.get(URL1, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    img_tags = soup.find_all("img")

    if not os.path.exists("imagenes/hombres_train"):
        os.makedirs("imagenes/hombres_train")

    for img in img_tags:
        img_url = img.get("src", "")
        # Ignora las imágenes codificadas en base64 y verifica la extensión
        if img_url.startswith("http") and is_valid_image_extension(img_url) and img_url.endswith("265w.png"):
            img_name = os.path.basename(img_url)
            with open(f"imagenes/hombres_train/{img_name}", "wb") as img_file:
                img_data = requests.get(img_url).content
                img_file.write(img_data)
                
def download_images2():
    response = requests.get(URL2, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    img_tags = soup.find_all("img")

    if not os.path.exists("imagenes/mujeres_train"):
        os.makedirs("imagenes/mujeres_train")

    for img in img_tags:
        img_url = img.get("src", "")
        # Ignora las imágenes codificadas en base64 y verifica la extensión
        if img_url.startswith("http") and is_valid_image_extension(img_url) and img_url.endswith("265w.png"):
            img_name = os.path.basename(img_url)
            with open(f"imagenes/mujeres_train/{img_name}", "wb") as img_file:
                img_data = requests.get(img_url).content
                img_file.write(img_data)
                
def download_images3():
    response = requests.get(URL1, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    img_tags = soup.find_all("img")

    if not os.path.exists("imagenes/hombres_validation"):
        os.makedirs("imagenes/hombres_validation")

    for img in img_tags:
        img_url = img.get("src", "")
        # Ignora las imágenes codificadas en base64 y verifica la extensión
        if img_url.startswith("http") and is_valid_image_extension(img_url) and img_url.endswith("265w.png"):
            img_name = os.path.basename(img_url)
            with open(f"imagenes/hombres_validation/{img_name}", "wb") as img_file:
                img_data = requests.get(img_url).content
                img_file.write(img_data)

def download_images4():
    response = requests.get(URL2, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    img_tags = soup.find_all("img")

    if not os.path.exists("imagenes/mujeres_validation"):
        os.makedirs("imagenes/mujeres_validation")

    for img in img_tags:
        img_url = img.get("src", "")
        # Ignora las imágenes codificadas en base64 y verifica la extensión
        if img_url.startswith("http") and is_valid_image_extension(img_url) and img_url.endswith("265w.png"):
            img_name = os.path.basename(img_url)
            with open(f"imagenes/mujeres_validation/{img_name}", "wb") as img_file:
                img_data = requests.get(img_url).content
                img_file.write(img_data)
                
for pages in range(1,5):
    URL1 = "https://www.ea.com/es/games/ea-sports-fc/ratings?gender=0&page=" + str(pages) #hombres
    URL2 = "https://www.ea.com/es/games/ea-sports-fc/ratings?gender=1&page=" + str(pages) #mujeres
                
    if __name__ == "__main__":
        download_images1()
        download_images2()

for pages in range(6,7):
    URL1 = "https://www.ea.com/es/games/ea-sports-fc/ratings?gender=0&page=" + str(pages) #hombres
    URL2 = "https://www.ea.com/es/games/ea-sports-fc/ratings?gender=1&page=" + str(pages) #mujeres   
                
    if __name__ == "__main__":
        download_images3()
        download_images4()
    

# docker build -t scraper .
# docker run --name scraper -v "$(pwd)/imagenes:/app/imagenes" scraper python scraper.py