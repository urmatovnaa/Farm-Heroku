from rest_framework import serializers

from web_app.models import ProductPhoto, Company, Main, AboutUs, ContactTo


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'photo')


class CompanyDetailSerializer(serializers.ModelSerializer):
    products_photos = ProductPhotoSerializer(many=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'logo', 'information', 'web_site', 'key_words', 'products_photos')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTo
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = '__all__'
