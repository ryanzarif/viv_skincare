from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.all_products, name='product'),
    path('detail/<int:id>/', views.product_detail, name='detail'),
    path('category/<int:id>', views.all_products, name='category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
