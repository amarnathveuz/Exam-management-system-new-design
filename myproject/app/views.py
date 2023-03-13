from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages

from .models import *
# Create your views here.



def dashboard(request):
    total_exam_count = Main_Exam_Master.objects.all().count()
    total_closed_exam = Main_Exam_Master.objects.filter(status="closed").count()
    total_pending_exam = Main_Exam_Master.objects.filter(status="pending").count()
    total_user = User_details.objects.all().count()
    total_role = Role_master.objects.all().count()
    user_data = User_details.objects.filter(status=True)
    current_exam = Main_Exam_Master.objects.all()

    context = {
        'total_exam_count':total_exam_count,
        'total_closed_exam':total_closed_exam,
        'total_pending_exam':total_pending_exam,
        'total_user':total_user,
        'total_role':total_role,
        'user_data':user_data,
        'current_exam':current_exam
    }

    return render(request,'dashboard.html',context)



def index(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, str("Incorrect username or password"))
            return redirect(request.META['HTTP_REFERER'])
    return render(request,'index.html')


def role(request):
    if request.method == "POST":
        role_name = request.POST.get("role_name")
        role_description = request.POST.get("role_description")
        data_save_role = Role_master.objects.create(
                role_name = role_name,
                description = role_description,
                status = "True",
                auth_user_id = request.user.id,
                created_by = request.user,
            )
        Role_mapping.objects.create(
                role_master_id_id = data_save_role.id,
                navbar_name = "User",
                read = request.POST.get('user_read',False),
                write = request.POST.get('user_write',False),
                edit = request.POST.get('user_edit',False),
                delete = request.POST.get('user_delete',False),
                view_all = request.POST.get('user_view_all',False),
                manage_all = request.POST.get('user_manage_all',False),
                created_by = request.user,
                status = "True"
            )

        Role_mapping.objects.create(
                role_master_id_id = data_save_role.id,
                navbar_name = "Role",
                read = request.POST.get('role_read',False),
                write = request.POST.get('role_write',False),
                edit = request.POST.get('role_edit',False),
                delete = request.POST.get('role_delete',False),
                view_all = request.POST.get('role_view_all',False),
                manage_all = request.POST.get('role_manage_all',False),
                created_by = request.user,
                status = "True"
            )

        Role_mapping.objects.create(
                role_master_id_id = data_save_role.id,
                navbar_name = "Exam",
                read = request.POST.get('exam_read',False),
                write = request.POST.get('exam_write',False),
                edit = request.POST.get('exam_edit',False),
                delete = request.POST.get('exam_delete',False),
                view_all = request.POST.get('exam_view_all',False),
                manage_all = request.POST.get('exam_manage_all',False),
                created_by = request.user,
                status = "True"
            )
        messages.success(request,"Successfully added Role")
        return redirect('role')

    data = Role_master.objects.filter(status=True)
    context = {
        'data':data
    }
    return render(request,'role.html',context)



def edit_role_management(request):
    id = request.GET.get("id")
    role_data = Role_master.objects.get(id=id)
    role_User = Role_mapping.objects.get(role_master_id_id=role_data.id, navbar_name="User")
    role_Role = Role_mapping.objects.get(role_master_id_id=role_data.id, navbar_name="Role")
    role_Exam = Role_mapping.objects.get(role_master_id_id=role_data.id, navbar_name="Exam")
   
    context = {
        'role_data':role_data,
        'role_User': role_User,
        'role_Role': role_Role,
        'role_Exam': role_Exam,
        
    }
    return render(request, "edit_role_management.html", context)

def edit_role_action(request):
    if request.method == "POST":
        role_data = request.POST.get('role_data')
        role_user = request.POST.get('role_user')
        role_role = request.POST.get('role_role')
        role_exam = request.POST.get('role_exam')
        

        

       
        data_save_role = Role_master.objects.filter(id=role_data).update(
                role_name = request.POST.get('name'),
                    description = request.POST.get('description'),
            )

        Role_mapping.objects.filter(id=role_role).update(
                    navbar_name = "Role",
                    read = request.POST.get('role_read',False),
                    write = request.POST.get('role_write',False),
                    edit = request.POST.get('role_edit',False),
                    delete = request.POST.get('role_delete',False),
                    view_all = request.POST.get('role_view_all',False),
                    manage_all = request.POST.get('role_manage_all',False),
            )

        Role_mapping.objects.filter(id=role_user).update(
                    navbar_name = "User",
                    read = request.POST.get('user_read',False),
                    write = request.POST.get('user_write',False),
                    edit = request.POST.get('user_edit',False),
                    delete = request.POST.get('user_delete',False),
                    view_all = request.POST.get('user_view_all',False),
                    manage_all = request.POST.get('user_manage_all',False),
                )


        Role_mapping.objects.filter(id=role_exam).update(
                    navbar_name = "Exam",
                    read = request.POST.get('exam_read',False),
                    write = request.POST.get('exam_write',False),
                    edit = request.POST.get('exam_edit',False),
                    delete = request.POST.get('exam_delete',False),
                    view_all = request.POST.get('exam_view_all',False),
                    manage_all = request.POST.get('exam_manage_all',False),
                )

            
        messages.success(request,"Successfully updated Role")
        return redirect('role')
    
