# -*- encoding: utf-8 -*-

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages

from apps.authentication.forms import SignUpForm
from django.db.models import Avg, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import StudentsForm, StudentsSearchForm, UploadContactForm,PredictForm
from .models import DataStudents
# Plotgraph
from .plotgraph import dashboard_graph
from .plotgraph import pie_chart
# CSV
import csv, io
# JSON
import json
# Predict
from pandas import DataFrame
from .sklearn import Model5, predict, Inverse,DataTEST
from sklearn import preprocessing


@login_required(login_url="/login/")
def index(request):
    sta = 'invisible'
    form = StudentsSearchForm(request.POST or None)
    status = DataStudents.objects.order_by('s_status').values(
        's_status').distinct()
    DD = DataStudents.objects.values('s_status').annotate(
        total=Count('s_id')).order_by('-total')
    x = []
    y = []
    for data in DD:
        x.append(data['s_status'])
        y.append(data['total'])
    graph1 = dashboard_graph(x, y)
    graph3 = pie_chart(x, y)
    count = 0
    countdata = 0
    for datay in y:
        countdata += datay
    context = {
        'status': DD,
        'count': count,
        'graph1': graph1,
        'graph3': graph3,
        'countdata':countdata
    }

    if request.method == 'POST':
        Status = ''
        sta = 'visible'
        if 'ไม่มีสิทธิ์สัมภาษณ์' in request.POST:
            Status = 'ไม่มีสิทธิ์สัมภาษณ์'
        elif 'ไม่มาสัมภาษณ์' in request.POST:
            Status = 'ไม่มาสัมภาษณ์'
        elif 'ผ่านแต่ไม่ชำระเงิน' in request.POST:
            Status = 'ผ่านแต่ไม่ชำระเงิน'
        elif 'ชำระเงินเรียบร้อย' in request.POST:
            Status = 'ชำระเงินเรียบร้อย'
        queryset = DataStudents.objects.filter(s_status__icontains=Status)
        count = len(queryset)
        graph2 = dashboard_graph(Status, count)
        context = {
            "queryset": queryset,
            'status': status,
            'Status': Status,
            'count': count,
            'graph1': graph1,
            'graph2': graph2,
            'sta': sta
        }
    # context = {'segment': 'index'}

    # html_template = loader.get_template('home/index.html')
    # return HttpResponse(html_template.render(context, request))
    return render(request, "home/index.html", context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

# register
def register(response):
    if response.method == "POST":
        form = SignUpForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("dashboardView")
    else:
        form = SignUpForm()
    return render(response, "accounts/register.html", {"form": form})


def dashboardView(request):
    sta = 'invisible'
    form = StudentsSearchForm(request.POST or None)
    status = DataStudents.objects.order_by('s_status').values(
        's_status').distinct()
    DD = DataStudents.objects.values('s_status').annotate(
        total=Count('s_id')).order_by('-total')
    x = []
    y = []
    for data in DD:
        x.append(data['s_status'])
        y.append(data['total'])
    graph1 = dashboard_graph(x, y)
    graph3 = pie_chart(x, y)
    count = 0
    countdata = 0
    for datay in y:
        countdata += datay
    context = {
        'status': DD,
        'count': count,
        'graph1': graph1,
        'graph3': graph3,
        'countdata':countdata
    }

    if request.method == 'POST':
        Status = ''
        sta = 'visible'
        if 'ไม่มีสิทธิ์สัมภาษณ์' in request.POST:
            Status = 'ไม่มีสิทธิ์สัมภาษณ์'
        elif 'ไม่มาสัมภาษณ์' in request.POST:
            Status = 'ไม่มาสัมภาษณ์'
        elif 'ผ่านแต่ไม่ชำระเงิน' in request.POST:
            Status = 'ผ่านแต่ไม่ชำระเงิน'
        elif 'ชำระเงินเรียบร้อย' in request.POST:
            Status = 'ชำระเงินเรียบร้อย'
        queryset = DataStudents.objects.filter(s_status__icontains=Status)
        count = len(queryset)
        graph2 = dashboard_graph(Status, count)
        context = {
            "queryset": queryset,
            'status': status,
            'Status': Status,
            'count': count,
            'graph1': graph1,
            'graph2': graph2,
            'sta': sta
        }
    return render(request, "home/dashboard.html", context)


def student_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentsForm()
        else:
            data = DataStudents.objects.get(s_id=id)
            form = StudentsForm(instance=data)
        return render(request, "home/add-data-student.html", {'form': form})

    else:
        if id == 0:
            form = StudentsForm(request.POST)
        else:
            data = DataStudents.objects.get(s_id=id)
            form = StudentsForm(request.POST, instance=data)

        if form.is_valid():
            form.save()
        return redirect('form_list')


def student_delete(request, id):
    data = DataStudents.objects.get(s_id=id)
    data.delete()
    return redirect('form_list')

def student_show(request):
    queryset = DataStudents.objects.all().order_by('s_id')
    context = {
        "queryset": queryset,
    }
    return render(request, "home/tables-bootstrap-tables.html", context)

# school
def school(request):
    return render(request, 'home/transactions.html')

# Upload
def uploadcsv(request):
    if request.method == "POST":
        if request.FILES:
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'กรุณาเลือกไฟล์ CSV')
                return render(request, 'home/uploadcsv.html')
            else:
                messages.success(request, 'สำเร็จ')
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                for columns in csv.reader(io_string,
                                          delimiter=',',
                                          quotechar='|'):
                    _, created = DataStudents.objects.update_or_create(
                        s_id=columns[0],
                        s_code=columns[1],
                        s_prefix=columns[2],
                        s_status=columns[3],
                        s_Applicant_type=columns[4],
                        s_Faculty_Code=columns[5],
                        s_Field_of_study=columns[6],
                        s_Year=columns[7],
                        s_Thai_Grade=columns[8],
                        s_Math_Grade=columns[9],
                        s_Science_Grade=columns[10],
                        s_Social_studies_Grades=columns[11],
                        s_Health_education_Grades=columns[12],
                        s_Art_Grade=columns[13],
                        s_Career_Grade=columns[14],
                        s_Foreign_language_Grade=columns[15],
                        s_GPAX=columns[16],
                        s_School_Name=columns[17],
                        s_Province_Name=columns[18],
                    )
        else:
            messages.error(request, 'เลือกไฟล์ CSV')
            return render(request, 'home/uploadcsv.html')

        return redirect('dashboardView')
    else:
        return render(request, 'home/uploadcsv.html')

