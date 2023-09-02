from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError

# Create your models here.
class Contact(models.Model):
    title=models.CharField(max_length=255, default='Contact-Info')
    address=models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    email=models.EmailField(blank=True, null=True)
    linkedin_url=models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Contact"

class About(models.Model):
    title=models.CharField(max_length=255, default='About')
    body=RichTextUploadingField(blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About"
