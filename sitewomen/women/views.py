from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Women\'s app</h1>')


def categories(request):
    return HttpResponse('<h2>Categories</h2>')

def category_by_id(request, id):
    return HttpResponse(f"<h3>Category №{id}</h3>")