# json
def json(request):
    data = list(DataStudents.objects.values())
    return JsonResponse(data, safe=False)

def admissions(request):
    return render(request, 'home/admissions.html')

def viewdatastudent(request):
    DD = DataStudents.objects.values('s_status').annotate(
        total=Count('s_id')).order_by('-total')

    PASS = 0
    NOTPASS = 0
    
    for status in DD:
        if status['s_status'] == 'ชำระเงินเรียบร้อย':
            PASS += status['total']
        elif status['s_status'] == 'ผ่านแต่ไม่ชำระเงิน':
            NOTPASS += status['total']
        elif status['s_status'] == 'ไม่มาสัมภาษณ์':
            NOTPASS += status['total']
        elif status['s_status'] == "ไม่มีสิทธิ์สัมภาษณ์":
            NOTPASS += status['total']
    sums = PASS + NOTPASS
    # ชำระเงินเรียบร้อย
    passper = round((PASS / sums) * 100, 2)
    # ผ่านแต่ไม่ชำระเงิน,ไม่มาสัมภาษณ์,ไม่มีสิทธิ์สัมภาษณ์
    nopassper = round((NOTPASS / sums) * 100, 2)

    context = {'passper': passper, 'nopassper': nopassper, 'NOTPASS': NOTPASS, 'PASS': PASS, 'sums': sums}
    return render(request, "home/datastudent.html", context)
