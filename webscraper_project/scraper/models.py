from django.db import models

# Create your models here.
class ScrapedDataJuanma(models.Model):
    h2 = models.CharField(max_length=100)
    paragraph = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
