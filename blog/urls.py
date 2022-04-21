from django.urls import path
from . import views

app_name='blog'

urlpatterns=[

    path('', views.posts, name='posts'), #The main URL of the app will showcase all the posts which exist within the db.
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post, name='post_detail')

]