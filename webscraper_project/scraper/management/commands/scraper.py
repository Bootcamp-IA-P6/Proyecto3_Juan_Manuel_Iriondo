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