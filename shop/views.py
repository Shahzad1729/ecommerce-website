from django.shortcuts import get_object_or_404, render, get_list_or_404
from numpy import product
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product':	product,'cart_product_form':	cart_product_form})


def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        #	If	page	is	not	an	integer	deliver	the	first	page
        products= paginator.page(1)
    except EmptyPage:
        #	If	page	is	out	of	range	deliver	last	page	of	results
        products = paginator.page(paginator.num_pages)
    
    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories,'products': products})


def about(request):
    return render(request, 'shop/about.html')
 
def aboutProL(request,category_slug=None):
    return render(request, 'shop/about.html')

def aboutProD(request,id, slug):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')

def contactProL(request,category_slug=None):
    return render(request, 'shop/contact.html')

def contactProD(request,id, slug):
    return render(request, 'shop/contact.html')