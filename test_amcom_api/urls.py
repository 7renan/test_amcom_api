
from django.contrib import admin
from django.urls import path, include

# api routers
from .api_routers import api_routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_routers.urls)),
]
