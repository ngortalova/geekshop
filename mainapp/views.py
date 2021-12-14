from django.shortcuts import render
from datetime import datetime
from .models import ProductCategory, Product

menu_links = [
    {'view_name': 'index', 'name': 'домой'},
    {'view_name': 'products', 'name': 'продукты'},
    {'view_name': 'contact', 'name': 'контакты'},
]

submenu_links = [
    {'view_name': 'products_all', 'name': 'все'},
    {'view_name': 'products_home', 'name': 'дом'},
    {'view_name': 'products_office', 'name': 'офис'},
    {'view_name': 'products_modern', 'name': 'модерн'},
    {'view_name': 'products_classic', 'name': 'классика'},
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
    products = Product.objects.all()
    return render(request, 'mainapp/index.html', context={'menu_links': menu_links,
                                                          'date_now': datetime.now(),
                                                          'container_block_class': "slider",
                                                          'products': products,
                                                          })


def contact(request):

    return render(request, 'mainapp/contact.html', context={'menu_links': menu_links,
                                                            'title': 'наши контакты',
                                                            'container_block_class': "hero",
                                                            })


def products(request):

    return render(request, 'mainapp/products.html', context={'menu_links': menu_links,
                                                             'submenu_links': submenu_links,
                                                             'products_new': products_new,
                                                             'container_block_class': "hero-white",
                                                             })