# Predict
def Predict(request):
    sta = 'invisible'
    df = DataFrame(DataStudents.objects.all().values())
    columns = [
        's_prefix', 's_Thai_Grade', 's_Math_Grade', 's_Science_Grade',
        's_Social_studies_Grades', 's_Health_education_Grades', 's_Art_Grade',
        's_Career_Grade', 's_Foreign_language_Grade', 's_GPAX',
        's_School_Name', 's_Province_Name'
    ]
    data = df.loc[:, columns]
    dropdata = data[data.s_prefix != 'Mr.']
    data = dropdata.reset_index(drop=True)
    dropdata = data[data.s_prefix != 'พลทหาร']
    data = dropdata.reset_index(drop=True)
    dropdata = data[data.s_prefix != 'สามเณร.']
    data = dropdata.reset_index(drop=True)
    status = preprocessing.LabelEncoder()

    # print(data)
    prefix = preprocessing.LabelEncoder()
    prefix = preprocessing.LabelEncoder()
    Thai = preprocessing.LabelEncoder()
    Math = preprocessing.LabelEncoder()
    Science = preprocessing.LabelEncoder()
    Social = preprocessing.LabelEncoder()
    Health = preprocessing.LabelEncoder()
    Art = preprocessing.LabelEncoder()
    Career = preprocessing.LabelEncoder()
    Foreign = preprocessing.LabelEncoder()
    GPAX = preprocessing.LabelEncoder()
    School = preprocessing.LabelEncoder()
    Province = preprocessing.LabelEncoder()

    status.fit(df['s_status'])
    list(status.classes_)
    # print(list(status.classes_))
    status.transform(df['s_status'])
    list(status.inverse_transform([1]))
    

    data.s_prefix = prefix.fit_transform(data['s_prefix'].astype(str))
    df.s_Thai_Grade = Thai.fit_transform(df['s_Thai_Grade'].astype(float))
    df.s_Math_Grade = Math.fit_transform(df['s_Math_Grade'].astype(float))
    df.s_Science_Grade = Science.fit_transform(
        df['s_Science_Grade'].astype(float))
    df.s_Social_studies_Grades = Social.fit_transform(
        df['s_Social_studies_Grades'].astype(float))
    df.s_Health_education_Grades = Health.fit_transform(
        df['s_Health_education_Grades'].astype(float))
    df.s_Art_Grade = Art.fit_transform(df['s_Art_Grade'].astype(float))
    df.s_Career_Grade = Career.fit_transform(df['s_Career_Grade'].astype(float))
    df.s_Foreign_language_Grade = Foreign.fit_transform(
        df['s_Foreign_language_Grade'].astype(float))
    df.s_GPAX = GPAX.fit_transform(df['s_GPAX'].astype(float))
    df.s_School_Name = School.fit_transform(df['s_School_Name'].astype(str))
    df.s_Province_Name = Province.fit_transform(
        df['s_Province_Name'].astype(str))

    # print('prefix',list(prefix.classes_))
    # print('s_Thai_Grade',list(Thai.classes_))
    # # print('Province',list(Province.classes_))
    # print('Province',list(GPAX.classes_))

    # for xx in list(Thai.classes_):
    # Index = list(prefix.classes_).index('นาย')
    # print(Index)

        
            

    # print(list(prefix.inverse_transform([0])))
    # print(list(Thai.inverse_transform([2])))
    # print(list(Math.inverse_transform([4])))
    # print(list(Science.inverse_transform([3])))
    # print(list(Social.inverse_transform([1])))
    # print(list(Health.inverse_transform([0])))
    # print(list(Art.inverse_transform([0])))
    # print(list(Career.inverse_transform([0])))
    # print(list(Foreign.inverse_transform([2])))
    # print(list(GPAX.inverse_transform([65])))
    # print(list(School.inverse_transform([10])))
    # print(list(Province.inverse_transform([33])))



    form = PredictForm()
    number = 5
    model = 'Naive_Bayes'
    if request.method == "POST":
        # pre2 = [1, 1, 2, 1, 1, 0, 0, 2, 1, 128, 463, 48]

        test = DataTEST(number)
        Xtrain5, Xtest5, ytrain5, ytest5, sta, data2 = test
        pre = []
        # m = Model5(number, pre, Xtrain5, Xtest5, ytrain5, ytest5)
        form = PredictForm(request.POST)
        if form.is_valid():
            listprefix = list(prefix.classes_)
            listThai = list(Thai.classes_)
            listMath = list(Math.classes_)
            listScience = list(Science.classes_)
            listSocial = list(Social.classes_)
            listHealth = list(Health.classes_)
            listArt = list(Art.classes_)
            listCareer = list(Career.classes_)
            listForeign = list(Foreign.classes_)
            listGPAX = list(GPAX.classes_)
            listSchool = list(School.classes_)
            listProvince = list(Province.classes_)
            # FORM
            prefix = form.cleaned_data['s_prefix']
            pre.append(listprefix.index(prefix))

            Thai_Grade = form.cleaned_data['s_Thai_Grade']
            pre.append(listThai.index(Thai_Grade))

            Math_Grade = form.cleaned_data['s_Math_Grade']
            pre.append(listMath.index(Math_Grade))

            Science_Grade = form.cleaned_data['s_Science_Grade']
            pre.append(listScience.index(Science_Grade))

            Social_studies_Grades =form.cleaned_data['s_Social_studies_Grades']
            pre.append(listSocial.index(Social_studies_Grades))

            Health_education_Grades = form.cleaned_data['s_Health_education_Grades']
            pre.append(listHealth.index(Health_education_Grades))

            Art_Grade = form.cleaned_data['s_Art_Grade']
            pre.append(listArt.index(Art_Grade))

            Career_Grade = form.cleaned_data['s_Career_Grade']
            pre.append(listCareer.index(Career_Grade))

            Foreign_language_Grade = form.cleaned_data['s_Foreign_language_Grade']
            pre.append(listForeign.index(Foreign_language_Grade))

            GPAX = form.cleaned_data['s_GPAX']
            pre.append(listGPAX.index(GPAX))

            School_Name = form.cleaned_data['s_School_Name']
            pre.append(listSchool.index(School_Name))

            Province_Name = form.cleaned_data['s_Province_Name']
            pre.append(listProvince.index(Province_Name))

            # print(pre)
            
        predicts = predict(pre, Xtrain5, Xtest5, ytrain5, ytest5)
        sta = 'invisible'
        # print('predicts',predicts)
        context = {
            'form': form,
            'pre': pre,
            'predicts':predicts,
            'sta':sta
            }
        return render(request, 'home/Predict.html', context)

    context = {
        'form': form,
        'sta':sta

    }
    return render(request, 'home/Predict.html', context)