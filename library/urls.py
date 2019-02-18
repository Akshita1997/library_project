from django.conf.urls import include, url
from . import views

urlpatterns = [
     url('about/',views.about, name = 'Library-about'),
     url('issuebook/',views.issuebook,name='Issue-book'),
    url('', views.home, name = 'library-home'),
    
]