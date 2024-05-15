from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden
from django.shortcuts import render

menu = [
    {"title": "Home", "url": "home"},
    {"title": "About", "url": "about"},
    {"title": "Articles", "url": "articles"},
    {"title": "Log in", "url": "login"}
]

data_db = [
    {"id": 1, "title": "Angelina Joly", "content": "Biography", "is_published": True},
    {"id": 2, "title": "Margo Robby", "content": "Biography", "is_published": False},
    {"id": 3, "title": "Julia Roberts", "content": "Biography", "is_published": True},
]

data = {
    "title": "Women",
    "menu": menu,
    "posts": data_db,
}

def index(request):
    return render(request, "women/index.html", context=data)


def about(request):
    return render(request, "women/about.html", context=data)


def woman_by_id(request, id):
    if id == 0:
        raise PermissionDenied()

    for data in data_db:
        if id == data["id"]:
            return render(request, "women/woman_by_id.html", context=data)
    raise Http404()


def articles(request):
    return render(request, "women/articles.html", context=data)


def login(request):
    return render(request, "women/login.html", context=data)


def archive(request, year):
    if year > 2024:
        raise Http404()
    return HttpResponse(f"<h3>Archive of {year} year</h3>")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Page is not found</h1>")


def page_denied(request, exception):
    return HttpResponseForbidden(f"<h1>Request is denied</h1>")
