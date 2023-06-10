from django.shortcuts import render, redirect
from .models import validate_process



# Create your views here.

# def registeration_validate_process(request):
#     return render(request,'validate_process_Template/registration.html')


def registration_validate_process(request):
    if request.method=='POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Phone_number = request.POST['Phone_number']
        Password = request.POST['Password']
        Address = request.POST['Address']
        validate_process(Name=Name, Email=Email, Phone_number=Phone_number, Password=Password , Address=Address).save()
        return redirect('/registration_validate_process/')
    else:
        return render(request, 'validate_process_Template/registration.html')


def validate_home_index(request):
    return render(request,'index.html')

# def v_login(request):
#     return render(request,'validate_process_Template/v_login.html')


def v_login(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password = request.POST['Password']
        try:
            r = validate_process.objects.get(Email=Email, Password=Password)
            request.session['data'] = r.Email

            if r is not None:
                # messages.info(request, 'welcome')
                return redirect('/data_home_index/')
        except validate_process.DoesNotExist as e:
            # messages.info(request, 'name does not exists')
            return redirect('/v_login/')
    # else:
    #     return redirect('/d_login/')
    return render(request,'validate_process_Template/v_login.html')

def uuu(request):
    return render(request,'validate_process_Template/uuu.html')

