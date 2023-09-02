from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from posts.models import Post

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)
    
    def lastmod(self, obj):
        return obj.created_at