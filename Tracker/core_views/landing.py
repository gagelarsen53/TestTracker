from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def landing(request):
    context = {}
    return render(request, 'general/landing.html', context)
