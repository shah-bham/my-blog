from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='cv_home'),
    path('edit/', views.edit_page, name='cv_edit'),
]