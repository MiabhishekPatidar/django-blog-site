from django.contrib import admin  # Import admin here
from django.urls import path, include
from django.http import HttpResponse

# Simple homepage view
def homepage(request):
    return HttpResponse("Welcome to the Blog Homepage!")

urlpatterns = [
    path('', homepage),  # <-- This adds the homepage route
    path('admin/', admin.site.urls),  # <-- Make sure admin is properly included
    path('blog/', include('blog.urls')),
]
