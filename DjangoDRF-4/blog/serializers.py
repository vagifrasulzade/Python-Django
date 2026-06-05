from rest_framework import serializers
from .models import Category, Post, Book


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source="category.name", read_only=True)

    def validate(self, data):
        if data["title"] == data["content"]:
            raise serializers.ValidationError("Basliq ve content eyni ola bilmez!")
        return data


    # def validate_title(self, value):
    #     qadagan_sozler = ["Qirmizi", "sari", "narinci"]

    #     for soz in qadagan_sozler:
    #         if soz.lower() in value.lower():
    #             raise serializers.ValidationError("Content icinde qadagan olunmus sozler var!")
    #     return value

    def validate_content(self, value):
        qadagan_sozler = ["Qirmizi", "sari", "narinci"]

        for soz in qadagan_sozler:
            if soz.lower() in value.lower():
                raise serializers.ValidationError("Content icinde qadagan olunmus sozler var!")
        return value



    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
