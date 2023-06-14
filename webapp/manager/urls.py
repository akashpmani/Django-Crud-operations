from . import views
from django.urls import path,include


urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('delete/<int:id>',views.delete_user,name='delete_user'),
    path('<int:id>/',views.update_user,name='update_user'),
    path('adminlogin',views.custom_login,name='adminlogin'),
    path('adminsignout',views.admin_logout,name='adminsignout')
    
    
]

