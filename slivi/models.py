from django.db import models

# Create your models here.

class Captcha(models.Model):
    captcha_text = models.CharField(max_length=5)
    captcha_image = models.ImageField(upload_to='slivi/media', null=True, blank=True)

