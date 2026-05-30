from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Article, Comment

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', "category", "tags"]
        widgets = {
            "tags": CheckboxSelectMultiple()
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']