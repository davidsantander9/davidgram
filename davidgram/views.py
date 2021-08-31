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

def hi(request):
    """Hi."""
    numbers_str = request.GET.get('numbers').split(",")
    numbers = list(map(int, numbers_str))
    numbers.sort()
    print( numbers )
    return JsonResponse({'numbers':numbers})
    # return HttpResponse(str(numbers))