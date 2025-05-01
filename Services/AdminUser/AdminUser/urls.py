"""
URL configuration for AdminUser project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
#from API.views import CreateUserView
from django.http import HttpResponse
from API.views import TestRateLimitView

def home_view(request):
    return HttpResponse("Página de inicio")

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('usuarios/', CreateUserView.as_view(), name='crear_usuario'),
    path('test-rate-limit/', TestRateLimitView.as_view(), name='test_rate_limit'),
    path('', home_view),
]
