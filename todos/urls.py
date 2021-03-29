from django.urls import path
from . import views
urlpatterns=[
    path('list/',views.list_todo_item),
    path('insert_todo/',views.insert_todo_item, name='insert_todo_item'),
    path('delete_todo/<int:todo_id>',views.delete_todo_item, name='delete_todo_item'),
    path('login/',views.login_user,name='login'),
    path('register/',views.register_user,name='register_user'),



]