# Imports from existing modules.
from django.urls import path
# Imports from custom modules.
from . import views
from apps import BlogConfig

# Retrieve the app's name from within the BlogConfig with the aid of the class-instance getter method
# for that value.
app_name= BlogConfig.get_name()

# Define a list of path objects which indicate all the possible relative paths that we have
# defined for the project.
urlpatterns=[
    path('', views.render_posts, name='posts'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.render_post, name='post_detail')
]
