from rest_framework import serializers
from blog.models import Article
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name']


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        fields = '__all__'

    def validate_title(self, value):
        filter_list = ['javascript', 'laravel', 'asp.net', 'php']
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError(f'what the hack!!??? {i} really???')
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
