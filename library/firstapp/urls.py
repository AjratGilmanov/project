from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('login/', Log.as_view(), name='login'),
    path('singup/', Reg.as_view(), name='singup'),
    path('order/', Form.as_view(), name='order')
]