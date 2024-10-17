from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),

    # Добавляем имя маршруту
    path('register_record/', views.register_record, name='register_record'),
    path('show_all_records/', views.show_all_records, name='show_all_records'),
    path('show_user_records/', views.show_user_records, name='show_user_records'),
]
