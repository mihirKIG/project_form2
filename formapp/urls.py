from django.urls import path

from .  import views


urlpatterns = [
   
    path('contact/',views.contact, name='contact'),
    
    path('register/',views.register_form, name='register'),
]
