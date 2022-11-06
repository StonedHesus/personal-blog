# Imports from existing modules.
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Imports from custom modules.
from .models import Post

def render_posts(request):
    """
        This routine is responsible for dynamically creating a new view which renders all the post
        contain within the database.

        In order to be able to properly manage resources, and to offer a more stylish approach
        for showcasing this information, we are utilising Django's paginator module, which enables
        us to impose a maximum number of elements to be present within a page, hence we can trim
        our data set into sizable bites, that we can after that rearrange in a standard, multiple
        pages booklet like view.

        Author : Andrei-Paul Ionescu.
    """

    # Retrieve all the published posts.
    posts = Post.published.all()
    # Create a new paginator that has a maximum number of one post per page.
    paginator = Paginator(posts, 1)
    # Retrieve the page element from within the server.
    page = request.GET.get('page')
    # Try adding that page to the paginator object.
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer serve the first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page exceeds the number of existing pages then serve the last page.
        posts = paginator.page(paginator.num_pages)
    # Finally, render the currently requested view.
    return render(request, 'blog/post/posts.html', {'page': page, 'posts': posts})

def render_post(request, year, month, day, post):
    """
        :parameter: year    - an integer value which indicates the year when the post was created.
        :parameter: month   - an integer value which indicates the month when the post was created.
        :parameter: day     - an integer value which indicates the day when the post was created.
        :parameter: post    - a Post type object.

        This view renders the details of a particular post, for which we know the year, month and day and implicitly
        the slug.

        Author: Andrei-Paul Ionescu.
    """

    # Try retrieving the object whose fields match the ones provided to the method as parameters.
    # If no match exist within the database then simply raise a 404, file not found error!
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

    # Finally, render the currently requested view.
    return render(request, 'blog/post/posts-detail.html', {'post': post})