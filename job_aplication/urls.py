from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.aboutPage, name='about'),
    path('accounts/', include('accounts.urls')),
];