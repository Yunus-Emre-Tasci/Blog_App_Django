from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields=(
            "id",
            "name"
        )
        
class BlogSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()        
    