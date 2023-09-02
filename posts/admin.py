from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class CommentItemInline(admin.TabularInline):
    model=Comment
    raw_id_fields=['post']

class PostAdmin(admin.ModelAdmin):
    """Post administrator. It manages the Post model."""

    fieldsets = [
        (None, {"fields": ["title"]}),
        ("Intro", {"fields": ["intro"]}),
        ("Slug", {"fields": ["slug"]}),
        ("Status", {"fields": ["status"]}),
        ("Body", {"fields": ["body"]}),
    ]
    search_fields=['title', 'intro', 'body']
    list_display=['title', 'slug', 'created_at', 'status']
    list_filter=['created_at', 'status']
    inlines=[CommentItemInline]
    prepopulated_fields={'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
