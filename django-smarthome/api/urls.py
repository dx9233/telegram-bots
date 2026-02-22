from django.urls import path
from django.http import JsonResponse

def hello_api(request):
    return JsonResponse({"message": "API working!"})

urlpatterns = [
    path('', hello_api),
]
