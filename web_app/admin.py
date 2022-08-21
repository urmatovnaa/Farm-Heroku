from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from web_app.models import ProductPhoto, Company, Contact, Main, AboutUs


@admin.register(Company)
class PersonAdmin3(TranslationAdmin):
    list_display = ('name', 'web_site')


@admin.register(ProductPhoto)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class PersonAdmin3(TranslationAdmin):
    pass


@admin.register(AboutUs)
class Admin2(TranslationAdmin):
    pass


@admin.register(Main)
class Admin4(TranslationAdmin):
    pass

