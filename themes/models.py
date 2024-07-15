from django.db import models

# model for themes.
class SiteSetting(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField()