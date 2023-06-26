
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from.views import *

urlpatterns = [
    # path('reg',reglass.as_view(),name='reg'),
    # path('send/',send.as_view(),name='send'),
    # path('otp/',OtpView.as_view(),name='otp')
    path('reg',Register.as_view(),name='register'),
    path('check/',check.as_view(),name='check'),
    path('login/',loginview.as_view(),name='login')
    # path('login',obtain_auth_token,name='login'),
    # path('itemlist/',itemlist.as_view()),
    # path('itemdetail/<int:pk>',itemdetails.as_view()),
    # path('location',locationlist.as_view()),
    # path('locationdetail/<int:pk>',locationdetails.as_view())
]