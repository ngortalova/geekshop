from django.shortcuts import render
from datetime import datetime
from .models import ProductCategory, Product

menu_links = [
    {'view_name': 'index', 'name': 'домой'},
    {'view_name': 'products:index', 'name': 'продукты'},
    {'view_name': 'contact', 'name': 'контакты'},
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
    products = Product.objects.all()[:4]
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


def products(request, pk=None):
    products_new = Product.objects.all()[:3]
    product_category = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context={'menu_links': menu_links,
                                                             'products_new': products_new,
                                                             'container_block_class': "hero-white",
                                                             "product_category": product_category,
                                                             })
