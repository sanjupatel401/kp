from django.db import models

# Create your models here.

category_name=[
    ('clouth','clouths'),
    ('electronic','electronics'),
    ('mobile','mobiles'),
]


class product(models.Model):
    image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    brand_name=models.CharField(max_length=100)
    link=models.CharField(max_length=100)
    category=models.CharField(max_length=100,choices=category_name)
