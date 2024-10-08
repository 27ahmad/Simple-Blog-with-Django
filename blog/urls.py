from django.urls import path,include
from .views import post_list, post_create, post_detail, author_posts, delete_post, category_detail
from .views import register, user_login, post_create, category_create, category_list, post_edit


urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('post/create/', post_create, name='post_create'),
    path('category/create/', category_create, name='category_create'),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:id>/', category_detail, name='category_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('author/posts/', author_posts, name='author_posts'),
    path('author/posts/delete/<int:post_id>/', delete_post, name='post_delete'),
    path('author/post/<int:pk>/edit/', post_edit, name='post_edit'),
]
    
