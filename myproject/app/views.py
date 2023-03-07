from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages

from .models import *
# Create your views here.



def dashboard(request):
    return render(request,'dashboard.html')

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
        messages.success(request, "Successfully updated Member details")
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
