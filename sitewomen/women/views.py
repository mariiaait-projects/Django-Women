from django.core.exceptions import PermissionDenied, BadRequest
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden, HttpResponseRedirect, \
    HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):
    if request.POST:
        print(request.POST)
    return render(request, "women/index.html")
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
