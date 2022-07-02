from django.urls import path
from . import views
app_name = 'orders'
urlpatterns = [
    path('create/',	views.order_create,	name='order_create'),

    path('create/about.html',	views.about,	name='order_create'),

    path('create/contact.html',	views.contact,	name='order_create'),
]
