from django.urls import path
from .views import homepage_view, product_list

urlpatterns = [
    path('catalog/', product_list, name='catalog'),
    path('catalog/<slug:category_slug>', product_list, name='catalog_category'),
    path('', homepage_view, name='home'),

]