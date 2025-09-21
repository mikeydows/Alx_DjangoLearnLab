from rest_framework import serializers
from .models import Book  # Ensure you have a Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Includes all fields of the Book model

