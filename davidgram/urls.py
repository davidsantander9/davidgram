
from django.urls import path

from davidgram import views 



urlpatterns = [
    path('hello-world/', views.hello_world),
    path('sorted_numbers/', views.sorted_numbers),
    path('hi/<str:name>/<int:age>/', views.say_hi)
]
