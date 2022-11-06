# Imports from existing modules.
from django.contrib import admin
# Imports from custom modules.
from .models import Post

# Register the Post object on the administration site.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
        This here class allows us to integrate and plugin our post object within Django's
        already prefabricated admin view.

        The class itself extends the admin.ModelAdmin class, and in addition to that it is
        also annotated as something that ought to be registered within the admin view.

        As for the code contain herein, there are mostly options for enhancing the default look
        of the template for our newly added admin entry.

        They will ensure that the user's experience is rich, satisfactory and that it accomplishes
        what the product strives to do.

        Author : Andrei-Paul Ionescu.
    """

    # We want to display the following features/columns of our data model.
    list_display = ('title', 'slug', 'author', 'publish', 'status')

    # We want to be able to easily filter posts based on the criteria defined in below tuple.
    list_filter  = ('status', 'created', 'publish', 'author')

    # We also want to be able to perform searches for the title or for patterns/words found within
    # the body of the post.
    search_fields = ('title', 'body')

    # We want the slug to always be generated automagically with the aid of the current title.
    prepopulated_fields = {'slug': ('title',)}

    raw_id_fields = ('author',)

    # We want to establish a predefined sorted order aka hierarchy.
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
