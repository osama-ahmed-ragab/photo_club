from django.urls import path
from . import views
from .views import UpdateView


urlpatterns = [
    path('', views.photo_list,name='photo_list'),
    path('photo/new/', views.photo_new, name='photo_new'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit'),
    #path('photo/<int:pk>/edit/', views.UpdateView.as_view(), name='add_post')
    path('photo/<int:pk>/comment/', views.add_comment_to_photo, name='add_comment_to_photo'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]