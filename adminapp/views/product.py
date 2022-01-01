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
            return HttpResponseRedirect(reverse('admin:products', args=[pk]))
    else:
        product_form = ProductEditForm()

    content = {'title': title, 'update_form': product_form, 'category': category}
    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(check_if_superuser)
def product_read(request, pk):
    title = 'продукт/подробнее'
    product = get_object_or_404(Product, pk=pk)
    content = {'title': title, 'object': product, }

    return render(request, 'adminapp/product.html', content)


@user_passes_test(check_if_superuser)
def product_update(request, pk):
    title = 'продукт/редактирование'

    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES,
                                    instance=edit_product)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {'title': title, 'update_form': edit_form, 'category': edit_product.category}
    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(check_if_superuser)
def product_delete(request, pk):
    title = 'продукт/удаление'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin:products',
                                            args=[product.category.pk]))

    content = {'title': title, 'product_to_delete': product, 'category': product.category}

    return render(request, 'adminapp/product_delete.html', content)
