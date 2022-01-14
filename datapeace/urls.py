from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import datapeaceApp.views
import datapeaceApp.api_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/users/', datapeaceApp.api_views.UserList.as_view()),
    path('api/users/new', datapeaceApp.api_views.UserCreate.as_view()),
    path('api/users/<int:id>/update', datapeaceApp.api_views.UserUpdate.as_view()),

    path('admin/', admin.site.urls),
    path('api/users/<int:id>/', datapeaceApp.views.show, name='show-user'),
 #   path('', store.views.index, name='list-products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
