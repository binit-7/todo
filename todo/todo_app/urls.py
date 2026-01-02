from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('add_task/', add_task, name='add_task'),
    path('mark_complete/<int:id>/', mark_complete, name='mark_complete'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('mark_undone/<int:id>/', mark_undone, name='mark_undone'),
    path('edit_task/<int:id>/', edit_task, name='edit_task'),   
    ]
