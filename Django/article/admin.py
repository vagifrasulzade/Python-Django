from django.contrib import admin
from .models import Article, Comment

# Register your models here.


class CommentInline(admin.TabularInline):
    """
    Article admin panelində comments-i inline göstərmə
    """
    model = Comment
    extra = 1  # Yeni comment əlavə etmək üçün 1 boş form
    fields = ('author', 'content', 'created_date')
    readonly_fields = ('created_date',)


class ArticleAdmin(admin.ModelAdmin):
    """
    Article admin konfigurasiyas
    CommentInline-ı əlavə etdik
    """
    list_display = ('title', 'author', 'created_date')
    list_filter = ('created_date', 'author')
    search_fields = ('title', 'content')
    inlines = [CommentInline]  # Article-nin altında comments-i göstər


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)