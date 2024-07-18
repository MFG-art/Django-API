from django.urls import path
from . import views

urlpatterns = [
    # path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blogpost/", views.BlogPostViewSet.as_view({'get': 'list'}), name="blogpost-view-create"),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update" )
]