from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import ProductCategory, Product
import random


menu_links = [
    {'view_name': 'index', 'active_if': ['index'], 'name': 'домой'},
    {'view_name': 'products:index', 'active_if': ['products:index', 'products:category', 'products:product'], 'name': 'продукты'},
    {'view_name': 'contact', 'active_if': ['contact'], 'name': 'контакты'},
]


def index(request):
    products = random.sample(list(Product.objects.all()), 4)

    return render(request, 'mainapp/index.html', context={'menu_links': menu_links,
                                                          'date_now': datetime.now(),
                                                          'container_block_class': "slider",
                                                          'products': products,
                                                          'hot_products': Product.objects.hot_product,

                                                          })


def contact(request):

    return render(request, 'mainapp/contact.html', context={'menu_links': menu_links,
                                                            'title': 'наши контакты',
                                                            'container_block_class': "hero",
                                                            })


def product(request, pk):
    product = get_object_or_404(Product, id=pk)
    product_categories = ProductCategory.objects.all()
    products_new = Product.objects.filter(category_id=product.category_id)
    return render(request, 'mainapp/product.html', context={'menu_links': menu_links,
                                                            'container_block_class': "hero-white",
                                                            'product': product,
                                                            'product_categories': product_categories,
                                                            'products_new': products_new,
                                                             })


def products(request, pk=None):
    if not pk:
        selected_category = ProductCategory.objects.first()
    else:
        selected_category = get_object_or_404(ProductCategory, id=pk)

    products_new = Product.objects.filter(category_id=pk)
    product_categories = ProductCategory.objects.all()
    products = random.sample(list(Product.objects.all()), 3)
    return render(request, 'mainapp/products.html', context={'menu_links': menu_links,
                                                             'products_new': products_new,
                                                             'container_block_class': "hero-white",
                                                             'product_categories': product_categories,
                                                             'products': products,
                                                             'selected_category': selected_category,
                                                             'hot_product': Product.objects.hot_product,
                                                             })


