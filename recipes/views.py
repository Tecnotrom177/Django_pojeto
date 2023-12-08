from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Tecnotrom',
    })


def sobre(request):
    return HttpResponse('Sobre')
    # return HTTP Response


def contato(request):
    return HttpResponse('Contato')
    # return HTTP Response
