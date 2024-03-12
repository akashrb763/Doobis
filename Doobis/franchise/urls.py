from . import views
from django.urls import path



app_name = "doobiz_franchise"

urlpatterns = [
    path('account_setup/',views.doobiz_franch_acc_setup,name="doobiz_franch_acc_setup" ),


]
