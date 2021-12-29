from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from mainapp.models import ProductCategory


def check_if_superuser(user):
    if not user.is_superuser:
        raise PermissionDenied
    return True


@user_passes_test(check_if_superuser)
def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


@user_passes_test(check_if_superuser)
def category_create(request):
    title = 'категории/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(check_if_superuser)
def category_update(request, pk):
    pass


@user_passes_test(check_if_superuser)
def category_delete(request, pk):
    pass
