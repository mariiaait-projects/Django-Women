from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index),
    path('categories/', views.categories),
    path('categories/<int:id>', views.category_by_id),
    path('categories/<slug:category_slug>', views.category_by_slug),
    path('archive/<year4:year>', views.archive),
    # re_path(r'^archive/(?P<year>[0-9]{4})', views.archive),
]