from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.PostListCreateView.as_view(), name='list-create'),
    path('<int:post_id>/like/', views.LikePostView.as_view(), name='like'),
]
