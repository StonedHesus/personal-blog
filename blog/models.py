from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class PublishedManager(models.Manager):
    """

        :parameter: models.Manager, a django class from which PublishedManager inherits, which contains django's API
        for the Manager object.

        Manage the manner in which objects are being retrieved from the database.
    """

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    """
        :parameter: models.Model; a django class from which our Post class inherits which enables us to utilise django's
        API so as to easy store information within the database.

        This class models a post object, which is an article, containing a text, a published or not status, a date for
        when the article was published, created and last updated, and an author who worked on the article; in addition to that the
        class also has an attribute which stores an unique slug which will be later use so as to generate an unique url
        for each post instance.

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

    #TODO: Learn how to drop the previously existing field so as to be able to move on with the development of the
    # app.
    #first_image = models.ImageField(upload_to='blog/images', default=None)

    publish = models.DateTimeField(default=timezone.now)
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
    status    = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')

    class Meta:
        ordering = ("-publish",)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def __str__(self):
        return self.title