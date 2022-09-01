from modeltranslation.translator import register, TranslationOptions
from web_app.models import Company, AboutUs, Contact


@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('name', 'information')


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('name', 'text')


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address',)
