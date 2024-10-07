from django.urls import path,include
from .views import post_list, post_create, post_detail
from .views import register, user_login, post_create, category_create, category_list


urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('post/create/', post_create, name='post_create'),
    path('category/create/', category_create, name='category_create'),
    path('categories/', category_list, name='category_list'),
    path('accounts/', include('django.contrib.auth.urls')),
]
    
