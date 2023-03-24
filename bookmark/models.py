from django.db import models

# class안에서는 lazy 사용해야 함
from django.urls import reverse

# Create your models here.

#실행어:  python manage.py migrate bookmark
#실행어:  python manage.py makemigrations bookmark

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self) -> str:
        return "이름: " + self.site_name + " , 주소: " + self.url
    

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])