from django.contrib import admin
from app_blog.models import Post, Author

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'author']
    list_filter = ['author']
    search_fields = ['title', 'description']

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
