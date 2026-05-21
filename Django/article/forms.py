from django import forms
from .models import Article, Comment, Tag


class ArticleForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Etiketlər"
    )
    
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'tags']
        labels = {
            'title': 'Başlıq',
            'content': 'Məzmun',
            'image': 'Şəkil',
            'tags': 'Etiketlər'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Başlıq daxil edin'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Məzmun daxil edin'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        labels = {
            'author': 'Adınız',
            'content': 'Şərhiniz'
        }
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınızı daxil edin'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Şərhinizi yazın'}),
        }
