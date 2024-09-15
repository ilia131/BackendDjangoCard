from .models import Card 
from rest_framework import serializers



class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('img' , 'title' ,'description', 'timezone' , 'get_image' , 'id')   
        extra_kwargs = {  
            'title': {'required': False},  
            'description': {'required': False,},  
            'img': {'required': False}  ,
            'timezone':{'required': False}
        } 