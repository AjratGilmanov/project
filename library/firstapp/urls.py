from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('login/', Log.as_view(), name='login'),
    path('singup/', Reg.as_view(), name='signup'),
    path('add_book/', Form_create_book.as_view(), name='add_book'),
    path('logout', Logout_user, name='logout'),
    path('edit/<int:pk>/', Edit.as_view(), name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
    path('form_order/', Form_order.as_view(), name='form_order')
]