# superuser :username-kshounish
#password 12345
from django.contrib import admin
from django.urls import path,include
#from django.contrib.auth import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/',LogoutView.as_view(),name='logout',kwargs={'next_page':'/'}),#whenevr after jogout go to home page
]
