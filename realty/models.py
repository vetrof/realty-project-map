from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from manager.models import Manager


class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.city}'


class TypeRealty(models.Model):
    type_realty = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.type_realty}'


class Street(models.Model):
    street = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.street}'


class House(models.Model):
    house = models.IntegerField()

    def __str__(self):
        return f'{self.house}'


class Realty(models.Model):
    type_realty = models.ForeignKey(TypeRealty, on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT)
    cover_image = models.ImageField(upload_to='cover_image')
    s = models.FloatField()
    rooms = models.IntegerField()
    info = models.TextField()
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    street = models.ForeignKey(Street, on_delete=models.PROTECT)
    house = models.ForeignKey(House, on_delete=models.PROTECT)
    price = models.IntegerField()
    latitude = models.FloatField(blank=True, null=True, default=0)
    longitude = models.FloatField(blank=True, null=True, default=0)
    active = models.BooleanField()

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

    def __str__(self):
        return f'{self.title}'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_image')
    realty = models.ForeignKey(Realty, on_delete=models.PROTECT, related_name='images')
