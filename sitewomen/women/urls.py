from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('articles/', views.articles, name="articles"),
    path('login/', views.login, name="login"),
    path('woman/<int:id>', views.woman_by_id, name="woman_by_id"),
    path('archive/<year4:year>', views.archive, name="archive"),
]