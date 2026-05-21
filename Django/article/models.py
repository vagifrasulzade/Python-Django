from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Etiket Adı")
    
    class Meta:
        verbose_name = "Etiket"
        verbose_name_plural = "Etiketlər"
    
    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=150, verbose_name="Başlıq")  # input
    content = models.TextField(verbose_name="Məzmun")  # textarea
    tags = models.ManyToManyField(Tag, related_name="articles", blank=True, verbose_name="Etiketlər")
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="Article Images",blank=True, null=True,verbose_name="Şəkil")

    def __str__(self):
        return f"{self.title} | {self.author}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=100, verbose_name="Müəllif")
    content = models.TextField(verbose_name="Məzmun")
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author} - {self.article.title}"