from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import CommentForm

# Create your views here.
def detail(request, slug):
    post=get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail', slug=slug)         
    else:
        form=CommentForm()
    return render(request, 'posts/detail.html', {'post':post, 'form': form})


def search(request):
    query=request.GET.get('query', '')
    posts=Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'posts/search.html', {'posts': posts, 'query': query})

