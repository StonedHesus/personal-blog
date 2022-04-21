from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def posts(request):
    """
        This view renders all the post objects which are found within the database.
    """

    posts = Post.published.all()
    return render(request, 'blog/post/posts.html', {'posts': posts})

def post(request, year, month, day, post):
    """
        :parameter: year; an integer value which depicts the year when the post was created.
        :parameter: month; an integer value which depicts the month when the post was created.
        :parameter: day; an integer value which depicts the day when the post was created.
        :parameter: post; a Post type object.
        This view renders the details of a particular post, for which we know the year, month and day and implicitly
        the slug.
    """

    post = get_object_or_404(Post,  slug=post,
                                    status='published',
                                    published__year=year,
                                    published__month=month,
                                    published__day=day)

    return render(request, 'blog/post/post-detail.html', {'post': post})