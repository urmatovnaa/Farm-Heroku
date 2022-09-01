from django.urls import path
from web_app.views import CompanyView, ContactViewSet, AboutUsViewSet

urlpatterns = [
    path('company/', CompanyView.as_view({'get': 'list'}), name='company_list'),
    path('company/<int:pk>', CompanyView.as_view(
        {'get': 'retrieve'}), name='company-detail'),
    path('contacts/', ContactViewSet.as_view({'get': 'list'}), name='contacts'),
    path('about_us/', AboutUsViewSet.as_view({'get': 'list'}), name='about-us'),
]
