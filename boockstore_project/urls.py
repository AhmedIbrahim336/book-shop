
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # Django admin 
    path('admin/', admin.site.urls),

    # User managment  
    path('accounts/', include('django.contrib.auth.urls')),

    # Local apps 
    path('',include('pages.urls'))
]
