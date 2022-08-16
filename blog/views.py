from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(status=True)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = "article"

    def get_object(self):
        pk = self.kwargs.get('pk')
        article = Article.objects.filter(status=True, id=pk)
        return get_object_or_404(article)

#
# class UserListView(ListView):
#     model = User
#     template_name = 'blog/user_list.html'
#     context_object_name = 'users'
#
#     def get_queryset(self):
#         return User.objects.all()
#
#
# class UserDetailView(DetailView):
#     model = User
#     template_name = 'blog/user_detail.html'
#     context_object_name = 'user'
