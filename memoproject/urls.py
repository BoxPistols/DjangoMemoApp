from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("memoapp.urls")),
]
# Compare this snippet from memoapp/views.py:
