from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mylist/', views.mylist, name='mylist'),
     path('mark_as_completed/<int:item_id>/', views.mark_as_completed, name='mark_as_completed'),
     path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
]
