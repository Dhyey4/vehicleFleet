from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from leasing import views as myapp_views

router = routers.DefaultRouter()
router.register(r'vehicle', myapp_views.VehicleViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