from PIL import Image
def user_management(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        photo =  request.FILES['photo']
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        fixed_height = 128
        image = Image.open(photo)
        width_size = int(fixed_height/image.height * image.width)
        resized_image = image.resize((width_size,fixed_height))
        from django.conf import settings
        resized_image.save("media/user_image/"+photo.name)
        image_new1 = 'user_image/'+photo.name
        password_option = request.POST.get("password_option")
        user_level = request.POST.get("user_level")
        if password_option == "Automatic":
            import string    
            import random
            S = 10
            password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
        else:
            password = request.POST.get("password_field",False)
        if User.objects.filter(username=username).exists():
            messages.warning(request,"Username already exists")
            return redirect(request.META['HTTP_REFERER'])
        else:
            user = User.objects.create_user(username, password = password)
            user.save()
            if user_level == "Normal Staff":
                manager_id = request.POST.get("manager_id")
                user_data = User_details.objects.create(
                   
                    auth_user = user,
                    photo = image_new1,
                    name = name,
                    username = username,
                    password_option = password_option,
                    email = email,
                    phone = phone,
                    user_level = user_level,
                    created_by = request.user,
                    status = "True",
                    manager_auth_id = manager_id 
                    )
            else:
                manager_id = request.POST.get("manager_id",False)
                print("manager_id:::::::::",str(manager_id))
                if manager_id == False:
                    manager_id = request.user.id 

                
                user_data = User_details.objects.create(
                   
                    auth_user = user,
                    photo = image_new1,
                    name = name,
                    username = username,
                    password_option = password_option,
                    email = email,
                    phone = phone,
                    user_level = user_level,
                    created_by = request.user,
                    status = "True",
                    manager_auth_id =manager_id
                    )
            role_id = request.POST.getlist("role_id[]")
            
            role_description = request.POST.getlist("role_description[]")
            role_start_dt = request.POST.getlist("role_start_dt[]")
            role_end_dt = request.POST.getlist("role_end_dt[]")
            role_length = len(role_id)
            for i in range(0,role_length):
                    role_end_dt1 = role_end_dt[i]
                    if role_end_dt1 == "":
                        role_end_dt1 = None
                    data_save_user_role = user_permission_mapping(
                        auth_user_id = user,
                        user_id_id = user_data.id,
                        role_mapping_id_id = int(role_id[i]),
                        start_dt = role_start_dt[i],
                        end_dt = role_end_dt1,
                        description = role_description[i]
                    )
                    data_save_user_role.save()
            messages.success(request,"Successfully added new member")
            return redirect('user_management')
    from datetime import datetime
    today_date = datetime.today().strftime('%Y-%m-%d')
    role_data = Role_master.objects.filter(status=True)
    manager_data = User_details.objects.filter(user_level = "Manager" ,status=True)
    user_data = User_details.objects.filter(status=True)
    context = {
        'role_data':role_data,
        'today_date':today_date,
        'manager_data':manager_data,
        'user_data':user_data
    }
    return render(request,'User.html',context)


def user_edit_modal(request):
    id = request.GET.get("id")
    user_data = User_details.objects.get(id=id)
    roles = user_permission_mapping.objects.filter(user_id=user_data)
    manager_data = ""
    role_data = ""
    role_data = Role_master.objects.all()
    manager_data = User_details.objects.filter(user_level="Manager")
    context = {
        'user_data':user_data,
        'manager_data':manager_data,
        'role_data':role_data,
        'roles':roles,
    }
    return render(request,"user_edit_modal.html",context)

from rest_framework.decorators import api_view
@api_view(['POST'])
def user_edit_action(request):
    if request.method == "POST":

        data = request.data
        role_id = request.POST.getlist("role_id[]")
        role_description = request.POST.getlist("role_description[]")
        role_start_dt = request.POST.getlist("role_start_dt[]")
        role_end_dt = request.POST.getlist("role_end_dt[]")
        role_permission_name = request.POST.getlist("role_permission_name")
        role_length = len(role_id)

        role_id_new = request.POST.getlist("role_id_new[]")
        role_description_new = request.POST.getlist("role_description_new[]")
        role_start_dt_new = request.POST.getlist("role_start_dt_new[]")
        role_end_dt_new = request.POST.getlist("role_end_dt_new[]")
        role_length_new = len(role_id_new)

        role_delete = request.POST.get("role_delete")
        aaaa = [int(x.strip()) for x in role_delete.split(',') if x]
        data_delete = user_permission_mapping.objects.filter(id__in=aaaa)
        data_delete.delete()

        try:
            photo = request.FILES['photo']
        except:
            photo = ""
        user_data = User_details.objects.get(id=data['member_id'])
        user_update = User.objects.get(username=data['username_old'])
        user_update.username = data['username']
        user_update.save()
        print("username:::::::::::::::::::",data['username'])
   
        if(user_data.username == data['username']):
            data_user = User_details.objects.filter(id=data['member_id']).update(
            name=data['name'].title(),
            username=data['username'],
            phone=data['phone'],
            email=data['email'],
            )
            for i in range(0, role_length):
                role_end_dt1 = role_end_dt[i]
                if role_end_dt1 == "":
                    role_end_dt1 = None
                data_save_user_role = user_permission_mapping.objects.filter(id=role_permission_name[i],user_id_id=data['member_id']).update(
                    role_mapping_id_id=int(role_id[i]),
                    start_dt=role_start_dt[i],
                    end_dt=role_end_dt1,
                    description=role_description[i]
                )
            for i in range(0, role_length_new):
                user = User.objects.get(username=data['username'])
                role_end_dt2 = role_end_dt_new[i]
                if role_end_dt2 == "":
                    role_end_dt2 = None
                data_save_user_role = user_permission_mapping(
                    auth_user_id_id=user.id,
                    user_id_id=user_data.id,
                    role_mapping_id_id=role_id_new[i],
                    start_dt=role_start_dt_new[i],
                    end_dt=role_end_dt2,
                    description=role_description_new[i]
                )
                data_save_user_role.save()

            
            if (user_data.manager_auth.username == data['manager_id']):
                pass
            else:
                user_id = data['manager_id']

                user_detail = User_details.objects.get(id=user_id)
                data_user = User_details.objects.filter(id=data['member_id']).update(
                manager_auth_id = user_detail.auth_user.id)
            if (data['password_option'] == "change_pass"):
                user_update.set_password(data['password'])
                user_update.save()
                user_data_update = User_details.objects.filter(id=data['member_id']).update(password=data['password'])
            else:
                pass
            try:
                fixed_height = 128
                image = Image.open(photo)
                width_size = int(fixed_height / image.height * image.width)

                resized_image = image.resize((width_size, fixed_height))
                from django.conf import settings
                resized_image.save("media/user_image/" + photo.name)
                image_new1 = 'user_image/' + photo.name
                data_user = User_details.objects.filter(id=data['member_id']).update(photo=image_new1)
            except:
                pass
        elif User_details.objects.filter(username=data['username']).exists():
            messages.warning(request,"Username already exists")
            return redirect(request.META['HTTP_REFERER'])
        else:
            data_user =User_details.objects.filter(id=data['member_id']).update(
                name=data['name'].title(),
                username=data['username'],
                phone=data['phone'],
                email=data['email'],
            )
            if (user_data.manager_auth.username == data['manager_id']):
                pass
            else:
                user_id = data['manager_id']

                user_detail = User_details.objects.get(id=user_id)
                data_user = User_details.objects.filter(id=data['member_id']).update(
                manager_auth_id = user_detail.auth_user.id)
            if (data['password_option'] == "change_password"):
                user_update.set_password(data['password'])
                user_update.save()
                user_data_update = User_details.objects.filter(id=data['member_id']).update(password=data['password'])
            else:
                pass
            try:
                fixed_height = 128
                image = Image.open(photo)
                width_size = int(fixed_height / image.height * image.width)

                resized_image = image.resize((width_size, fixed_height))
                from django.conf import settings
                resized_image.save("media/user_image/" + photo.name)
                image_new1 = 'user_image/' + photo.name
                data_user = User_details.objects.filter(id=data['member_id']).update(photo=image_new1)
            except:
                pass
        messages.success(request, "Successfully updated user details")
        return redirect('user_management')
    



def delete_role_management(request):
    if request.method == "POST":
        role_id = request.POST.get("role_id")
        data = Role_master.objects.filter(id=role_id).update(status=False)
        
        messages.success(request, "Role Deleted Successfully..")
        return redirect('role')
    else:
        id = request.GET.get("id")
        data = Role_master.objects.get(id=id)
        return render(request,"delete_role_management.html",{'data':data})
    


def delete_user_management(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        data = User_details.objects.filter(id=user_id).update(status=False)
        
        messages.success(request, "User Deleted Successfully..")
        return redirect('user_management')
    else:
        id = request.GET.get("id")
        data = User_details.objects.get(id=id)
        return render(request,"delete_user_management.html",{'data':data})

def exam(request):
    exam_details = Main_Exam_Master.objects.all()
    context = {
        'exam_details' : exam_details
    }
    return render(request,'exam.html',context)


def edit_exam(request):
    exam_id = request.GET.get("type")
    data = Main_Exam_Master.objects.get(id=exam_id)
    user = User.objects.all()
    data_main = Main_Exam_section.objects.filter(Exam_id_id = exam_id)
    intial_field = Exam_inital_field.objects.filter(Exam_id = data.id)
    lang = Main_exam_language.objects.filter(Exam_id = exam_id)
    context = {
        'data' : data,
        'user': user,
        'data_main' : data_main,
        'intial_field':intial_field,
        'lang':lang
    } 
    return render(request,'edit_exam.html' ,context)






#------------------------------------------------------------- Amritha Updates-------------------------------------------------------------


from django.http import JsonResponse

def exam_create(request):
    user_details = User.objects.all()
    context = {
        "user_details":user_details
    }
    return render(request,'exam_create.html',context)


def validation_check(request):
    section_line = request.GET.getlist("section_line",False)
    print("section_line::::::::",section_line)

    initial_line_count = request.GET.getlist("initial_count")
    print("initial_line_count:::::::::",initial_line_count)

    if section_line == False:
        data = {"message":"sectionFalse"}
        return JsonResponse(data,safe=False)
    else:
        data = {"message":"False"}
        return JsonResponse(data,safe=False)


def exam_save_action(request):
    if request.method == "POST":
        exam_title = request.POST.get("exam_title",False)
        exam_background = ""
        image_new1 = ""
        try:
            exam_background = request.FILES['exam_background']
            fixed_height = 758
            image = Image.open(exam_background)
            print("image.size",image.size)
            width_size = int(fixed_height/image.height * image.width)
            resized_image = image.resize((width_size,fixed_height))
            print("resizeeeeeed:",resized_image.size)
            from django.conf import settings
            resized_image.save("media/user_image/"+exam_background.name)
            image_new1 = 'user_image/'+exam_background.name
        except:
            pass
        responsible_name = request.POST.get("responsible_name",False)
        layout = request.POST.get("layout",False)
        progression = request.POST.get("progression",False)
        exam_time_limit = request.POST.get("exam_time_limit",False)
        exam_check = request.POST.get("exam_check",False)
        if exam_check == False:
            exam_time_limit = "00:00"
        else:
            pass
        start_message = request.POST.get("start_message",False)
        end_message = request.POST.get("end_message",False)
        selection = request.POST.get("selection_mode",False)
        Scoring = request.POST.get("Scoring",False)
        required_score = request.POST.get("required_score",False)
        if Scoring == "0":
            required_score = 0
        access_mode = request.POST.get("access_mode",False)
        login_required = request.POST.get("login_required",False)
        attempt_limit = request.POST.get("attempt_limit",False)
        if login_required == False:
            attempt_limit = 0
        else:
            pass
        section_line = request.POST.getlist("section_line")
        if len(section_line) == 0:
            messages.warning(request,"Add atleast one question")
            return redirect(request.META['HTTP_REFERER'])
        else:
            pass

        initial_line_count = request.POST.getlist("initial_count")
        for initial_count in initial_line_count:
            initial_label =  request.POST.get("initial_label"+initial_count)
            initial_type =  request.POST.get("initial_type"+initial_count)
            if initial_type == "selection":
                initial_answer =  request.POST.getlist("initial_answer"+initial_count)
                if not initial_answer:
                    messages.error(request,"Add Answer to Selection type")
                    return redirect('exam')
        # Main_Exam_Master creation
        exam_save = Main_Exam_Master.objects.create(Exam_title =exam_title,responsible_person_id =responsible_name,
        background_image = image_new1,
        start_message = start_message,end_message = end_message,
        layout = layout, progression_mode = progression,
        Exam_time_limit = exam_time_limit,selection_mode = selection,
        scoring_mode = Scoring,access_mode = access_mode,
        Login_required = login_required,
        attempt_limit = attempt_limit,
        created_by = request.user,
        Success_per = required_score
        )
        language_type = request.POST.getlist("language_type",False)   
        try: 
            for i in language_type:
                Main_exam_language.objects.create(Exam_id_id =exam_save.id,language_access = i )
        except:
            pass
        # Main_Exam_section save
        section_line_count = request.POST.getlist("section_line_count")
        modal_status = request.POST.getlist("modal_status")
        main_zip = zip(section_line,section_line_count,modal_status)
        for section_title,section_count,modal_status in main_zip:    
            if modal_status != "direct_question" :
                section_save = Main_Exam_section.objects.create(Exam_id_id = exam_save.id ,section_title = section_title,
                        section_type = "Section",created_by = request.user
                        )
            else:
                section_save = Main_Exam_section.objects.create(Exam_id_id = exam_save.id ,section_title = section_title,
                        section_type = "Question",
                        created_by = request.user
                        )
            #  Main_Question_Bank save
            print("section_count::::::",section_count)
            question = request.POST.getlist("question_name"+str(section_count))
            eng_question = request.POST.getlist("eng_question"+str(section_count))
            ar_question = request.POST.getlist("ar_question"+str(section_count))
            hi_question = request.POST.getlist("hi_question"+str(section_count))
            ur_question = request.POST.getlist("ur_question"+str(section_count))
            ta_question = request.POST.getlist("ta_question"+str(section_count))
            question_description = request.POST.getlist("qstn_descriptn"+str(section_count))
            question_comment = request.POST.getlist("question_comment"+str(section_count))
            model_count = request.POST.getlist("question_model_name"+str(section_count))

            question_zip = zip(question,eng_question,ar_question,hi_question,ur_question,ta_question,question_description,question_comment,model_count)
            for  question,eng_question,ar_question,hi_question,ur_question,ta_question,question_description,question_comment,model_count in question_zip:
                question_type = request.POST.get("question_type"+model_count)
                question_mandatory = request.POST.get("question_mandatory"+model_count,False)
                try:
                    question_image = request.FILES['question_image'+model_count]
                    import os
                    extension = os.path.splitext(str(question_image))[1]
                    print("extension:::",extension)
                    if extension == ".pdf" or extension == ".txt" or extension == ".doc" or extension == ".docx" :
                        image_new1 = question_image
                    else:
                        fixed_height = 758
                        image = Image.open(question_image)
                        print("image.size",image.size)
                        width_size = int(fixed_height/image.height * image.width)
                        resized_image = image.resize((width_size,fixed_height))
                        print("resizeeeeeed:",resized_image.size)
                        from django.conf import settings
                        resized_image.save("media/user_image/"+question_image.name)
                        image_new1 = 'user_image/'+question_image.name
                    question_save = Main_Question_Bank.objects.create(Question=question,question_ar=ar_question,question_en=eng_question,question_hi=hi_question,question_ur=ur_question,question_ta=ta_question,
                        Description =  question_description, Question_type = question_type,created_by = request.user,
                        comments = question_comment,Imagefield =image_new1,manadatory = question_mandatory)
                except:
                    question_save = Main_Question_Bank.objects.create(Question=question,question_ar=ar_question,question_en=eng_question,question_hi=hi_question,question_ur=ur_question,question_ta=ta_question,
                        Description =  question_description, Question_type = question_type,created_by = request.user,
                        comments = question_comment,manadatory = question_mandatory)
                if modal_status == "direct_question":
                        section_save.Question_bank_id_id = question_save.id
                        section_save.save()
                        Section_Question_Mapping.objects.create(Section_id_id = section_save.id,Question_id_id = question_save.id,created_by = request.user)
                else:
                    Section_Question_Mapping.objects.create(Section_id_id = section_save.id,Question_id_id = question_save.id,created_by = request.user)
                    pass
                # Question_Bank_multiple_choice save 
                question_line_count = request.POST.getlist("question_line_count"+model_count)
                total_score = 0
                for  choice_count in question_line_count:
                    choice_data = request.POST.get("question_choice"+choice_count+'-'+model_count)
                    eng_choice = request.POST.get("eng_choice"+choice_count+'-'+model_count)
                    ar_choice = request.POST.get("ar_choice"+choice_count+'-'+model_count)
                    hi_choice = request.POST.get("hi_choice"+choice_count+'-'+model_count)
                    ur_choice = request.POST.get("ur_choice"+choice_count+'-'+model_count)
                    ta_choice = request.POST.get("ta_choice"+choice_count+'-'+model_count)
                    result_status = request.POST.get("addline_check"+choice_count+'-'+model_count,False)
                    Score = request.POST.get("Score"+choice_count+'-'+model_count,False)
                    if (result_status == "True"):
                        total_score += int(Score)
                    try:
                        file_data = request.FILES['question_image_choice'+choice_count+'-'+model_count]
                        import os
                        extension = os.path.splitext(str(file_data))[1]
                        print("extension:::",extension)
                        if extension == ".pdf" or extension == ".txt" or extension == ".doc" or extension == ".docx" :
                            image_new1 = file_data
                        else:
                            fixed_height = 758
                            image = Image.open(file_data)
                            print("image.size",image.size)
                            width_size = int(fixed_height/image.height * image.width)
                            resized_image = image.resize((width_size,fixed_height))
                            print("resizeeeeeed:",resized_image.size)
                            from django.conf import settings
                            resized_image.save("media/user_image/"+file_data.name)
                            image_new1 = 'user_image/'+file_data.name
                        question_choices = Question_Bank_multiple_choice.objects.create(Question_id_id=question_save.id,choice= choice_data,choice_ar=ar_choice,choice_en=eng_choice,choice_hi=hi_choice,choice_ur=ur_choice,choice_ta=ta_choice,
                            Imagefield =  image_new1, file_type = extension, Mark = Score,result_status=result_status,created_by = request.user
                            )
                        if(result_status == "True"):
                            question_save.answer_id.add(question_choices.id)
                    except:
                        question_choices = Question_Bank_multiple_choice.objects.create(Question_id_id=question_save.id,choice= choice_data,choice_ar=ar_choice,choice_en=eng_choice,choice_hi=hi_choice,choice_ur=ur_choice,choice_ta=ta_choice,
                            Mark = Score,result_status=result_status,created_by = request.user
                            )
                        if(result_status == "True"):
                            question_save.answer_id.add(question_choices.id)
                            pass
                question_save.total_mark = total_score
                question_save.save()


        # Exam_inital_field save
        initial_line_count = request.POST.getlist("initial_count")
        for initial_count in initial_line_count:
            initial_label =  request.POST.get("initial_label"+initial_count)
            initial_type =  request.POST.get("initial_type"+initial_count)
            exam_initial_save = Exam_inital_field.objects.create(Exam_id_id = exam_save.id,title = initial_label,field_type = initial_type  )
            if initial_type == "selection":
                initial_answer =  request.POST.getlist("initial_answer"+initial_count)
                for i in initial_answer:
                    Exam_inital_field_choice.objects.create(initial_field_id_id = exam_initial_save.id,choice_name = i)
            else:
                pass
        messages.success(request,"Successfully added Exam details")
        return redirect('exam')
        


def open_section_based_question(request):
    modal_id = request.GET.get("modal_id")
    data_id = request.GET.get("data_id")
    status = request.GET.get("status")
    value1 = str(data_id)+"-"+str(modal_id)

    context = {
        "value1":value1,
        "modal_id":modal_id,
        "data_id":data_id,
        "status":status,
    }
    
    return render(request,'open_section_based_question.html',context)





# --------------------amritha end method------------------------




# ---------------anirudh ----------------------------------
def update_exam_details(request):
    if request.method == "POST":
        updated_id = request.POST.get("updated_id",False)
        exam_title = request.POST.get("exam_title",False)
        responsible_person = request.POST.get("responsible_person",False)
        start_message = request.POST.get("start_message",False)
        end_message = request.POST.get("end_message",False)
        layout = request.POST.get("layout",False)
        access_mode = request.POST.get("access_mode",False)
        progression_mode = request.POST.get("progression_mode",False)
        login_required = bool(request.POST.get('login_required', False))
        attempt_limit = request.POST.get("attempt_limit",False)
        attempt_check = request.POST.get("Attempt_check",False)
        required_score = request.POST.get("required_score",False)

        if attempt_check == False:
            attempt_limit = 0
        else:
            pass
        if login_required == False:
            attempt_limit = 0
        else:
            pass
        exam_time_limit = request.POST.get("exam_time_limit",False)
        section = request.POST.get("section",False)
        scoring_mode = request.POST.get("scoring_mode",False)
        if exam_time_limit == "":
            exam_time_limit = "00:00:00"
        else:
            pass   

            #  initail field #######
        
        initial_line_count = request.POST.getlist("initial_count")
        for initial_count in initial_line_count:
            initial_label =  request.POST.get("initial_label"+initial_count)
            initial_type =  request.POST.get("initial_type"+initial_count)
            exam_initial_save = Exam_inital_field.objects.create(Exam_id_id = updated_id,title = initial_label,field_type = initial_type  )
            if initial_type == "selection":
                initial_answer =  request.POST.getlist("initial_answer"+initial_count)
                for i in initial_answer:
                    Exam_inital_field_choice.objects.create(initial_field_id_id = exam_initial_save.id,choice_name = i)
            else:
                pass

        data_update = Main_Exam_Master.objects.filter(id=updated_id).update(
            responsible_person_id = responsible_person,
            Exam_title = exam_title,
            start_message = start_message,
            end_message = end_message,
            layout = layout,
            progression_mode = progression_mode,
            Exam_time_limit = exam_time_limit,
            selection_mode = section,
            scoring_mode = scoring_mode,
            access_mode = access_mode,
            Login_required = login_required,
            attempt_limit = attempt_limit,
            Success_per = required_score
        )
        messages.success(request,str("Updated"))
        return redirect(request.META['HTTP_REFERER'])


def section_Question_view_modal(request):
    data_id = request.GET.get("data_id")
    data = Main_Question_Bank.objects.get(id=data_id)
    value1 = str(data_id)+"-"+str(data_id)
    modal_id = request.GET.get("modal_id")

    print("value1:::::::::::::",value1)
    return render(request,'section_Question_view_modal.html',{'data':data,'value1':value1,'modal_id':modal_id})

def Question_Management_update(request):
    updated_id = request.POST.get("updated_id",False)
    model_count = request.POST.get("question_model_name")
    question_name = request.POST.get("question_name",False)
    remove_status = request.POST.getlist("remove_status[]")
    Question_type = request.POST.get("Question_type",False)
    Description = request.POST.get("Description",False)
    manadatory = bool(request.POST.get('manadatory', False))
    comments = request.POST.get("comments",False)
    choice_update = request.POST.getlist("choice_update[]",False)
    question_choice = request.POST.getlist("question_choice[]",False)
    answer = request.POST.getlist("answer[]",False)
    Score = request.POST.getlist("Score[]",False)
    Qmain=Main_Question_Bank.objects.get(id=updated_id)

    total_score = 0

    data_save1=Main_Question_Bank.objects.filter(id=updated_id).update(
                Question =  question_name,
                Question_type = Question_type,
                Description = Description,
                manadatory = manadatory,
                comments =  comments
    )

    image_field = request.FILES.getlist('exam_choice_image[]')

    for i in range(len(choice_update)):
        if int(remove_status[i]) == 1: 
            if image_field :
                for k in range(len(image_field)):
                    Question_Bank_multiple_choice.objects.filter(id=choice_update[i]).update(
                            Imagefield = image_field[k]
                        )
            else:

                Question_Bank_multiple_choice.objects.filter(id=choice_update[i]).update(
                        Imagefield = ""
                    )
              
    for i in range(len(choice_update)):
        Question_Bank_multiple_choice.objects.filter(id=choice_update[i]).update(
                    choice = question_choice[i],
                    Mark = Score[i],
                )

        print("answer;;;;;;;;;;;;;;;;;;",answer)
        total_score += int(Score[i])

        if answer == False:
            Question_Bank_multiple_choice.objects.filter(id=choice_update[i]).update(
                    result_status = False
                )
        else:

            for j in range(len(answer)):
                if answer[j] == choice_update[i]:
                    print("answer:qqqqqq:::::",answer[j]) 
                    update_result=Question_Bank_multiple_choice.objects.filter(id=choice_update[i]).update(
                        result_status = True
                    )
                    data_choice_id = Question_Bank_multiple_choice.objects.get(id=choice_update[i])
                    
                    Qmain.answer_id.add(data_choice_id.id)
                    Qmain.save()

 

    question_line_count = request.POST.getlist("question_line_count"+model_count)
    print("question_line_count::::::::::::",question_line_count)
    if question_line_count :
        question_save = Main_Question_Bank.objects.get(id=updated_id)
        total_score = 0
        for  choice_count in question_line_count:
            choice_data = request.POST.get("question_choice"+choice_count+'-'+model_count)
            eng_choice = request.POST.get("eng_choice"+choice_count+'-'+model_count)
            ar_choice = request.POST.get("ar_choice"+choice_count+'-'+model_count)
            hi_choice = request.POST.get("hi_choice"+choice_count+'-'+model_count)
            ur_choice = request.POST.get("ur_choice"+choice_count+'-'+model_count)
            ta_choice = request.POST.get("ta_choice"+choice_count+'-'+model_count)
            result_status = request.POST.get("addline_check"+choice_count+'-'+model_count,False)
            Score = request.POST.get("Score"+choice_count+'-'+model_count,False)
            if (result_status == "True"):
                total_score += int(Score)
            try:
                file_data = request.FILES['question_image_choice'+choice_count+'-'+model_count]
                import os
                extension = os.path.splitext(str(file_data))[1]
                print("extension:::",extension)
                if extension == ".pdf" or extension == ".txt" or extension == ".doc" or extension == ".docx" :
                    image_new1 = file_data
                else:
                    fixed_height = 758
                    image = Image.open(file_data)
                    print("image.size",image.size)
                    width_size = int(fixed_height/image.height * image.width)
                    resized_image = image.resize((width_size,fixed_height))
                    print("resizeeeeeed:",resized_image.size)

                    from django.conf import settings
                    resized_image.save("media/Question_Bank_image/"+file_data.name)
                    image_new1 = 'Question_Bank_image/'+file_data.name
                    
                question_choices = Question_Bank_multiple_choice.objects.create(Question_id_id=question_save.id,choice= choice_data,choice_ar=ar_choice,choice_en=eng_choice,choice_hi=hi_choice,choice_ur=ur_choice,choice_ta=ta_choice,
                    Imagefield =  image_new1, file_type = extension, Mark = Score,result_status=result_status,created_by = request.user
                    )

                if(result_status == "True"):
                    question_save.answer_id.add(question_choices.id)
            except:
                question_choices = Question_Bank_multiple_choice.objects.create(Question_id_id=question_save.id,choice= choice_data,choice_ar=ar_choice,choice_en=eng_choice,choice_hi=hi_choice,choice_ur=ur_choice,choice_ta=ta_choice,
                    Mark = Score,result_status=result_status,created_by = request.user
                    )

                if(result_status == "True"):
                    question_save.answer_id.add(question_choices.id)
                    pass

    question_save.total_mark = total_score
    question_save.save()

    messages.success(request,str("Updated"))
    return redirect(request.META['HTTP_REFERER'])


def section_title_edit(request):
    updated_id = request.POST.get("updated_id",False)
    exam_title = request.POST.get("exam_title")
    data = Main_Exam_section.objects.filter(id=updated_id).update(
        section_title = exam_title
        )
    messages.success(request,str("Section Title Updated"))
    return redirect(request.META['HTTP_REFERER'])


def delete_initial_field(request):
    if request.method == "POST":
        field_id = request.POST.get("initial_field_id")
        field = Exam_inital_field.objects.get(id=field_id)
        field.delete()
        messages.success(request, "initial field Deleted Successfully..")
        return redirect(request.META['HTTP_REFERER'])
    else:
        id = request.GET.get("id")
        data = Exam_inital_field.objects.get(id=id)
        return render(request,"delete_initial_field.html",{'data':data})


def New_section_add(request):
    if request.method == "POST":
        exam_id = request.POST.get("exam_id")
        section_title = request.POST.get("section_title")

        section_save = Main_Exam_section.objects.create(
                        Exam_id_id = exam_id,
                        section_title = section_title,
                        section_type = "Section",
                        created_by = request.user
                    )
        return redirect(request.META['HTTP_REFERER'])
    


def delete_question_section(request):
    if request.method == "POST":
        field_id = request.POST.get("field_id")
        field = Main_Exam_section.objects.get(id=field_id)
        field.delete()
        messages.success(request, "Field Deleted Successfully..")
        return redirect(request.META['HTTP_REFERER'])
    else:
        id = request.GET.get("id")
        data = Main_Exam_section.objects.get(id=id)
        return render(request,"delete_question_section.html",{'data':data})


def delete_question_modal(request):
    if request.method == "POST":
        field_id = request.POST.get("field_id")
        field = Main_Question_Bank.objects.get(id=field_id)
        field.delete()
        messages.success(request, "Question Deleted Successfully..")
        return redirect(request.META['HTTP_REFERER'])
    else:
        id = request.GET.get("id")
        data = Main_Question_Bank.objects.get(id=id)
        return render(request,"delete_question_modal.html",{'data':data})
    



def save_section_question_action(request):
    if request.method == "POST":
        updated_id = request.POST.get("updated_id")
        button_status =  request.POST.get("button_status")
        exam_id =  request.POST.get("exam_id")
        section_line = request.POST.getlist("section_line")
        section_line_count = request.POST.getlist("section_line_count")
        section_count = updated_id
        question = request.POST.get("question_name")
        eng_question = request.POST.get("eng_question")
        ar_question = request.POST.get("ar_question")
        hi_question = request.POST.get("hi_question")
        ur_question = request.POST.get("ur_question")
        ta_question = request.POST.get("ta_question")
        question_description = request.POST.get("qstn_descriptn")
        question_comment = request.POST.get("question_comment")
        model_count = request.POST.get("question_model_name")
        question_type = request.POST.get("question_type")
        question_mandatory = request.POST.get("question_mandatory",False)

        print("question::::::::::::::::",question)
        print("eng_question::::::::::::::::",eng_question)
        print("ar_question::::::::::::::::",ar_question)
        
        try:
            print("qaaaaaaaaaaaaooo")
            question_image = request.FILES['question_image']
            print("qaaaaaaaaaaaaooo11")
            import os
            extension = os.path.splitext(str(question_image))[1]
            print("extension:::",extension)
            if extension == ".pdf" or extension == ".txt" or extension == ".doc" or extension == ".docx" :
                image_new1 = question_image
            else:
                fixed_height = 758
                image = Image.open(question_image)
                print("image.size",image.size)
                width_size = int(fixed_height/image.height * image.width)
                resized_image = image.resize((width_size,fixed_height))
                print("resizeeeeeed:",resized_image.size)
                from django.conf import settings
                resized_image.save("media/user_image/"+question_image.name)
                image_new1 = 'user_image/'+question_image.name

            if button_status == "direct_question" :
                section_save = Main_Exam_section.objects.create(Exam_id_id = exam_id ,section_title = question,
                        section_type = "Question",
                        created_by = request.user
                        )
            else:   

               pass

            question_save = Main_Question_Bank.objects.create(Question=question,question_ar=ar_question,question_en=eng_question,question_hi=hi_question,question_ur=ur_question,question_ta=ta_question,
                Description =  question_description, Question_type = question_type,created_by = request.user,
                comments = question_comment,Imagefield =image_new1,manadatory = question_mandatory)

            if button_status == "direct_question":
                section_save.Question_bank_id_id = question_save.id
                section_save.save()
                Section_Question_Mapping.objects.create(Section_id_id = section_save.id,Question_id_id = question_save.id,created_by = request.user,status="True")
            else:
                Section_Question_Mapping.objects.create(Section_id_id = updated_id,Question_id_id = question_save.id,created_by = request.user,status="True")
             # Question_Bank_multiple_choice save 
            question_line_count = request.POST.getlist("question_line_count")

            total_score = 0
            for  choice_count in question_line_count:
                choice_data = request.POST.get("question_choice"+choice_count+'-'+model_count)
                eng_choice = request.POST.get("eng_choice"+choice_count+'-'+model_count)
                ar_choice = request.POST.get("ar_choice"+choice_count+'-'+model_count)
                hi_choice = request.POST.get("hi_choice"+choice_count+'-'+model_count)
                ur_choice = request.POST.get("ur_choice"+choice_count+'-'+model_count)
                ta_choice = request.POST.get("ta_choice"+choice_count+'-'+model_count)
                result_status = request.POST.get("addline_check"+choice_count+'-'+model_count,False)
                Score = request.POST.get("Score"+choice_count+'-'+model_count,False)
                if (result_status == "True"):
                    total_score += int(Score)
                try:
                    file_data = request.FILES['question_image_choice'+choice_count+'-'+model_count]
                    import os
                    extension = os.path.splitext(str(file_data))[1]
                    print("extension:::",extension)
                    if extension == ".pdf" or extension == ".txt" or extension == ".doc" or extension == ".docx" :
                        image_new1 = file_data
                    else:
                        fixed_height = 758
                        image = Image.open(file_data)
                        print("image.size",image.size)
                        width_size = int(fixed_height/image.height * image.width)
                        resized_image = image.resize((width_size,fixed_height))
                        print("resizeeeeeed:",resized_image.size)
                        from django.conf import settings
                        resized_image.save("media/Question_Bank_image/"+file_data.name)
                        image_new1 = 'Question_Bank_image/'+file_data.name
                    question_choices = Question_Bank_multiple_choice.objects.create(Question_id_id=question_save.id,choice= choice_data,choice_ar=ar_choice,choice_en=eng_choice,choice_hi=hi_choice,choice_ur=ur_choice,choice_ta=ta_choice,
                        Imagefield =  image_new1, file_type = extension, Mark = Score,result_status=result_status,created_by = request.user
                        )

                    if(result_status == "True"):
                        question_save.answer_id.add(question_choices.id)
                except:
                    question_choices = Question_Bank_multiple_choice.objects.create(Question_id_id=question_save.id,choice= choice_data,choice_ar=ar_choice,choice_en=eng_choice,choice_hi=hi_choice,choice_ur=ur_choice,choice_ta=ta_choice,
                        Mark = Score,result_status=result_status,created_by = request.user
                        )
                    if(result_status == "True"):
                        question_save.answer_id.add(question_choices.id)
                        pass
            question_save.total_mark = total_score
            question_save.save()
        except:
            pass
        messages.success(request, "Added Successfully")
        return redirect(request.META['HTTP_REFERER'])


def open_section_based_question_edit(request):
    button_status = request.GET.get("button_status")
    modal_id = request.GET.get("modal_id")
    data_id = request.GET.get("data_id")
    value1 = str(data_id)+"-"+str(modal_id)
    status = request.GET.get("status")



    print("value:::::::::",value1)
    print("modal_id:::::::::",modal_id)
    print("data_id:::::::::",data_id)






    if button_status == "section_question":
        section_id = Main_Exam_section.objects.get(id=data_id)
    else:
        section_id = 0

    context = {

        "value1":value1,
        "modal_id":modal_id,
        "data_id":data_id,
        "status":status,
        "section_id":section_id,
        "button_status":button_status
    }
    
    return render(request,'open_section_based_question_edit.html',context)





# /////////////////////////////////////////////////////////////////////////
def exam_login_new(request):
    slug = request.GET.get("type")
    data = Main_Exam_Master.objects.get(slug=slug)
    return render(request,'exam_login_new.html',{'data':data})


def customer_using_link_new(request):
    slug = request.GET.get("type")
    data_exam = Main_Exam_Master.objects.get(slug=slug)
    data = Exam_inital_field.objects.filter(Exam_id=data_exam)
    return render(request,'customer_using_link_new.html',{'data':data})


def attend_exam_new(request,slug):
    data = Main_Exam_Master.objects.get(slug=slug)
    uid = request.session['uid']
    data_attend = Exam_attend_user.objects.get(id=uid)
    data_language = Main_exam_language.objects.filter(Exam_id=data)
    return render(request,'attend_exam_new.html',{'data':data,'data_attend':data_attend,'data_language':data_language})

def exam_login_action_new(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        password = request.POST.get("password")
        user = authenticate(username=uname, password=password)
        if user is not None:
            exam_id = request.POST.get("exam_id")
            data_exam = Main_Exam_Master.objects.get(slug=exam_id)
            try:
                data_user = User.objects.get(username=uname)
                data_user_new = Exam_attend_user.objects.get(auth_user=data_user,exam_id=data_exam)
            except:
                data_user_new = ""
            if data_user_new:
                request.session['uid'] = data_user_new.id
            else:
                data = Exam_attend_user.objects.create(
                    exam_id=data_exam,
                    user_type="login_user",
                    auth_user=user,
                )
                request.session['uid'] = data.id
            url = "attend_exam_new/" + exam_id
            return redirect(url)
        else:
            messages.error(request, str("Incorrect username or password"))
            return redirect(request.META['HTTP_REFERER'])

def exam_link_action_new(request):
    if request.method == "POST":
        exam_id = request.POST.getlist('exam_details')
        data_exam = Main_Exam_Master.objects.get(slug=exam_id[0])
        data = Exam_attend_user.objects.create(
            exam_id=data_exam,
            user_type="non_login_user",
        )
        request.session['uid'] = data.id
        attend_user_id = request.POST.getlist('attend_user_id')
        title = request.POST.getlist('title')
        zip_objects = zip(attend_user_id, title)
        for i, j in zip_objects:
            data_new = exam_attend_user_initial_field.objects.create(
                exam_attend_user_id = data,
                Exam_inital_field_id_id=i,
                answer=j
            )
        url = "attend_exam_new/" + exam_id[0]
        return redirect(url)

def wizard_new(request):
    slug = request.GET.get("type")
    data_main_exam = Main_Exam_Master.objects.get(slug=slug)
    try:
        z = str(data_main_exam.Exam_time_limit) + str(',000')
        import datetime
        import time
        x = time.strptime(z.split(',')[0], '%H:%M:%S')
        y = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
    except:
        y = ""
    data_count = ""
    if (data_main_exam.layout == "0"):
        if (data_main_exam.selection_mode == "All questions"):
            data = Section_Question_Mapping.objects.filter(Section_id__Exam_id=data_main_exam)
        else:
            data = Section_Question_Mapping.objects.filter(Section_id__Exam_id=data_main_exam).order_by("?")
        question_list = list(data.values_list('Question_id', flat=True))
        data_question = Main_Question_Bank.objects.filter(id__in=question_list)
        total_mark = sum(data_question.values_list('total_mark', flat=True))
        return render(request, 'wizard_new0.html',
                      {'data_main_exam': data_main_exam, 'data': data, 'data_count': data_count,
                       'total_mark': total_mark,'y':y})
    elif (data_main_exam.layout == "1"):
        if (data_main_exam.selection_mode == "All questions"):
            data = Main_Exam_section.objects.filter(Exam_id=data_main_exam)
        else:
            data = Main_Exam_section.objects.filter(Exam_id=data_main_exam).order_by("?")
        data1 = Section_Question_Mapping.objects.filter(Section_id__Exam_id=data_main_exam)
        question_list = list(data1.values_list('Question_id', flat=True))
        data_question = Main_Question_Bank.objects.filter(id__in=question_list)
        total_mark = sum(data_question.values_list('total_mark', flat=True))
        return render(request, 'wizard_new1.html',
                      {'data_main_exam': data_main_exam, 'data': data, 'data_count': data_count,
                       'total_mark': total_mark,'y':y})
    else:
        if (data_main_exam.selection_mode == "All questions"):
            data = Section_Question_Mapping.objects.filter(Section_id__Exam_id=data_main_exam)
        else:
            data = Section_Question_Mapping.objects.filter(Section_id__Exam_id=data_main_exam).order_by("?")
        data_count = data.count()
        question_list = list(data.values_list('Question_id', flat=True))
        data_question = Main_Question_Bank.objects.filter(id__in=question_list)
        total_mark = sum(data_question.values_list('total_mark', flat=True))
        return render(request, 'wizard_new2.html', {'data_main_exam': data_main_exam, 'data': data,'data_count':data_count,'total_mark':total_mark,'y':y})

def exam_result_new(request):
    uid = request.session['uid']
    slug = request.GET.get("type")
    data_main_exam = Main_Exam_Master.objects.get(slug=slug)
    data_answer1 = exam_attend_user_score.objects.filter(exam_attend_user_id_id=uid)
    if data_answer1:
        question_list = list(data_answer1.values_list('Question_id', flat=True))
        data_question = Main_Question_Bank.objects.filter(id__in=question_list)
        total_mark = sum(data_question.values_list('total_mark', flat=True))
        total_score = sum(data_answer1.values_list('Mark', flat=True))
        exam_per = (total_score/total_mark)*100
        return render(request, 'exam_result_new.html',
                      {'data_main_exam': data_main_exam,'total_mark':total_mark,'total_score': total_score,
                       'data_answer': data_answer1,'exam_per':exam_per})
    else:
        total_mark = 0
        total_score = 0
        if request.method == "POST":
            question_id = request.POST.getlist("question_id")
            for i in question_id:
                data = Main_Question_Bank.objects.get(id=i)
                print("data.total_mark",data.total_mark)
                Section_Question = Section_Question_Mapping.objects.get(Question_id=data)
                data_create = exam_attend_user_score.objects.create(exam_attend_user_id_id=uid,
                                                                    section_question_id=Section_Question,
                                                                    Mark=0, result_status=False,
                                                                    Question_id=data)
                if data.Question_type == "Checkbox":
                    answer = request.POST.getlist("answer"+i)
                    for j in answer:
                        try:
                            data_option = Question_Bank_multiple_choice.objects.get(id=j)
                            if (data.answer_id.count() < len(answer)):
                                data_create.user_select_choice.add(data_option.id)
                            else:
                                if (data_option.result_status == True):
                                    total_score += data_option.Mark
                                    data_create_mark = exam_attend_user_score.objects.get(id=data_create.id)
                                    mark = data_create_mark.Mark + data_option.Mark
                                    data_create_new = exam_attend_user_score.objects.filter(id=data_create.id).update(Mark=mark)
                                    data_create.correct_answer.add(data_option.id)
                                    data_create.user_select_choice.add(data_option.id)
                                else:
                                    data_create.user_select_choice.add(data_option.id)
                        except:
                            pass
                else:
                    answer = request.POST.get("answer"+i)
                    try:
                        data_option = Question_Bank_multiple_choice.objects.get(id=answer)
                        if (data_option.result_status == True):
                            total_score += data_option.Mark
                            data_create_mark = exam_attend_user_score.objects.get(id=data_create.id)
                            mark = data_create_mark.Mark + data_option.Mark
                            data_create_new = exam_attend_user_score.objects.filter(id=data_create.id).update(Mark=mark)
                            data_create.correct_answer.add(data_option.id)
                            data_create.user_select_choice.add(data_option.id)
                        else:
                            data_create.user_select_choice.add(data_option.id)
                    except:
                        pass
                total_mark += data.total_mark
            print("total_mark",total_mark)
            print("total_score",total_score)
        exam_per = (total_score / total_mark) * 100
        data_attend = Exam_attend_user.objects.filter(id=uid).update(attend_status=True)
        data_answer = exam_attend_user_score.objects.filter(exam_attend_user_id_id=uid)
        return render(request, 'exam_result_new.html', {'data_main_exam': data_main_exam,'total_mark':total_mark,'total_score':total_score,'data_answer':data_answer,'exam_per':exam_per})