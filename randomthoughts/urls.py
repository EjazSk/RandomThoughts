"""randomthoughts URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rt import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'account/(?P<user__username>[\w.@+-]+)$',views.userView),
    url(r'^rt/(?P<id>\d+)$', views.detailView),
     url(r'^about/$', views.about, name='about'),


  


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
