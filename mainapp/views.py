from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import ProductCategory, Product
from cartapp.models import Cart
import random


menu_links = [
    {'view_name': 'index', 'active_if': ['index'], 'name': 'домой'},
    {'view_name': 'products:index', 'active_if': ['products:index', 'products:category'], 'name': 'продукты'},
    {'view_name': 'contact', 'active_if': ['contact'], 'name': 'контакты'},
]


products_new = [
    {'href': '#',
     'name': 'product_11',
     'title': "Бра",
     'img': "img/product-11.jpg",
     'text': 'Не оторваться'},
    {'href': '#',
     'name': 'img/product_21',
     'title': "Стул как стул",
     'img': 'img/product-21.jpg',
     'text': 'Не оторваться'},
    {'href': '#',
     'name': 'product_11',
     'title': "Лампа как лампа",
     'img': 'img/product-31.jpg',
     'text': 'Не оторваться'},
    ]




def index(request):
    products = random.sample(list(Product.objects.all()), 4)
    #cart = Cart.objects.filter(user=request.user)
    return render(request, 'mainapp/index.html', context={'menu_links': menu_links,
                                                          'date_now': datetime.now(),
                                                          'container_block_class': "slider",
                                                          'products': products,
                                                          #'cart': cart,
                                                          })


def contact(request):
    cart = Cart.objects.filter(user=request.user)

    return render(request, 'mainapp/contact.html', context={'menu_links': menu_links,
                                                            'title': 'наши контакты',
                                                            'container_block_class': "hero",
                                                            'cart': cart,
                                                            })


def products(request, pk=None):
    cart = Cart.objects.filter(user=request.user)
    if not pk:
        selected_category = ProductCategory.objects.first()
    else:
        selected_category = get_object_or_404(ProductCategory, id=pk)

    products_new = Product.objects.filter(category_id=pk)
    product_category = ProductCategory.objects.all()
    products = random.sample(list(Product.objects.all()), 3)

    return render(request, 'mainapp/products.html', context={'menu_links': menu_links,
                                                             'products_new': products_new,
                                                             'container_block_class': "hero-white",
                                                             "product_category": product_category,
                                                             "products": products,
                                                             "selected_category": selected_category,
                                                             'cart': cart,

                                                             })
