from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.


def home__view(request):
    return render(request, "index.html")


# domain/articles/
def articles__view(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})


# domain/article/1
def article__detail__view(request, id):
    article = Article.objects.get(id=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect("article-detail", id=id)
    else:
        form = CommentForm()

    context = {"article": article, "form": form}
    return render(request, "article_detail.html", context)


@login_required()
def add__article__view(request):

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("articles")

    else:
        form = ArticleForm()

    return render(request, "article_form.html", {"form": form})


