from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render



def index(request):
    return HttpResponse('hello page')