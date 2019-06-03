"""curd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from curdapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home',views.main_page_view),
    url(r'^create',views.create_page_view),
    url(r'^retrieve',views.retrieve_page_view),
    url(r'^update',views.update_page_view),
    url(r'^delete',views.delete_page_view),
]

