from modeltranslation.translator import register, TranslationOptions
from web_app.models import Company, AboutUs, Main, ContactTo


@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('name', 'information')


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('name', 'text')


@register(Main)
class MainTranslationOptions(TranslationOptions):
    fields = ('name', 'text')


@register(ContactTo)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address',)
