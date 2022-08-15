from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('title',)}
