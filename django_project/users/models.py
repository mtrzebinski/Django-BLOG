from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def saved(self):
        super().saved()

        photo = Image.open(self.image.path)

        if photo.height > 300 or photo.width > 300:
            size = (300, 300)
            photo.thumbnail(size)
            photo.save(self.image.path)
