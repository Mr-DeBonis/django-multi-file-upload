from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from posts.forms import AddPostForm
from posts.models import Post, PostImage


def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/blog.html', {'posts': posts})


def detail_view(request, id):
    post = get_object_or_404(Post, pk=id)
    photos = PostImage.objects.filter(post=post)
    context = {
        'post': post,
        'photos': photos
    }
    return render(request, 'posts/detail.html', context=context)

def create_post_view(request):

    if request.method == 'POST':
        form = AddPostForm(request.POST)
        files = request.FILES.getlist('filepond')
        if form.is_valid():
            post = form.save()

            for file in files:
                PostImage.objects.create(
                    post=post,
                    image=file
                )

            messages.success(request, "Post saved.")
            return redirect("posts:index")
    else:
        form = AddPostForm()

    context = {
        'form': form,
    }

    return render(request, 'posts/create_post.html', context = context)
