from django.contrib import admin
from django.contrib.admin.options import TabularInline
from modeltranslation.admin import TranslationAdmin
from web_app.models import ProductPhoto, Company, Contact, AboutUs


class ProductImageAdminInLine(TabularInline):
    extra = 1
    model = ProductPhoto
    max_num = 100


@admin.register(Company)
class PersonAdmin3(TranslationAdmin):
    inlines = (ProductImageAdminInLine,)
    list_display = ('name', 'web_site')


@admin.register(Contact)
class PersonAdmin3(TranslationAdmin):
    pass


@admin.register(AboutUs)
class Admin2(TranslationAdmin):
    pass
