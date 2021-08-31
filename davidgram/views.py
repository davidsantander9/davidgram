"""Davidgram views"""

# Django
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse('Hello World, current server time is {now}'.format(
        now=str(now))
    )

def sorted_numbers(request):
    """Return a JSON response with sorted numbers"""
    numbers = request.GET['numbers'].split(",")
    numbers.sort()
    return JsonResponse({'status':'ok','numbers':numbers})

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are no allowed here'.format(name)
    else:
        message = 'Hi, {}! Welcome to Davidgram'.format(name)
    return HttpResponse(message)