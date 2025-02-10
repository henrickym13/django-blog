from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notice.urls')),
    path('', include('user.urls')),
]
