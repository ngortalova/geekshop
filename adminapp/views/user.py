from django.core.exceptions import PermissionDenied

from authapp.models import ShopUser
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def check_if_superuser(user):
    if not user.is_superuser:
        raise PermissionDenied


@user_passes_test(check_if_superuser)
def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', content)


def user_create(request):
    pass


def user_update(request, pk):
    pass


def user_delete(request, pk):
    pass
