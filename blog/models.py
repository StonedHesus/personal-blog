# Imports from existing modules.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    """
        This here class is responsible for providing the required functionalities for retrieving
        all the published articles, and for managing those values.

        The class itself extends Django's models.Manager.

        Author: Andrei-Paul Ionescu.
    """

    def get_queryset(self):
        """
            This here routine is a more sophisticated getter.
            For despite looking like a simple getter routine, it actually is a wrapper for
            a query search, in which a predefined predicate is being passed that of published; hence
            this here routine is responsible for returning all the published posts.
        """
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    """

        This class models a post object, which  contains a text, a published or not status,
        a date for when the article was published, created and last updated, and an author who worked on the article;
        in addition to that the class also has an attribute which stores a unique slug which will be later
        used so as to generate a unique url for each post instance.

        The class itself extends Django's models.Model class.

        Author: Andrei-Paul Ionescu.
    """

    objects = models.Manager() # The default object manager.
    published = PublishedManager() # The custom object manager.

    # An article which is stored in the database could either be a draft of a published one.
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title  = models.CharField(max_length=250)
    slug   = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body   = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
    status    = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')

    class Meta:
        ordering = ("-publish",)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def __str__(self):
        """
            Return a textual representation of the data.
        """
        return self.title