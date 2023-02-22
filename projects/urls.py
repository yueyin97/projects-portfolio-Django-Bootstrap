from django.urls import path
from . import views

urlpatterns = [
    # hook up the root URL of the app to the project_index view
    path("", views.project_index, name="project_index"),
    # want the URL to be /1, or /2, and so on, depending on the pk of the project
    path("<int:pk>", views.project_detail, name="project_detail"),

    path('contact/', views.contact, name='contact'),
]
