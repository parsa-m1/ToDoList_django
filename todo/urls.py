from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos_list/', views.todos_list, name='todos_list'),

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]

