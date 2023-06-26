from django.contrib import admin
from django.urls import path, include

from women.views import *
from .routers import CustomRouter

router = CustomRouter()
router.register(r'women', WomenViewSet, basename='women')
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/women/
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
]
