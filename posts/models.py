from django.db import models
from datetime import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='posts/images/', default='default.jpg')
class Image(models.Model):
    image = models.ImageField(upload_to='images/%y')
    def _str_(self):
        return self.caption