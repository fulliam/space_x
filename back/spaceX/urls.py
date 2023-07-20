from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^api/', include('editor.urls')),
    re_path(r'^admin/', admin.site.urls),
]
