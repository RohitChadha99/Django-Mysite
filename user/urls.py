from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('signup' , views.signup , name='signup'),
    path('logout' , views.logout , name='logout'),
    path('signin' , views.signin , name='signin'),
    path('handlesignup', views.handlesignup ,name="handlesignup"),
    path('handlesignout', views.handlesignout ,name="handlesignout"),
]
