"""Davidgram views"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse('Hello World, current server time is {now}'.format(
        now=str(now))
    )