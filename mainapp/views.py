from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import ProductCategory, Product
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


menu_links = [
    {'view_name': 'index', 'active_if': ['index'], 'name': 'домой'},
    {'view_name': 'products:index', 'active_if': ['products:index', 'products:category', 'products:product'], 'name': 'продукты'},
    {'view_name': 'contact', 'active_if': ['contact'], 'name': 'контакты'},
]

list_of_products = Product.objects.filter(is_active=True)


def index(request):

    products = list_of_products.order_by("price")

    page = int(request.GET.get('page', default='1'))
    per_page = int(request.GET.get('per_page', default='4'))

    return render(request, 'mainapp/index.html', context={'menu_links': menu_links,
                                                          'date_now': datetime.now(),
                                                          'container_block_class': "slider",
                                                          'products': Paginator(products,per_page).get_page(page),
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
    products_new = Product.objects.filter(category_id=product.category_id, is_active=True)
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



    page = int(request.GET.get('page', default='1'))
    per_page = int(request.GET.get('per_page', default='3'))
    product_categories = ProductCategory.objects.all()
    products_new = list_of_products.order_by("price").filter(category_id=pk)
    products = list_of_products.order_by("price")
    content = {'menu_links': menu_links,
               'products_new': Paginator(products_new, per_page).get_page(page),
               'container_block_class': "hero-white",
               'product_categories': product_categories,
               'products': Paginator(products, per_page).get_page(page),
               'selected_category': selected_category,
               'hot_product': Product.objects.hot_product,
               }

    return render(request, 'mainapp/products.html', content)


