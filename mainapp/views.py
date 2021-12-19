from django.shortcuts import render
from datetime import datetime


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


def index(request):

    return render(request, 'mainapp/index.html', context={'menu_links': menu_links,
                                                          'date_now': datetime.now()})


def contact(request):

    return render(request, 'mainapp/contact.html', context={'menu_links': menu_links,
                                                            'title': 'наши контакты'
                                                            })


def products(request):

    return render(request, 'mainapp/products.html', context={'menu_links': menu_links,
                                                             'submenu_links': submenu_links})
