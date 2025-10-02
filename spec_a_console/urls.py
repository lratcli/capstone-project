from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.ConsoleSystemListView.as_view(), name='index'),
    path('<slug:slug>/', views.console_system_detailed_view,
         name='system_detail'),
]
