from bussiness_seeker import views
from django.urls import path

app_name = "bussiness_seeker"

urlpatterns = [
    path('register/',views.bussiness_sale_reg,name="bussiness_sale_reg"),

    path('user/activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('profile/',views.bussiness_seeker_profile,name="bussiness_seeker_profile" ),
    path('profile/account_setup/',views.bussiness_seeker_account_setup,name="bussiness_seeker_account_setup"),
    path('profile/invoice/',views.bussiness_seeker_invoice,name="bussiness_seeker_invoice"),
    path('profile/bookandhistory/',views.bussiness_seeker_bookandhistory,name="bussiness_seeker_bookandhistory"),
    path('profile/notification/',views.bussiness_seeker_notification,name="bussiness_seeker_notification" ),
    path('profile/bussiness_seeker_plans/',views.bussiness_seeker_plans,name="bussiness_seeker_plans" ),
    


    path('profile/settings/',views.bussiness_seeker_demo,name="demo" ),

    path('profile/settings/profile_edit/',views.bussiness_seeker_profile_edit,name="bussiness_seeker_profile_edit" ),
    path('profile/settings/password_update/',views.bussiness_seeker_pass_update,name="bussiness_seeker_pass_update" ),
    path('profile/settings/account_details_update/',views.bussiness_seeker_acc_update,name="bussiness_seeker_acc_update" ),
    path('profile/settings/support/',views.bussiness_seeker_support,name="bussiness_seeker_support" ),
]