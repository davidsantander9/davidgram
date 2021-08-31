"""Post views"""

# Django
from django.http import HttpResponse

# Create your views here.
def list_posts(request):
    """List existign posts"""
    posts = [ 1, 2, 6]
    return HttpResponse(str(posts))

