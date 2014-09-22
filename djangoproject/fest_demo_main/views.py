from django.http import HttpResponse


def index(request):
    return HttpResponse(
        '<html><body style="bgcolor: yellow">FEST-API finner du <a href="/api/v1/doc/">her!</a></body></html>')