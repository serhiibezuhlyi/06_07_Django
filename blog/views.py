from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Article


# def index(request):
#     return render(request, "blog/index.html")


class Index(ListView):
    model = Article
    template_name = "blog/index.html"

    def get_queryset(self):
        return Article.objects.order_by("-publication_date")[:3]

class AllArticles(ListView):
    model = Article
    template_name = "blog/all_articles.html"

class ArticleDetail(DetailView):
    model = Article