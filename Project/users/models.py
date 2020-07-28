from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#Pillow is library for working with pictures
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    #overriding our save method to resize pro pic automatically using Pillow
    #to sun the save method of our parent class use super
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 280 or img.width > 280:
            output_size = (280, 280)
            #to resize and save
            img.thumbnail(output_size)
            img.save(self.image.path)


