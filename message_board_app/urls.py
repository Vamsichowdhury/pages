
from django.urls import path,include
from .views import home,blogs

urlpatterns = [
 
    path("home/",home,name='home'),
    path("blogs/",blogs,name='blogs'),
]
