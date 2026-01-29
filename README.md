# Proyecto3_Juan_Manual_Iriondo
## Django Scraper

Este proyecto scrapea mi página web del curriculum : jumair.github.io/curriculum

## 📝 Descripción del Proyecto

Este proyecto crea un servicio scraper activado con comando en Django

### 📢 Explicación

- En el fichero settings.py que está situado en webscraper_project/webscraper_project, en INSTALLED_APPS se ha añdido el servicio scraper para que pueda ser ejecutado.
- En el directorio scraper que es el servicio tenemos lo siguiente :
    - Un fichero models.py con el modelo de datos de la base de datos. Se guardarán el h2, el párrafo y la fecha en la que se hace el scraping.
    - En el fichero scrape_juanma.py está la lógica que obtiene los datos de la página web. Se obtienen el *h2* y el *p* cuando todos los elementos de CLASS_NAME = "parrafo" estén creados en la página.
    - El fichero scraper.py contiene las intrucciones para ejecutar el scraping llamando a la función **scrape_website_juanma()** que está en el fichero scrape_juanma.py.

### 🎯 Ficheros

**webscraper_project/webscraper_project/settings.py**

```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'scraper'
]
```
**webscraper_project/scraper/models.py**

´´´
from django.db import models

# Create your models here.
class ScrapedDataJuanma(models.Model):
    h2 = models.CharField(max_length=100)
    paragraph = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
´´´

**webscraper_project/scraper/services/scrape_juanma.py**

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Para Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_website_juanma():
    # Configurar Selenium
    options = Options()
    options.add_argument('--headless')  # Ejecutar en modo headless
    options.add_argument('--no-sandbox')  # Requerido para algunos servidores
    options.add_argument('--disable-dev-shm-usage')  # Para evitar errores de memoria

    # 🔹 Aquí inicializamos correctamente `service`
    service = Service(ChromeDriverManager().install())

    # Para Chrome
    # Selenium Manager se encargará de descargar y gestionar el WebDriver
    #service = Service()  # No es necesario especificar el ejecutable
    driver = webdriver.Chrome(service=service, options=options)

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
```

**webscraper_project/scraper/management/commands/scraper.py**

```
from django.core.management.base import BaseCommand
from scraper.services.scrape_juanma import scrape_website_juanma
from scraper.models import ScrapedDataJuanma

class Command(BaseCommand):
    help = "Run the web scraper de Juanma"
    # Hereda de BaseCommand, lo que permite que este comando sea ejecutable mediante python manage.py <nombre_comando>.

    def handle(self, *args, **kwargs):
        # Ejecuta función
        data = scrape_website_juanma()
        print("Scraped Data in Command :", data)  # Agrega esta línea para depurar
        #print("Scraped Data in position 0 :", data[0]["paragraph"])  # Agrega esta línea para depurar y ver el párrafo del primer elemento 
        # Guarda
        for item in data:
            ScrapedDataJuanma.objects.create(h2=item["h2"], paragraph=item["paragraph"])
        # Confirma
        self.stdout.write(self.style.SUCCESS("Scraping completed!"))
```

### 🛠️ Tecnologías Usadas

Python, Django, Selenium, webdriver-manager

### 💾 Instalación
1.- Clona el repositorio

    git clone https://github.com/Bootcamp-IA-P6/Proyecto3_Juan_Manual_Iriondo.git

2.- Navega al directorio del proyecto

    cd "directorio_del_proyecto"

### 🚀 Uso

1.- Instala un entorno virtual, actívalo e instala las librerías

    python -m venv venv
    source venv/Scripts/activate (source venv/bin/activate si estás en Mac)
    pip install -r requirements.txt

2.- Ejecuta el servicio **scraper**. 
*Debes estar ubicado en el directorio webscraper_project que es donde se encuentra el fichero manage.py*

    cd webscraper_project

    python manage.py scraper

3.- Puedes comprobar la estructura en SQlite para ver que todo va bien con https://sqlitebrowser.org/ (Por defecto Django trabaja con Sqlite podrias cambiarlo en settings.py)

### 🪪 Contacto
Si tienes cualquier sugerencia o consulta, contáctame a través de juanmanuel.iriondo@gmail.com
