from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('role',views.role,name='role'),
    path('edit_role_management',views.edit_role_management,name='edit_role_management'),
    path('edit_role_action',views.edit_role_action,name='edit_role_action'),
    path('user_management',views.user_management,name='user_management'),
    path('user_edit_modal',views.user_edit_modal,name='user_edit_modal'),
    path('user_edit_action',views.user_edit_action,name='user_edit_action'),
    path('delete_role_management',views.delete_role_management,name='delete_role_management'),
    path('delete_user_management',views.delete_user_management,name='delete_user_management')

    




]