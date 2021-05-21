from django.contrib import admin
from django.urls import path, include
from django.views.generic import CreateView

from fotodnya.views import *
from fotodnya.views import BlogDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage),
    path('about', aboutPage),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    #CreateView.as_view(model=fotoNews, success_url="post/<int:pk>/")
]
