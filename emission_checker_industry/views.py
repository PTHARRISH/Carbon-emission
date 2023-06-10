from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *


# Create your views here.



def emission_home_index(request):
    return render(request,'index.html')




def e1_login(request):
    return render(request,"emission_checker_industry_Template/e1_login.html")



def registration_emission_checker_industry(request):
    if request.method=='POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Phone_number = request.POST['Phone_number']
        Password = request.POST['Password']
        Address = request.POST['Address']
        emission_checker_industry(Name=Name, Email=Email, Phone_number=Phone_number, Password=Password , Address=Address).save()
        messages.info(request, 'Welcome to login!!!')
        return redirect('/e1_login/')
    else:
        return render(request, 'emission_checker_industry_Template/registration.html')



def e1_login(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password = request.POST['Password']
        try:
            r = emission_checker_industry.objects.get(Email=Email, Password=Password)
            request.session['data'] = r.Email
            if r is not None:
                messages.info(request, 'Welcome to home page for industry emission !!!')
                return redirect('/home_industry/')
        except emission_checker_industry.DoesNotExist as e:
            messages.info(request, 'Email not matched')
            return redirect('/e1_login/')
    return render(request,'emission_checker_industry_Template/e1_login.html')



def home_industry(request):
    return render(request,'emission_checker_industry_Template/emission_check_industry_home.html')



def emission_check_industry(request):
    if request.method == 'POST':
        petrol = request.POST ['petrol']
        diesel = request.POST ['diesel']
        gas = request.POST ['gas']
        electricity = request.POST ['electricity']
        emission_calculate_industry(petrol=petrol, diesel=diesel, gas=gas, electricity=electricity).save()
        messages.info(request, 'Information submitted!!!')
        return redirect('/emission_check_industry/')
    else:
        return render(request,'emission_checker_industry_Template/emission_check_industry.html')




def view_emission_calculate_industry(request):
    data = emission_calculate_industry.objects.all()
    return render(request,'emission_checker_industry_Template/data_view_industry.html',{'data':data})



def total_emission_industry(request,id):
    get = emission_calculate_industry.objects.get(id=id)
    get.emission_calculate=True
    get.save()
    r = get.id
    a = get.petrol
    b = get.diesel
    c = get.gas
    h = get.electricity
    i = (float(a)*2.33+float(b)*2.68+float(c)*2.68+float(h)*0.90)
    get.total_emission_industry = i
    print(i)
    st = emission_calculate_industry.objects.filter(id=r).update(Total_emission=i)
    messages.info(request, 'Sent to admin and get approve for analyse process!!!')
    return redirect('/view_emission_calculate_industry/')



def emission_logout(request):
    if 'admin' in request.session:
        request.session.pop('management', None)
        messages.success(request, 'session logged out')
        return redirect('/')
    else:
        return redirect('/')




def industryindex(request):
    return render(request, 'emission_checker_industry_Template/industryindex.html')



def industrysave(request):
    if request.method=='POST':
        name = request.POST['name']
        address = request.POST['address']
        # date = request.POST['date']
        people_working = request.POST['people_working']
        type_industry = request.POST['type_industry']
        region = request.POST['region']
        indusdatail( name=name, address=address, people_working=people_working , type_industry=type_industry, region=region).save()
        messages.info(request, 'Industry details saved')
        return redirect('/industryindex/')
    else:
        return render(request, 'emission_checker_industry_Template/industryindex.html')




def industry_update(request):
    key = indusdatail.objects.all()
    return render(request, 'emission_checker_industry_Template/industry_update.html',{'key': key})



def deletein(request, id):
    member = indusdatail.objects.get(id=id)
    member.delete()
    messages.info(request, 'Deleted successfully!!!')
    return redirect('/industry_update/')



def updatein(request, id):
    value = indusdatail.objects.get(id=id)
    if request.method == 'POST':
        value.name = request.POST.get('name')
        value.address = request.POST.get('address')
        value.date = request.POST.get('date')
        value.people_working = request.POST.get('people_working')
        value.type_industry = request.POST.get('type_industry')
        value.region = request.POST.get('region')
        value.save()
        messages.info(request, 'Updated successfully')
        return redirect('/industry_update/')
    return render(request, 'emission_checker_industry_Template/industrytemp.html', {'value': value})




def industrytemp(request):
    return render(request, 'emission_checker_industry_Template/industrytemp.html')