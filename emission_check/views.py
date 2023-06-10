from django.contrib import messages
from django.shortcuts import render, redirect
from .models import emission_check
from .models import emission_calculate
from .models import userdatail


# Create your views here.


def registration_emission_check(request):
    if request.method=='POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Phone_number = request.POST['Phone_number']
        Password = request.POST['Password']
        Address = request.POST['Address']
        emission_check(Name=Name, Email=Email, Phone_number=Phone_number, Password=Password , Address=Address).save()
        messages.info(request, 'Registration Successfull!!!')
        return redirect('/login/')
    else:
        return render(request, 'emission_check/registration.html')



def emission_home_index(request):
        return render(request, 'index.html')



def e_login(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password = request.POST['Password']
        try:
            r = emission_check.objects.get(Email=Email, Password=Password)
            request.session['data'] = r.Email
            if r is not None:
                messages.info(request, 'Welcome to Home!!!')
                return redirect('/home/')
        except emission_check.DoesNotExist as e:
            messages.info(request, 'Email Does not Match')
            return redirect('/login/')
    return render(request,'emission_check/login.html')



def emission_check_homepage(request):
    if request.method == 'POST':
        petrol = request.POST ['petrol']
        diesel = request.POST ['diesel']
        gas = request.POST ['gas']
        taxi = request.POST ['taxi']
        localbus = request.POST ['localbus']
        train = request.POST ['train']
        lpg_cyclinder = request.POST ['lpg_cyclinder']
        electricity = request.POST ['electricity']
        emission_calculate(petrol=petrol, diesel=diesel, gas=gas, taxi=taxi, localbus=localbus, train=train,
                           lpg_cyclinder=lpg_cyclinder, electricity=electricity).save()
        messages.info(request, 'Information Submitted Successfully!!!')
        return redirect('/emission_check_homepage/')
    else:
        return render(request,'emission_check/emission_check_homepage.html')



def home(request):
    return render(request,'emission_check/emission_home.html')



def view_emission_calculate(request):
    data = emission_calculate.objects.all()
    return render(request,'emission_check/data_view.html',{'data':data})



def total_emission(request,id):
    get = emission_calculate.objects.get(id=id)
    get.emission_calculate=True
    get.save()
    r = get.id
    a = get.petrol
    b = get.diesel
    c = get.gas
    d = get.taxi
    e = get.localbus
    f = get.train
    g = get.lpg_cyclinder
    h = get.electricity
    i = (float(a)*2.33+float(b)*2.68+float(c)*2.68+float(d)*0.31+float(e)*0.05+float(f)*0.05+float(g)*42.50+float(h)*0.90)
    get.total_emission = i
    print(i)
    st = emission_calculate.objects.filter(id=r).update(Total_emission=i)
    messages.info(request,'Forwarded to admin , get approve from admin for analyse process!!!')
    return redirect('/view_emission_calculate/')



def emission_logout(request):
    if 'admin' in request.session:
        request.session.pop('management', None)
        messages.success(request, 'session logged out')
        return redirect('/')
    else:
        return redirect('/')



def userindex(request):
    return render(request,'emission_check/userindex.html')



def usersave(request):
    if request.method=='POST':
        name = request.POST['name']
        address = request.POST['address']
        # date = request.POST['date']
        no_of_peple = request.POST['no_of_peple']
        type_of_shelter = request.POST['type_of_shelter']
        region = request.POST['region']
        userdatail( name=name, address=address, no_of_peple=no_of_peple , type_of_shelter=type_of_shelter, region=region).save()
        messages.info(request, 'User details saved')
        return redirect('/userindex/')
    else:
        return render(request, 'emission_check/userindex.html')



def user_update(request):
    key = userdatail.objects.all()
    return render(request, 'emission_check/user_update.html',{'key': key})



def delete(request, id):
    member = userdatail.objects.get(id=id)
    member.delete()
    messages.info(request, 'Delete is done!!!')
    return redirect('/user_update/')



def update(request, id):
    value = userdatail.objects.get(id=id)
    if request.method == 'POST':
        value.name = request.POST.get('name')
        value.address = request.POST.get('address')
        value.no_of_peple = request.POST.get('no_of_peple')
        value.type_of_shelter = request.POST.get('type_of_shelter')
        value.region = request.POST.get('region')
        value.save()
        messages.info(request, 'Updated the information!!!')
        return redirect('/user_update/')
    return render(request, 'emission_check/updatetemp.html', {'value': value})



def updatetemp(request):
    return render(request, 'emission_check/updatetemp.html')