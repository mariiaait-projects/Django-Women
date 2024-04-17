from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    if request.POST:
        print(request.POST)
    return HttpResponse('<h1>Women\'s app</h1>')


def categories(request):
    return HttpResponse('<h2>Categories</h2>')

def category_by_id(request, id):
    return HttpResponse(f"<h3>Category №{id}</h3>")

def category_by_slug(request, category_slug):
    return HttpResponse(f"<h3>Category's slug: {category_slug}</h3>")

def archive(request, year):
    if year > 2024:
        raise Http404()
    return HttpResponse(f"<h3>Archive of {year} year</h3>")

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Page is not found</h1><p>{exception}</p>")