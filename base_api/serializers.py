from rest_framework import serializers
from .models import Book, Author, Customer, Order

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # read_only_fields = []

    def to_representation(self, instance):
        # we can override response data here, if needed
        # self.Meta.model.objects.prefetch_related(Prefetch('related_model'))
        return super().to_representation(instance)

    def create(self, validated_data):
        instance = super().create(validated_data)
        # Additional logic can go here
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        # Additional logic can go here
        return instance

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'email', 'username', 'is_active', 'is_staff']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        # read_only_fields = []

    def to_representation(self, instance):
        # we can override response data here, if needed
        return super().to_representation(instance)

    def create(self, validated_data):
        instance = super().create(validated_data)
        # Additional logic can go here
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        # Additional logic can go here
        return instance