from django.shortcuts import render, redirect
from django.contrib import messages
from emission_check.models import emission_calculate
from emission_checker_industry.models import emission_calculate_industry
from .models import data_analyst_register
from .models import data_analyst_data
from django.contrib import messages
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import warnings

# Create your views here.



def data_home_index(request):
    return render(request,'index.html')



def data_index(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password = request.POST['Password']
        try:
            r = data_analyst_register.objects.get(Email=Email, Password=Password)
            request.session['data'] = r.Email
            if r is not None:
                messages.info(request, 'Welcome To Data Analyst Page!!!')
                return redirect('/datapage/')
        except data_analyst_register.DoesNotExist as e:
            messages.info(request, 'Name does not exists')
            return redirect('/data_index/')
    return render(request,'data_analyst_Template/data_index.html')



def registration_data_analyst(request):
    if request.method=='POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Phone_number = request.POST['Phone_number']
        Password = request.POST['Password']
        Address = request.POST['Address']
        data_analyst_register(Name=Name, Email=Email, Phone_number=Phone_number, Password=Password,Address=Address).save()
        messages.info(request, 'Registration is SUccess!!!')
        return redirect('/data_index/')
    else:
        return render(request, 'data_analyst_Template/registration.html')



def datapage(request):
    return render(request,'data_analyst_Template/datapage.html')




def  data_analyst_data_save(request):
    if request.method == 'POST':
        Name_user = request.POST['Name_user']
        petrol = request.POST['petrol']
        diesel = request.POST['diesel']
        gas = request.POST['gas']
        taxi = request.POST['taxi']
        localbus = request.POST['localbus']
        train = request.POST['train']
        lpg_cyclinder = request.POST['lpg_cyclinder']
        electricity = request.POST['electricity']
        data_analyst_data(Name_user=Name_user,petrol=petrol, diesel=diesel, gas=gas,taxi=taxi,localbus=localbus,train=train,
                               lpg_cyclinder=lpg_cyclinder,electricity=electricity).save()
        messages.info(request, 'Data submitted!!!')
        return redirect('/data_analyst_data_save/')
    else:
        return render(request,'data_analyst_Template/data_homepage_traindata.html')




def dataset_view_industry(request):
    data = data_analyst_data.objects.all()
    messages.info(request, 'calculating the emission and forward to analyse')
    return render(request,'data_analyst_Template/data_analyst_view.html',{'data':data})



def total_emission_datamatch(request,id):
    get = data_analyst_data.objects.get(id=id)
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
    get.total_emission_datamatch = i
    print(i)
    st = data_analyst_data.objects.filter(id=r).update(Total_emission=i)
    messages.info(request, 'Calculated Data Sent to Next Process!!!')
    return redirect('/dataset_view_industry/')



def analysing_data_home(request):
    x = emission_calculate.objects.all()
    y = data_analyst_data.objects.all()
    for i in y:
        if i.Name_user=='home':
              for j in x:
                  if j.Total_emission < i.Total_emission:
                      print("emission is low")
                      return render(request, 'data_analyst_Template/dummy.html')
                  else :
                      return  render(request,'data_analyst_Template/Hemission.html')




def Hemission(request):
    return render(request, 'data_analyst_Template/Hemission.html')



def dummy(request):
    return render(request, 'data_analyst_Template/dummy.html')



def analysing_data_industry(request):
    x = emission_calculate_industry.objects.all()
    y = data_analyst_data.objects.all()
    for i in y:
        if i.Name_user=='Industry':
              for j in x:
                  if j.Total_emission < i.Total_emission:
                      print("emission is low")
                      return render(request, 'data_analyst_Template/dummy.html')
                  else :
                      print("emission is high")
                      return  render(request,'data_analyst_Template/Hemission.html')



def data_logout(request):
    if 'admin' in request.session:
        request.session.pop('management', None)
        messages.success(request, 'session logged out')
        return redirect('/')
    else:
        return redirect('/')



def view_home_analyse(request):
    data = emission_calculate.objects.all()
    data1 = emission_calculate_industry.objects.all()
    return render(request, 'data_analyst_Template/Home_analyse.html',{'data':data,'data1':data1})



def start_process(request):
    messages.info(request,'Forwarded To Analyse')
    return render(request, 'data_analyst_Template/Home_analyse.html' )



def analyse_process(request):
    data = data_analyst_data.objects.all()
    return render(request, 'data_analyst_Template/analyse_process.html',{'data':data})



def algorithm(datas,r):
    data = pd.read_csv('test.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]
    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)
    model = DecisionTreeClassifier()
    model.fit(data_x, data_y)
    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    print(12334455)
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]



def analyst_calculate(request,id):
    get = data_analyst_data.objects.get(id=id)
    get.analyse=True
    get.save()
    inputvar = []
    r = get.id
    home = get.Name_user
    a = get.petrol
    b = get.diesel
    c = get.gas
    d = get.taxi
    e = get.localbus
    f = get.train
    g = get.lpg_cyclinder
    h = get.electricity
    k=get.Total_emission
    inputvar.append(home)
    inputvar.append(a)
    inputvar.append(b)
    inputvar.append(c)
    inputvar.append(d)
    inputvar.append(e)
    inputvar.append(f)
    inputvar.append(g)
    inputvar.append(h)
    inputvar.append(k)
    print('input:', inputvar)
    o = algorithm(inputvar, r)
    print('OUTPUT:', o)
    st = data_analyst_data.objects.filter(id=r).update(output=o)
    return redirect('/analyse_process/')






