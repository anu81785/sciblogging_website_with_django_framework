from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    ACTIVE='active'
    DRAFT='draft'
    CHOICES_STATUS=(
        (ACTIVE, 'Active'), 
        (DRAFT, 'Draft')
    )
    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255)
    intro=models.TextField(max_length=500)
    body=RichTextUploadingField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    class Meta:
        ordering=('-created_at',)
    

    def __str__(self):
        return self.title     

    def get_absolute_url(self):
        return '/%s/' % (self.slug)

class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering=('-created_at',)

