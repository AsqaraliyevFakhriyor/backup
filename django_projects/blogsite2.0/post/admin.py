from django.contrib import admin

from .models import Post, PostComment, PostLike


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ('status', 'publish')


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user_name', "user_email", 'body')