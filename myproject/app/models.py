from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class common_table(models.Model):
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_ownership",on_delete=models.CASCADE,null=True)
    created_dt = models.DateField(auto_now=True)
    updated_by =  models.ForeignKey(User, related_name="%(app_label)s_%(class)s_ownership1",on_delete=models.CASCADE,null=True)
    updated_dt = models.DateField(null=True)
    created_tm = models.TimeField(auto_now=True)
    updated_tm = models.TimeField(null=True)
    status = models.CharField(max_length=10, null=True)

    class Meta:
        abstract = True



layout_choice = (
    ("0","One page with all the questions"),
    ("1","One page per section"),
    ("2","One page per question")
)

progression_choices =(
    ("Percentage","Percentage"),
    ("Number","Number")
)

selection_choices =(
    ("All questions","All questions"),
    ("Randomized per section","Randomized per section")
)

scoring_choices =(
    ("0","No scoring"),
    ("1","Scoring with answers at the end"),
    ("2","Scoring without answers at the end")
)

access_choices =(
    ("0","Anyone with the link"),
    ("1","Invited people only"),
   
)

section_choices =(
    ("Section","Section"),
    ("Question","Question"),
   
)

from django.utils.text import slugify
class Main_Exam_Master(common_table):
    Exam_title = models.CharField(max_length=50,null=True)
    responsible_person = models.ForeignKey(User,related_name='Main_Exam_Master_auth_id',on_delete=models.CASCADE,null=True)
    background_image = models.FileField(upload_to='exam_background',null=True)
    start_message = models.TextField()
    end_message = models.TextField()
    layout = models.CharField(max_length=25,choices=layout_choice,null=True)
    progression_mode = models.CharField(max_length=25,choices=progression_choices,null=True)
    Exam_time_limit = models.TimeField(null=True)
    selection_mode = models.CharField(max_length=25,choices=selection_choices,null=True)
    scoring_mode = models.CharField(max_length=25,choices=scoring_choices,null=True)
    access_mode = models.CharField(max_length=25,choices=access_choices,null=True)
    Login_required = models.BooleanField(null=True)
    attempt_limit = models.IntegerField(null=True)
    Success_per = models.IntegerField(null=True)
    slug = models.SlugField(max_length=50, unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.Exam_title)
        super(Main_Exam_Master, self).save(*args, **kwargs)

import string
import random
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(1))

question_type_choices =(
    ("Radio","Multiple choice: only one answer"),
    ("Checkbox","Multiple choice: multiple answers allowed"),
   
)


class Main_Question_Bank(common_table):
    Question = models.TextField()
    Imagefield = models.FileField(upload_to='Question_Bank_image',null=True)
    Question_type = models.CharField(max_length=20,choices=question_type_choices,null=True)
    Description =  models.TextField(null=True)
    manadatory = models.BooleanField(default=False)
    comments = models.CharField(max_length=25,null=True)
    total_mark = models.IntegerField(null=True)
    answer_id =  models.ManyToManyField('Question_Bank_multiple_choice', blank=True,related_name="Answer_master_id")
    question_ar = models.TextField(null=True)
    question_en = models.TextField(null=True)
    question_hi  = models.TextField(null=True) 
    question_ur  = models.TextField(null=True) 
    question_ta  = models.TextField(null=True)   
    


class Main_Exam_section(common_table):
    Exam_id = models.ForeignKey(Main_Exam_Master,related_name ="Main_Exam_section_exam_id",on_delete=models.CASCADE,null=True)
    section_title = models.CharField(max_length=50,null=True)
    section_type = models.CharField(max_length=20,choices=section_choices,null=True)
    Question_bank_id = models.ForeignKey(Main_Question_Bank,related_name='Main_Exam_Master_question_id',on_delete=models.CASCADE,null=True)



language_type =(
    ("en","English"),
    ("ar","Arabic "),
    ("ur","Urdu"),
    ("ta","Tamil"),
    ("hi","Hindi")
)

class Main_exam_language(common_table):
    Exam_id = models.ForeignKey(Main_Exam_Master,related_name ="Main_exam_language_eaxm_id",on_delete=models.CASCADE,null=True)
    language_access = models.CharField(choices=language_type,max_length=25)
    

class Question_Bank_multiple_choice(common_table):
    Question_id = models.ForeignKey(Main_Question_Bank,related_name ="Exam_section_exam_id",on_delete=models.CASCADE,null=True)
    choice = models.CharField(max_length=50,null=True)
    Imagefield = models.FileField(upload_to='Question_Bank_multiple',null=True)
    file_type = models.CharField(max_length=20,null=True)
    Mark = models.IntegerField(null=True)
    result_status = models.BooleanField(default=False)
    choice_ar = models.TextField(null=True)
    choice_en = models.TextField(null=True)
    choice_hi  = models.TextField(null=True) 
    choice_ur  = models.TextField(null=True) 
    choice_ta  = models.TextField(null=True)   

class Section_Question_Mapping(common_table):
    Section_id = models.ForeignKey(Main_Exam_section,related_name ="Section_Question_Mapping_id",on_delete=models.CASCADE,null=True)
    Question_id = models.ForeignKey(Main_Question_Bank,related_name ="Question_Bank_id",on_delete=models.CASCADE,null=True)


Exam_start_field=(
    ("selection","selection"),
    ("Text Input","Text Input"),
   
)


