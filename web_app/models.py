from django.db import models


class ProductPhoto(models.Model):
    photo = models.ImageField(upload_to='product_photo/')
    company = models.ForeignKey('web_app.Company', models.CASCADE, related_name='products_photos')

    def __str__(self):
        return f'{self.photo}'


class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo/')
    photo = models.ImageField(upload_to='company_photo/')
    information = models.TextField()
    key_words = models.CharField(max_length=255, null=True)
    web_site = models.URLField()

    class Meta:
        verbose_name_plural = 'companies'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return f'{self.name}'


class Contact(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=14)
    location = models.URLField()
    email = models.EmailField()
    whatsapp = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.address}'


class AboutUs(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = 'AboutUs'

    def __str__(self):
        return f'{self.name}'
