from django.shortcuts import render, get_object_or_404

from posts.models import Post, PostImage


def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/blog.html', {'posts': posts})


def detail_view(request, id):
    post = get_object_or_404(Post, pk=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'posts/detail.html',
                  {
                      'post': post,
                      'photos': photos
                  })
