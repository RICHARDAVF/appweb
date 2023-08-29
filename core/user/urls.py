from django.urls import path
from core.user.views import *
app_name = 'user'

urlpatterns = [
    # user
    path('list/', ListViewUser.as_view(), name='user_list'),
    path('add/', CreateViewUser.as_view(), name='user_create'),
    path('update/<int:pk>/', UpdateViewUser.as_view(), name='user_update'),
    path('delete/<int:pk>/', DeleteViewUser.as_view(), name='user_delete'),
    path('change/group/<int:pk>/', UserChangeGroup.as_view(), name='user_change_group'),
]