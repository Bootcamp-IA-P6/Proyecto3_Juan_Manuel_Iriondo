# Proyecto3_Juan_Manuel_Iriondo
## Django Scraper + Docker

Este proyecto scrapea mi página web del curriculum : jumair.github.io/curriculum y guarda los datos en una base de datos Sqlite3 y lo dockeriza todo para poder ejecutarlo en cualquier máquina.

## 🚀 Imagen pública en docker_hub (352 MB)
https://hub.docker.com/r/jmiriondo/proyecto3_juan_manual_iriondo-server

## 📝 Descripción del Proyecto

Este proyecto crea un servicio scraper activado con comando en Django y lo dockeriza.

### 📢 Explicación

- En el fichero Dockerfile que está situado en la raiz están las instrucciones para la creación de la imagen.
- El fichero compose.yaml sólo tiene el contexto y el puerto que expone.
- En requirements.txt se ha cambiado la línea donde ponía otra versión de Django por una versión inferior para que funcione (sugerido por chatgpt) **Django>=5.2,<6.0**

### 🛠️ Tecnologías Usadas

Python, Django, Selenium, Sqlite3 y Docker

### 💾 Uso y Acciones

Una vez levantado el contenedor podemos hacer lo siguiente :

```
docker ps #listamos nombre del contenedor

docker exec -it proyecto3_juan_manual_iriondo_server-1 bash #Ejecuta una terminal bash en el contenedor
**Si, me equivoque y puse manual en vez de manuel**

python webscraper_project/manage.py scraper #Ejecuta el scraper y guarda los datos en sqlite3

#Comprobamos los datos en la base de datos
apt-get update && apt-get install -y sqlite3

(Asegurate que estás en webscraper_project)
cd webscraper_project
sqlite3 db.sqlite3 #Abrimos terminal de sqlite3 con nuestra base de datos creada

#Los comandos en esta terminal se preceden de . y los comandos sql terminan con ;
sqlite> .tables
sqlite> SELECT * FROM scraper_scrapeddata;
sqlite> .quit #Volvemos a la terminal bash del contenedor

exit #Salimos al entorno virtual local
```

### 🪪 Contacto
Si tienes cualquier sugerencia o consulta, contáctame a través de juanmanuel.iriondo@gmail.com
