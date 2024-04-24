from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name="home"),
    path('categories/', views.categories, name="categories"),
    path('categories/<int:id>', views.category_by_id, name="categories_by_id"),
    path('categories/<slug:category_slug>', views.category_by_slug,  name="category_by_slug"),
    path('archive/<year4:year>', views.archive, name="archive"),
    # re_path(r'^archive/(?P<year>[0-9]{4})', views.archive),
]