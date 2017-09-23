from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Dresses, Sweaters, Skirts, Jeans, Shirts, Sarees, Salwars, Sandals, Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'image')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class DressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dresses
        fields = ('title', 'price', 'image')

class JeansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jeans
        fields = ('title', 'price', 'image')

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('title', 'price', 'image')

class SalwarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salwars
        fields = ('title', 'price', 'image')

class SandalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sandals
        fields = ('title', 'price', 'image')
class SareesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sarees
        fields = ('title', 'price', 'image')

class ShirtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shirts
        fields = ('title', 'price', 'image')

class SkirtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skirts
        fields = ('title', 'price', 'image')

class SweatersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweaters
        fields = ('title', 'price', 'image')
