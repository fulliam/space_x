from rest_framework import serializers
from .models import Menu, InfoCard

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'title', 'url')

class InfoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoCard
        fields = ('id', 'top', 'middle_number', 'middle_text', 'bottom')
