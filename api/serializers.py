from rest_framework.serializers import ModelSerializer
from .models import Product

# class serializer
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'