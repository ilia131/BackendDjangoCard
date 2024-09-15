from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)
    timezone =models.DateField()
    
    def get_image(self):
        if self.img:
            return 'http://127.0.0.1:8000/' + self.img.url
        return ''