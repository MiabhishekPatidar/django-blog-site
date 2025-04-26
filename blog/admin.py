from django.contrib import admin
from .models import Post, Comment

# Customize Post admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at', 'author')

# Customize Comment admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('author', 'content')
    list_filter = ('created_at',)

# Register models with admin site
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
