from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('',views.cart_detail,	name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove,name='cart_remove'),

    path('about.html/',views.aboutD,	name='aboutD'),
    path('add/<int:product_id>/about.html', views.aboutA, name='aboutA'),
    path('remove/<int:product_id>/about.html', views.aboutR,name='aboutR'),

    path('contact.html/',views.contactD,name='contactD'),
    path('add/<int:product_id>/contact.html', views.contactA, name='contactA'),
    path('remove/<int:product_id>/contact.html', views.contactR,name='contactR'),
]
