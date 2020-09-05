
from django.contrib import admin
from django.urls import path, include
from resume import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('resume/', include('resume.urls')),
]
