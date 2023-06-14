from . import views
from django.urls import path,include


urlpatterns = [
    path('',views.home,name='home'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('signout',views.signout,name='signout'),
    
]

