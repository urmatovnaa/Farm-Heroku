from rest_framework import serializers

from web_app.models import ProductPhoto, Company, AboutUs, Contact


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'name_en', 'name_ru', 'photo')


class CompanyDetailSerializer(serializers.ModelSerializer):
    products_photos = ProductPhotoSerializer(many=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'name_en', 'name_ru', 'logo', 'information',
                  'information_en', 'information_ru', 'web_site', 'key_words', 'products_photos')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

