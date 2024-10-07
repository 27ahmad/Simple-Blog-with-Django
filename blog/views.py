from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm, PostForm, UserRegistrationForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post_detail', args=[pk]))
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Post Creation View
@login_required  # Ensure the user is logged in to create a post
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Do not save yet
            post.author = request.user  # Assign the author
            post.save()  # Now save the post
            return redirect('post_detail', pk=post.pk)  # Redirect to the post detail view
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

# Category Creation View
@login_required
def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
            return redirect('category_list')
    return render(request, 'blog/category_form.html')

@login_required
def author_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/author_posts.html', {'posts': posts})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('author_posts')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, 'blog/category_detail.html', {'category': category})

# Create your views here.

#testuser
#8Xfm#wfjJrHcq7J
