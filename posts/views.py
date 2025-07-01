from django.shortcuts import render, get_object_or_404

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
        print("Received a POST request!")

        length = int(request.POST.get('length'))
        title = request.POST.get('title')
        description = request.POST.get('description')

        print(length)
        print(title)
        print(description)

        post = Post.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, length):
            PostImage.objects.create(
                post=post,
                image=request.FILES.get(f'images{file_num}'),
            )

    return render(request, 'posts/create_post.html')
