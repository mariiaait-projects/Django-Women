from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('categories/', views.categories),
    path('categories/<int:id>', views.category_by_id),
]