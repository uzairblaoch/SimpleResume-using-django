from django.urls import path
from . import views


# SET THE NAMESPACE!
app_name = 'resume'


urlpatterns = [
    path("services/", views.services, name="services"),
    path("skills/", views.skills, name="skills"),
    path("contact/", views.contact, name="contact")
]
