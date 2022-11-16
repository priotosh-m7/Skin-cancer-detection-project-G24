from django.db import models

# Create your models here.
class UploadImage(models.Model):
    user = models.CharField('username',max_length=200)
    image = models.ImageField(null=True,blank=True,upload_to='images/')

    def __str__(self) :
        return self.user