from django.contrib import admin
from django.urls import path
from fotodnya.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage),
]
