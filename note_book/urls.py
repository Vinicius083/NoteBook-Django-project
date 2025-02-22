from django.contrib import admin
from django.urls import path, include
from user import urls as user_urls
from notes import urls as notes_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include(user_urls)),
    path("notes/", include(notes_urls))
]
