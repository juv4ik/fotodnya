from django.contrib import admin
from django.urls import path, include
from fotodnya.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
