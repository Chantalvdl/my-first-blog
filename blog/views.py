from django.shortcuts import render
from .models import Post, Todo
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer


# Create your views here.

@login_required
def post_list(request):
    posts = Todo.objects.filter(author = request.user).order_by('deadline')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_list_title(request):
    posts_title = Todo.objects.filter(author = request.user).order_by('item')
    return render(request, 'blog/post_list_title.html', {'posts_title': posts_title})

@login_required
def post_list_others(request):
    posts_others = Todo.objects.order_by('author')
    return render(request, 'blog/post_list_others.html', {'posts_others': posts_others})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Todo, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Todo, pk=pk)
    post.delete()
    return redirect('post_list')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class Postlist(APIView):
    def get(self, request):
        posts = Todo.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
