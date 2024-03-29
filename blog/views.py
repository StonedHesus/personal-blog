from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def posts(request):
    """
        This view renders all the post objects which are found within the database.
    """

    posts = Post.published.all()
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer serve the first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page exceeds the number of existing pages then serve the last page.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/posts.html', {'page': page, 'posts': posts})

def post(request, year, month, day, post):
    """
        :parameter: year; an integer value which depicts the year when the post was created.
        :parameter: month; an integer value which depicts the month when the post was created.
        :parameter: day; an integer value which depicts the day when the post was created.
        :parameter: post; a Post type object.
        This view renders the details of a particular post, for which we know the year, month and day and implicitly
        the slug.
    """

    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'blog/post/posts-detail.html', {'post': post})