from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title + ' - ' + self.title


class Dresses(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title + ' - ' + self.title

class Sweaters(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title + ' - ' + self.title

class Skirts(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title + ' - ' + self.title

class Jeans(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title + ' - ' + self.title

class Sarees(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title + ' - ' + self.title

class Shirts(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title + ' - ' + self.title

class Salwars(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title + ' - ' + self.title

class Sandals(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title + ' - ' + self.title

class Products(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title + ' - ' + self.title

class Kids(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title + ' - ' + self.title
