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
    path('delete_user_management',views.delete_user_management,name='delete_user_management'),
    path('exam',views.exam,name='exam'),
    path('edit_exam',views.edit_exam,name='edit_exam'),
    path('exam-create',views.exam_create,name='exam-create'),



    # ------------amrith url start--------------------------
    path('exam_save_action',views.exam_save_action,name='exam_save_action'),
    path('open_section_based_question',views.open_section_based_question,name='open_section_based_question'),
    path('validation_check',views.validation_check,name='validation_check'),


     # ------------amrith url end--------------------------

    # ---------------anirudh url------------------------
    path('section_title_edit',views.section_title_edit,name='section_title_edit'),
    path('update_exam_details',views.update_exam_details,name='update_exam_details'),
    path('delete_initial_field',views.delete_initial_field,name='delete_initial_field'),
    path('section_Question_view_modal',views.section_Question_view_modal,name='section_Question_view_modal'),
    path('Question_Management_update',views.Question_Management_update,name='Question_Management_update'),

    
    path('New_section_add',views.New_section_add,name='New_section_add'),
    path('open_section_based_question_edit',views.open_section_based_question_edit,name='open_section_based_question_edit'),
    path('delete_question_section',views.delete_question_section,name='delete_question_section'),
    path('delete_question_modal',views.delete_question_modal,name='delete_question_modal'),
    path('save_section_question_action',views.save_section_question_action,name='save_section_question_action'),





    # ------------------jiyad url---------------
    path('exam_login_new',views.exam_login_new,name='exam_login_new'),
    path('customer_using_link_new',views.customer_using_link_new,name='customer_using_link_new'),
    path('attend_exam_new/<str:slug>',views.attend_exam_new,name='attend_exam_new'),
    path('exam_login_action_new',views.exam_login_action_new,name='exam_login_action_new'),
    path('exam_link_action_new',views.exam_link_action_new,name='exam_link_action_new'),
    path('wizard_new',views.wizard_new,name='wizard_new'),
    path('exam_result_new',views.exam_result_new,name='exam_result_new'),

    


    




]