from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('add_task/', add_task, name='add_task'),
    # path('mark_complete/<int:task_id>/', mark_complete, name='mark_complete'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    ]
