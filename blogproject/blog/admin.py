from django.contrib import admin
from blog.models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'user', 'title', 'content', 'view_count', 'like_count', 'create_date', 'update_date')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')