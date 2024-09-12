from django.shortcuts import render


def authorization(request):
    return render(request, 'works/authorization.html')


def home_page(request):
    return render(request, 'works/home_page.html')
