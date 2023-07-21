from django.urls import path
from FinalProject.common.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home page"),
    path('about/', AboutPageView.as_view(), name="about page"),
    path('gallery/', GalleryView.as_view(), name="gallery page"),
    path('add_post_page/', add_post_view, name="add post page"),
    path('delete_post/<int:pk>/', post_delete, name="delete post"),
    path('like/<int:pk>/', like_functionality, name="like"),
    path('comment/<int:pk>/', comment_functionality, name="comment"),
]
