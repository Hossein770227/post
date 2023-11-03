from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SigupView.as_view(), name= 'signup')

]
