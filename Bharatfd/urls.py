from django.contrib import admin
from django.urls import path, include  # Ensure 'include' is imported
from django.http import HttpResponse

# Simple view for the root URL
def home(request):
    return HttpResponse("Welcome to the FAQ Application!")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin path
    path('api/', include('faq.urls')),  # API path
    path('', home),  # Home page path
]
