from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('account_landing/', views.account_landing, name='account_landing'),
    path('view_new_name/', views.view_new_name, name='view_new_name')
]
