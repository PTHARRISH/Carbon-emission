from django.contrib import messages
from django.shortcuts import render, redirect
from emission_check.models import emission_calculate
from emission_checker_industry.models import emission_calculate_industry
from .models import admin_calcu
import warnings

warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt, seaborn as sns
import warnings

warnings.filterwarnings('ignore')
import pandas as pd

from django.shortcuts import render


def pie_chart(request):
    labels = []
    data = []
    queryset = emission_calculate.objects.order_by('total emission')[:5]
    for emission in queryset:
        labels.append(emission.petrol)
        labels.append(emission.diesel)
        labels.append(emission.gas)
        labels.append(emission.taxi)
        labels.append(emission.localbus)
        labels.append(emission.train)
        labels.append(emission.lpg_cyclinder)
        labels.append(emission.electricity)
        data.append(emission.emission_calculate)
    return render(request, 'inde.html', {'labels': labels, 'data': data, })


def inde(request):
    return render(request, 'management_admin_Template/inde.html')


def admin_home_index(request):
    return render(request, 'index.html')


def m_login(request):
    return render(request, 'management_admin_Template/m_login.html')


def admin_homepage(request):
    return render(request, 'management_admin_Template/admin_homepage.html')


def admin_login(request):
    if request.method == "POST":
        Email = request.POST["Email"]
        Password = request.POST["Password"]
        # print(email)
        if Email == "admin@gmail.com" and Password == "admin":
            # print(email)
            request.session['admin'] = "admin@gmail.com"
            messages.info(request, "Admin login successfully!!!")
            return render(request, 'management_admin_Template/admin_homepage.html')
        elif Email != "admin@gmail.com":
            messages.error(request, "Wrong Mail id")
            return render(request, 'management_admin_Template/m_login.html')
        elif Password != "admin":
            messages.error(request, "wrong password")
            return render(request, 'management_admin_Template/m_login.html')
        else:
            return render(request, 'management_admin_Template/m_login.html')
    return render(request, 'management_admin_Template/m_login.html')



def admin_logout(request):
    if 'admin' in request.session:
        request.session.pop('management', None)
        messages.success(request, 'session logged out')
        return redirect('/')
    else:
        return redirect('/')


def basic_calc(request):
    return render(request, 'management_admin_Template/basic_calc.html')


def process_admin(request):
    return render(request, 'management_admin_Template/process_admin.html')


def admincalcu_save(request):
    if request.method == 'POST':
        petrol = request.POST['petrol']
        diesel = request.POST['diesel']
        gas = request.POST['gas']
        taxi = request.POST['taxi']
        localbus = request.POST['localbus']
        train = request.POST['train']
        lpg_cyclinder = request.POST['lpg_cyclinder']
        electricity = request.POST['electricity']
        admin_calcu(petrol=petrol, diesel=diesel, gas=gas, taxi=taxi, localbus=localbus, train=train,
                    lpg_cyclinder=lpg_cyclinder, electricity=electricity).save()
        return redirect('/admin_homepage/')
    else:
        return render(request, 'management_admin_Template/admin_homepage.html')


def admin_view(request):
    data = admin_calcu.objects.all()
    return render(request, 'management_admin_Template/admin_view.html', {'data': data})


def calc_emission(request, id):
    get = admin_calcu.objects.get(id=id)
    get.emission_calculate = True
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
    i = (float(a) * 2.33 + float(b) * 2.68 + float(c) * 2.68 + float(d) * 0.31 + float(e) * 0.05 + float(
        f) * 0.05 + float(g) * 42.50 + float(h) * 0.90)
    get.total_emission = i
    print(i)
    st = admin_calcu.objects.filter(id=r).update(Total_emission=i)
    return redirect('/admin_view/')


def data_table_admin(request):
    return render(request, 'management_admin_Template/data_table _admin.html')


def data_table_home(request):
    data = emission_calculate.objects.filter(send_to_analyse=False)
    return render(request, 'management_admin_Template/data_table_home.html', {'data': data})


def send_analyse(request, id):
    data = emission_calculate.objects.get(id=id)
    data.send_to_analyse = True
    data.save()
    messages.success(request, 'Home data Successfully forwarded to analyse process!!!')
    return redirect('/data_table_home/')


def data_table_industry(request):
    data = emission_calculate_industry.objects.filter(send_to_analyse=False)
    return render(request, 'management_admin_Template/data_table_industry.html', {'data': data})


def send_analyse_industry(request, id):
    data = emission_calculate_industry.objects.get(id=id)
    data.send_to_analyse = True
    data.save()
    messages.success(request, ' Industry data Successfully forwarded to analyse process!!!')
    return redirect('/data_table_industry/')


def total_emission_home(request, id):
    get = emission_calculate.objects.get(id=id)
    get.emission_calculate = True
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
    i = (float(a) * 2.33 + float(b) * 2.68 + float(c) * 2.68 + float(d) * 0.31 + float(e) * 0.05 + float(
        f) * 0.05 + float(g) * 42.50 + float(h) * 0.90)
    get.total_emission = i
    print(i)
    st = emission_calculate.objects.filter(id=r).update(Total_emission=i)
    return redirect('/data_table_home/')


def total_emission_industry(request, id):
    get = emission_calculate_industry.objects.get(id=id)
    get.emission_calculate = True
    get.save()
    r = get.id
    a = get.petrol
    b = get.diesel
    c = get.gas
    h = get.electricity
    i = (float(a) * 2.33 + float(b) * 2.68 + float(c) * 2.68 + float(h) * 0.90)
    get.total_emission_industry = i
    print(i)
    st = emission_calculate_industry.objects.filter(id=r).update(Total_emission=i)
    return redirect('/data_table_industry/')


def report(request):
    return render(request, "management_admin_Template/report.html")


x = pd.read_csv('test.csv')


# def graph1(request):
#     sns.distplot(x['total emission'])
#     plt.show()
#     messages.info(request, "View the heatmap")
#     return render(request, 'management_admin_Template/report.html')
#
#
# def graph2(request):
#     plt.figure(figsize=(16,10))
#     x['type of client'].value_counts().plot.pie()
#     plt.show()
#     messages.info(request, "View the heatmap")
#     return redirect('/graph2/')
# #
#
# def graph3(request):
#     plt.figure(figsize=(16,10))
#     x['total emission'].value_counts(normalize=True).plot.bar()
#     plt.show()
#     messages.info(request, "View the heatmap")
#     return redirect('/graph3/')


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
#
#
# def report(request):
#     return render(request, 'management_admin_Template/report.html')
#
#
# a = pd.read_csv('test.csv')
# print(a.head())
#
#
# def graph1(request):
#     a.Fertilizer_Name.value_counts(normalize=True).plot.bar()
#     plt.show()
#     return redirect('/graph1/')


x = pd.read_csv('test.csv')


def graph_1(request):
    x.plot.scatter(x='type_of_client', y='total_emission')
    plt.title("HOME AND INDUSTRY EMISSION COMPARISION")
    plt.show()
    return render(request, 'management_admin_Template/report.html')



def graph_2(request):
    x.total_emission.value_counts().plot.bar()
    plt.title("TOTAL EMISSION PER MONTH")
    plt.show()
    return render(request, 'management_admin_Template/report.html')


def graph_3(request):
    x['total_emission'].value_counts().plot.pie()
    plt.title("Prducts used on emission")
    plt.show()
    return render(request, 'management_admin_Template/report.html')





