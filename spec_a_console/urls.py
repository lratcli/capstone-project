from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.ConsoleSystemListView.as_view(), name='index'),
    path('create/', views.create_console_system_view, name='create_system'),
    path('my_systems/', views.my_console_systems_view, name='my_systems'),
    path('<slug:slug>/delete/', views.delete_console_system_view,
         name='delete_system'),
    path('<slug:slug>/', views.console_system_detailed_view,
         name='system_detail'),
]
