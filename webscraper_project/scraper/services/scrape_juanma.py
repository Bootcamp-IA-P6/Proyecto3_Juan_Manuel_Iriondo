from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Para firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def scrape_website_juanma():
    # Configurar Selenium
    options = Options()
    options.add_argument('--headless')  # Ejecutar en modo headless
    options.add_argument('--no-sandbox')  # Requerido para algunos servidores
    options.add_argument('--disable-dev-shm-usage')  # Para evitar errores de memoria

   # Configurar el servicio de GeckoDriver
    service = Service("/usr/local/bin/geckodriver")
    # Crear el WebDriver de Firefox
    driver = webdriver.Firefox(service=service, options=options)

    # Navegar al sitio web
    url = "https://jumair.github.io/curriculum/"
    driver.get(url)
    print(driver.title)  
# Esperar a que los elementos estén presentes
    try:
        WebDriverWait(driver, 10).until(
            #EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2"))
            EC.presence_of_all_elements_located((By.CLASS_NAME, "parrafo"))
        )
        headers = driver.find_elements(By.CSS_SELECTOR, "h2")
        paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
    except Exception as e:
        print("Error al encontrar los elementos:", e)
        driver.quit()
        return []

    scraped_data = []
    for header, paragraph in zip(headers, paragraphs):
        scraped_data.append({
            "h2": header.text,
            "paragraph": paragraph.get_attribute("textContent"), 
        })

    print("Scraped data in scrape_website_juanma :", scraped_data)  # Para depuración
    driver.quit()
    return scraped_data