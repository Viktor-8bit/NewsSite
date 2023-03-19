from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from .forms import *



#страницы храняться по адресу NewsSite\Main\site_pages
def registration_page(request):
    if request.method == 'GET':
        return render(request, 'reg.html', { 'reg': RegForm() })
    elif request.method == 'POST':
        return HttpResponse('Вы зарегистрированы')

def index(request):
    return HttpResponse('hello page')