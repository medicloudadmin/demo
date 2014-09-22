from django.http import HttpResponse


def index(request):
    return HttpResponse(
        '<html><body style="background-color: green">FEST-API finner du <a href="/api/v1/doc/">her!</a></body></html>')
