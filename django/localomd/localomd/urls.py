"""localomd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from localomd.admin import admin_omd

urlpatterns = [
    url(r'^admin_omd/', admin_omd.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('localomddata.urls', namespace='data')),
    url(r'^web/', include('localomdweb.urls')),
    url(r'^api/data/', include("localomddata.api.urls", namespace='data-api')),
]
