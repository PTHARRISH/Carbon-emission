from django.shortcuts import render, redirect

from .models import community_process


def community_home_index(request):
    return render(request,'index.html')





# def registration_community_process(request):
#     return render(request, 'community_process_Template/registration.html')
def registration_community_process(request):
    if request.method=='POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Phone_number = request.POST['Phone_number']
        Password = request.POST['Password']
        Address = request.POST['Address']
        community_process(Name=Name, Email=Email, Phone_number=Phone_number, Password=Password , Address=Address).save()
        return redirect('/c_login/')
    else:
        return render(request, 'community_process_Template/registration.html')


def c_login(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password = request.POST['Password']
        try:
            r = community_process.objects.get(Email=Email, Password=Password)
            request.session['community'] = r.Email

            if r is not None:
                # messages.info(request, 'welcome')
                return redirect('/community_home_index/')
        except community_process.DoesNotExist as e:
            # messages.info(request, 'name does not exists')
            return redirect('/c_login/')
    # else:
    #     return redirect('/d_login/')
    return render(request,'community_process_Template/c_login.html')

