

from bussiness_invester import views
from django.urls import path
app_name = "bussiness_invester"

urlpatterns = [
    path('register/',views.bussiness_invester_reg,name="bussiness_invester_reg"),
]

