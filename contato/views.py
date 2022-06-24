from django.shortcuts import render


def info(request):
    return render (request , 'contato/index.html')
