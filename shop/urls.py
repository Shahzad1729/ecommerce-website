from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('',views.product_list,	name='product_list'),
    path('<slug:category_slug>/',	views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
    
    path('about.html/',views.about,	name='about'),
    path('<slug:category_slug>/about.html/',	views.aboutProL,	name='aboutL'),
    path('<int:id>/<slug:slug>/about.html/',views.aboutProD,	name='aboutD'),
    
    path('contact.html/',views.contact,	name='contact'),
    path('<slug:category_slug>/contact.html/',views.contactProL,	name='contactL'),
    path('<int:id>/<slug:slug>/contact.html/',views.contactProD,	name='contactD'),
]
