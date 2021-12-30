from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.http import HttpResponseRedirect
from django.urls import reverse
from adminapp.forms import ProductEditForm


def check_if_superuser(user):
    if not user.is_superuser:
        raise PermissionDenied
    return True


@user_passes_test(check_if_superuser)
def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)


@user_passes_test(check_if_superuser)
def product_create(request, pk):
    title = 'продукт/создание'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products'))
    else:
        product_form = ProductEditForm(initial={'category': category})

    content = {'title': title, 'update_form': product_form}

    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(check_if_superuser)
def product_read(request, pk):
    pass


@user_passes_test(check_if_superuser)
def product_update(request, pk):
    pass


@user_passes_test(check_if_superuser)
def product_delete(request, pk):
    pass
