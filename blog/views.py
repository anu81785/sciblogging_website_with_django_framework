from django.shortcuts import render
from posts.models import Post
from .models import About, Contact
from django.http import HttpResponse
# Create your views here.
def frontpage(request):
    all_posts=Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'blog/frontpage.html', {"all_posts": all_posts})


def contact(request):
    items=Contact.objects.all().values()
    return render(request, 'blog/contact.html', {'items': items})

def about(request):
    items=About.objects.all().values()
    return render(request, 'blog/about.html', {'items': items})


def robots_txt(request):
    text=[
        "User-Agent: *",
        "Disallow: /admin/",
    ]

    return HttpResponse("\n".join(text), content_type="text/plain")

