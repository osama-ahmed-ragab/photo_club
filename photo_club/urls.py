from django.urls import path
from . import views
from .views import UpdateView


urlpatterns = [
    path('', views.photo_list,name='photo_list'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit'),
    #path('photo/<int:pk>/edit/', views.UpdateView.as_view(), name='add_post')
]