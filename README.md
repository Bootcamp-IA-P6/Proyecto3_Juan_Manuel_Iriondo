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
