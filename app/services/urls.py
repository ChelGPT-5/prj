from django.urls import path

from services import views

app_name = 'services'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),
]
