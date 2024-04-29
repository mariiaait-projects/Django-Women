from django.core.exceptions import PermissionDenied, BadRequest
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden, HttpResponseRedirect, \
    HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = ["About site", "Add article", "Feedback", "Login"]

data_db = [
    {"id": 1, "title": "Angelina Joly", "content": "Biography", "is_published": True},
    {"id": 2, "title": "Margo Robby", "content": "Biography", "is_published": False},
    {"id": 3, "title": "Julia Roberts", "content": "Biography", "is_published": True},
]


class MyClass:
    def __init__(self, num1, num2):
        self.num1, self.num2 = num1, num2


def index(request):
    data = {
        "title": "Main page",
        "menu": menu,
        "posts": data_db,
    }

    # if request.POST:
    #     print(request.POST)

    # data = {
    #     "title": "Main page",
    #     "main_title": "",
    #     "menu": menu,
    #     "float": 28,
    #     "lst": [1, 2, "abc", True],
    #     "set": {1, 2, 3, 2, 5},
    #     "dict": {"key_1": "value_1", "key_2": "value_2"},
    #     "obj": MyClass(10, 20),
    #     "url": slugify("The Main Page")
    # }
    return render(request, "women/index.html", context=data)
    # content = render_to_string("women/index.html")
    # return HttpResponse(content)


def about(request):
    return render(request, "women/about.html")


def categories(request):
    return HttpResponse('<h2>Categories</h2>')


def category_by_id(request, id):
    if id == 1:
        return redirect("archive", 2018)

    if id == 0:
        raise PermissionDenied()
    return HttpResponse(f"<h3>Category №{id}</h3>")


def category_by_slug(request, category_slug):
    if category_slug == 'sport':
        return redirect("archive", 2018, permanent=True)

    # if category_slug == 'music':
    #     url = reverse("archive", args=(2024,))
    #     return HttpResponseRedirect(url)
    # return HttpResponsePermanentRedirect(url)

    return HttpResponse(f"<h3>Category's slug: {category_slug}</h3>")


def archive(request, year):
    if year > 2024:
        raise Http404()
    return HttpResponse(f"<h3>Archive of {year} year</h3>")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Page is not found</h1>")


def page_denied(request, exception):
    return HttpResponseForbidden(f"<h1>Request is denied</h1>")
