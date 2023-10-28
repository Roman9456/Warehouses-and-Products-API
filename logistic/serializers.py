from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']

    @staticmethod
    def get_products_by_title(query):
        return Product.objects.filter(title__icontains=query)

    @staticmethod
    def get_products_by_description(query):
        return Product.objects.filter(description__icontains=query)


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions_data = validated_data.pop('positions')
        stock = Stock.objects.create(**validated_data)

        for position_data in positions_data:
            product = position_data.pop('product')
            StockProduct.objects.create(stock=stock, product=product, **position_data)

        return stock

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        instance.positions.all().delete()

        for position_data in positions_data:
            product = position_data.pop('product')
            StockProduct.objects.create(stock=stock, product=product, **position_data)

        return stock

    @staticmethod
    def get_stocks_with_product(product_id):
        return Stock.objects.filter(positions__product_id=product_id)