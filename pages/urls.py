from django.urls import path
from .views import homeViewPage

urlpatterns = [path('', homeViewPage, name='home')]