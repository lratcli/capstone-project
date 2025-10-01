from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.HypotheticalSystemListView.as_view(), name='index'),
    path('<slug:slug>/', views.hypothetical_system_detail_view, 
         name='system_detail'),
]
