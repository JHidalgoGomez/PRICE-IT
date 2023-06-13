from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Establece la ubicación del controlador de Chrome
chrome_path = './chromedriver'  # Reemplaza aquí la ubicación de tu controlador de Chrome

# Crea un objeto Service con la ubicación del controlador de Chrome
service = Service(chrome_path)

# Instancio el driver de Selenium utilizando el objeto Service
driver = webdriver.Chrome(service=service)

# Lista de URLs de los productos
urls = [
    "https://www.exito.com/coca-cola-zero-300-ml-236800/p",
    "https://www.exito.com/gaseosa-coca-cola-pet-600-ml-409900/p",
    "https://www.exito.com/bebida-gaseosa-original-316451/p",
    "https://www.exito.com/gaseosa-light-696914/p",
    "https://www.exito.com/colombiana-super-gigante-72256/p",
    "https://www.exito.com/gatorade-frutas-tropicales-500-ml-408762/p",
    "https://www.exito.com/hit-mango-pet-500-ml-86806/p",
    "https://www.exito.com/bebida-surtido-pag10-llev12-283704/p",
    "https://www.exito.com/pepsi-15-litros-963454/p",
    "https://www.exito.com/pony-malta-pet-330-ml-836322/p",
    "https://www.exito.com/bebida-gaseosa-sin-azucar-sprite-1500-ml-3067451/p",
    "https://www.exito.com/bretana-15-litros-963452/p",
    "https://www.exito.com/jamon-sanduche-x-450g-255284/p",
    "https://www.exito.com/jamon-estandar-libre-de-grasa-reducido-en-sodio-x-230g-711974/p",
    "https://www.exito.com/jamon-de-pollo-pietran-x-230g-416889/p",
    "https://www.exito.com/jamon-de-pavo-x-225g-304409/p",
    "https://www.exito.com/jamon-de-cerdo-sin-conserv-pietran-431-gramo-308920/p",
    "https://www.exito.com/jamon-ideal-x-400g-7947/p",
    "https://www.exito.com/salchicha-ranchera-x-230-749936/p",
    "https://www.exito.com/salchicha-perro-caliente-x-800-gr-634879/p",
    "https://www.exito.com/toallas-higienicas-invisible-rapigel-x40-und-precio-especial-147185/p",
    "https://www.exito.com/tampon-original-super-214982/p",
    "https://www.exito.com/jabon-intimo-agua-rosas-nosotras-310-ml-3086389/p",
    "https://www.exito.com/desodorante-rexona-clinical-cream-women-x-48-gr-111798/p",
    "https://www.exito.com/hs-sh-purificacion-208637/p",
    "https://www.exito.com/shampoo-head-shoulders-purificacion-capilar-x-700ml-208308/p",
    "https://www.exito.com/servilletas-familia-acolchamax-normal-x-100-und-51068/p"
]

for url in urls:
    # Voy a la página del producto
    driver.get(url)
    sleep(1)

    try:
        # Encuentro el elemento donde se encuentra el nombre
        nombre_element = WebDriverWait(driver, 110).until(
            EC.visibility_of_element_located((By.XPATH, '//h1[@class="vtex-store-components-3-x-productNameContainer mv0 t-heading-4"]/span[@class="vtex-store-components-3-x-productBrand "]')))
        nombre = nombre_element.text.strip()
    except:
        nombre = "N/A"

    print("Nombre:", nombre)

    try:
        # Encuentro el elemento donde se encuentra el precio
        precio_element = WebDriverWait(driver, 110).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="exito-vtex-components-4-x-PricePDP"]/span')))
        precio = precio_element.text.strip()
    except:
        precio = "N/A"

    print("Precio:", precio)
    print()

# Cierro el navegador
driver.quit()
