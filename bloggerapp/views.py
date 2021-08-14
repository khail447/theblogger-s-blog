from django.shortcuts import redirect, render

from .models import Category, Post
from .forms import commentform
# Create your views here.
def frontpage(request):
    posts= Post.objects.all()

    context={
        'posts': posts
    }
    return render(request, 'frontpage.html', context)

def detail(request, slug):
    post= Post.objects.get(slug=slug)

    if request.method=='POST':
        form= commentform(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()

            return redirect('detail', slug=post.slug)
    else:
        form= commentform()

    context={
        'post': post,
        'form': form
    }
    return render(request, 'detail.html', context)

def categoryview(request, slug):
    category= Category.objects.get(slug=slug)

    context={
        'category': category
    }
    return render(request, 'category.html', context)
