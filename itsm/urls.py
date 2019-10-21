from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'catalogo/', include('catalogo.urls')),
    path('', RedirectView.as_view(url='/catalogo/', permanent=True) )
]
