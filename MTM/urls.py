from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('classes/', ClassesPageView.as_view(), name='classes'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('ariza/', ArizaView, name='ariza'),


    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)