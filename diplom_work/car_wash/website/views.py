from django.shortcuts import render
from .models import Block


def home(request):
    bl = Block.objects.all()
    context = {'bl': bl}
    return render(request, "website/home.html", context)