class Exam_inital_field(common_table):
    Exam_id = models.ForeignKey(Main_Exam_Master,related_name ="Exam_inital_field_exam_id",on_delete=models.CASCADE,null=True)
    title = models.TextField()
    field_type = models.CharField(max_length=20,choices=Exam_start_field,null=True)

class Exam_inital_field_choice(common_table):
    initial_field_id = models.ForeignKey(Exam_inital_field,related_name ="Exam_inital_field_id",on_delete=models.CASCADE,null=True)
    choice_name = models.CharField(max_length=25,null=True)







Exam_attend_user_type=(
    ("login_user","login_user"),
    ("non_login_user","non_login_user"),
   
)


class Exam_attend_user(models.Model):
    exam_id  = models.ForeignKey(Main_Exam_Master, related_name="Exam_attend_user_exam_id", on_delete=models.CASCADE,null=True)
    user_type = models.CharField(choices=Exam_attend_user_type,null=True,max_length=25)
    auth_user = models.ForeignKey(User, related_name="Exam_attend_user_auth_id", on_delete=models.CASCADE,
                                   null=True)
    created_dt = models.DateField(auto_now_add=True)
    created_tm = models.TimeField(auto_now_add=True)
    attend_status = models.BooleanField(default=False)



class exam_attend_user_initial_field(models.Model):
    exam_attend_user_id  = models.ForeignKey(Exam_attend_user, related_name="exam_attend_user_initial_field_attend_id", on_delete=models.CASCADE,null=True)
    Exam_inital_field_id = models.ForeignKey(Exam_inital_field, related_name="exam_attend_user_initial_field_id_Exam_inital_field", on_delete=models.CASCADE,null=True)
    answer = models.CharField(max_length=25,null=True)



class exam_attend_user_score(models.Model):
    exam_attend_user_id  = models.ForeignKey(Exam_attend_user, related_name="exam_attend_user_score_user_id", on_delete=models.CASCADE,null=True)
    section_question_id  = models.ForeignKey(Section_Question_Mapping, related_name="exam_attend_user_score_question_id", on_delete=models.CASCADE,null=True)
    Mark = models.IntegerField(null=True)
    result_status = models.BooleanField(default=False)
    Question_id = models.ForeignKey(Main_Question_Bank, related_name="exam_attend_user_score_Question_Bank_id", on_delete=models.CASCADE,null=True)
    correct_answer = models.ManyToManyField(Question_Bank_multiple_choice,related_name="exam_attend_user_score_Question_Bank_id")
    user_select_choice =   models.ManyToManyField(Question_Bank_multiple_choice,related_name="exam_attend_user_score_Question_Bank_id_select_id")







class customer_answers(models.Model):
    auth_user = models.ForeignKey(User, related_name="customer_details", on_delete=models.CASCADE,
                                   null=True)
    Exam_id = models.ForeignKey(Main_Exam_Master, related_name="customer_answers_exam_id", on_delete=models.CASCADE,null=True)
    Question_id = models.ForeignKey(Main_Question_Bank, related_name="customer_answers_Question_Bank_id", on_delete=models.CASCADE,null=True)
    answer = models.CharField(max_length=50, null=True)
    Mark = models.IntegerField(null=True)




class Role_master(common_table):
    auth_user = models.ForeignKey(User,related_name="role_auth_id",on_delete=models.CASCADE,null=True)
    role_name = models.CharField(max_length=50,null=True)
    description = models.TextField(null=True)


navbar_name = (
   
    ("User","User"),
    ("Role","Role"),
    ("Exam","Exam"),
    
)

class Role_mapping(common_table):
    role_master_id = models.ForeignKey(Role_master,related_name="Role_master_role_id",on_delete=models.CASCADE,null=True)
    navbar_name = models.CharField(max_length=50,choices=navbar_name,null=True)
    read = models.BooleanField(null=True)
    write = models.BooleanField(null=True)
    edit = models.BooleanField(null=True)
    delete = models.BooleanField(null=True)
    view_all = models.BooleanField(null=True)
    manage_all = models.BooleanField(null=True)


user_level = (
    ("Manager","Manager"),
    ("Normal Staff","Normal Staff")
)
password_generate_option = (
    ("Automatic","Automatic"),
    ("Manual","Manual"),
)
class User_details(common_table):
    auth_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_details_authuser", null=True)
    name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50,null=True)
    password_option =  models.CharField(max_length=50,choices=password_generate_option,null=True)
    user_level = models.CharField(max_length=25,choices=user_level,null=True)
    photo = models.FileField(upload_to="user_image", null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    manager_auth = models.ForeignKey(User,on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s_owner1",null=True)


class user_permission_mapping(common_table):
    auth_user_id = models.ForeignKey(User,related_name="user_permision_auth",on_delete=models.CASCADE,null=True)
    user_id = models.ForeignKey(User_details,related_name="user_permision_userid",on_delete=models.CASCADE,null=True)
    role_mapping_id = models.ForeignKey(Role_master,related_name="user_permission_role_id",on_delete=models.CASCADE,null=True)
    start_dt = models.DateField(null=True)
    end_dt = models.DateField(null=True)
    description = models.TextField(null=True)


class Exam_general_instruction(models.Model):
    exam_id  = models.ForeignKey(Main_Exam_Master, related_name="Exam_general_instruction_exam_id", on_delete=models.CASCADE,null=True)
    instruction = models.CharField(max_length=50,null=True)