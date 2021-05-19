from django.urls import path
from django.urls.conf import include
from .views import SignupPageView

urlpatterns = [ 
    path('signup/', SignupPageView.as_view(), name='signup')    
 ]