
from django.urls import path

from davidgram import views 



urlpatterns = [
    path('hello-world/', views.hello_world),
]
