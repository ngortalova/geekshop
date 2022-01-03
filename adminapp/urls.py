from adminapp.views import category, user, product
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', user.UsersCreateView.as_view(), name='user_create'),
    path('users/read/', user.UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', user.UsersUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', user.UsersDeleteView.as_view(), name='user_delete'),

    path('categories/create/', category.category_create, name='category_create'),
    path('categories/read/', category.categories, name='categories'),
    path('categories/update/<int:pk>/', category.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', category.category_delete, name='category_delete'),

    path('products/create/category/<int:pk>/', product.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', product.products, name='products'),
    path('products/read/<int:pk>/', product.product_read, name='product_read'),
    path('products/update/<int:pk>/', product.product_update, name='product_update'),
    path('products/delete/<int:pk>/', product.product_delete, name='product_delete'),
]
