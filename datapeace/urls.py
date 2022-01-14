from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

import datapeaceApp.views
import datapeaceApp.api_views

router = routers.DefaultRouter()
router.register(r'users', datapeaceApp.views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', datapeaceApp.api_views.UserList.as_view()),
    path('api/users/new', datapeaceApp.api_views.UserCreate.as_view()),
    path('api/users/<int:id>/update', datapeaceApp.api_views.UserUpdate.as_view()),
    path('api/users/<int:id>/delete', datapeaceApp.api_views.UserDestroy.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ] 
