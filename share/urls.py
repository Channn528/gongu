from django.urls import path
from . import views

urlpatterns = [
     path('home/',views.home, name='home'),
     path('<int:id>/', views.board, name='board'),
     path('like.', views.post_like, name='post_like'),
]