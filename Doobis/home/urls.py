from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
   
    path('',views.home,name="home" ),
    path('login/',views.login,name="login" ),
    path('register/',views.register,name="register" ),
    path('profile/',views.profile,name="profile" ),
    path('profile/account_setup/',views.account_setup,name="account_setup"),
    path('profile/invoice/',views.invoice,name="invoice"),
    path('profile/bookandhistory/',views.bookandhistory,name="bookandhistory"),
    path('profile/notification/',views.notification,name="notification" ),
    path('profile/settings/',views.demo,name="demo" ),
    path('profile/settings/profile_edit/',views.profile_edit,name="profile_edit" ),
    path('profile/settings/password_update/',views.pass_update,name="pass_update" ),
    path('profile/settings/account_details_update/',views.acc_update,name="acc_update" ),
    path('profile/settings/support/',views.support,name="support" ),
    
]