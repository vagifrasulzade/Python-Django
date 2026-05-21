from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
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
    comments = article.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article-detail', id=id)
    else:
        form = CommentForm()
    
    return render(request, "article_detail.html", {
        "article": article,
        "comments": comments,
        "form": form
    })


# Article oluştur
@login_required(login_url='login')
def article_create__view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()  # Tags'ı kaydet
            return redirect('article-detail', id=article.id)
    else:
        form = ArticleForm()
    
    return render(request, 'article_form.html', {'form': form, 'title': 'Yeni Məqalə Əlavə Edin'})


# Article düzenle
@login_required(login_url='login')
def article_edit__view(request, id):
    article = get_object_or_404(Article, id=id)
    
    # Yalnız yazarı düzenleyebilsin
    if article.author != request.user:
        return redirect('articles')
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article-detail', id=article.id)
    else:
        form = ArticleForm(instance=article)
    
    return render(request, 'article_form.html', {'form': form, 'title': 'Məqaləni Redaktə Edin'})


# Article sil
@login_required(login_url='login')
def article_delete__view(request, id):
    article = get_object_or_404(Article, id=id)
    
    # Yalnız yazarı silebilsin
    if article.author != request.user:
        return redirect('articles')
    
    if request.method == 'POST':
        article.delete()
        return redirect('articles')
    
    return render(request, 'article_confirm_delete.html', {'article': article})

