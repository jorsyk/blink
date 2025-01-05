from django.urls import path
from .views import UserListView

urlpattens = [
    path('', UserListView.as_view(), name='user-list'),
]
