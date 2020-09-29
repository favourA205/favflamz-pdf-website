from django.urls import path
from .views import home,download_page,addUser,interjection_page

urlpatterns = [
    path('', home, name='home'),
    path('download/', download_page, name='download page'),
    path('addUser/', addUser, name='addUser'),
    path('download/interject/', interjection_page, name='interjection page'),

]
