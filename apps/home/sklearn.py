from django.db.models.expressions import F
from pandas import DataFrame
from .models import DataStudents

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import re
import collections
ledata = LabelEncoder()


def FITTRANSFORM(data, key):
    # print("DATA1",data)
    # s_prefix = ledata.fit_transform(data['s_prefix'].astype(str))
    # s_Thai_Grade = ledata.fit_transform(data['s_Thai_Grade'].astype(str))
    # s_Math_Grade = ledata.fit_transform(data['s_Math_Grade'].astype(str))
    # s_Science_Grade = ledata.fit_transform(data['s_Science_Grade'].astype(str))
    # s_Social_studies_Grades = ledata.fit_transform(data['s_Social_studies_Grades'].astype(str))
    # s_Health_education_Grades = ledata.fit_transform(data['s_Health_education_Grades'].astype(str))
    # s_Art_Grade = ledata.fit_transform(data['s_Art_Grade'].astype(str))
    # s_Career_Grade = ledata.fit_transform(data['s_Career_Grade'].astype(str))
    # s_Foreign_language_Grade = ledata.fit_transform(data['s_Foreign_language_Grade'].astype(str))
    # s_GPAX = ledata.fit_transform(data['s_GPAX'].astype(str))
    # s_School_Name = ledata.fit_transform(data['s_School_Name'].astype(str))
    # s_Province_Name = ledata.fit_transform(data['s_Province_Name'].astype(str))

    s_prefix = ledata.fit_transform(data.s_prefix.astype(str))
    s_Thai_Grade = ledata.fit_transform(data.s_Thai_Grade.astype(str))
    s_Math_Grade = ledata.fit_transform(data.s_Math_Grade.astype(str))
    s_Science_Grade = ledata.fit_transform(data.s_Science_Grade.astype(str))
    s_Social_studies_Grades = ledata.fit_transform(
        data.s_Social_studies_Grades.astype(str))
    s_Health_education_Grades = ledata.fit_transform(
        data.s_Health_education_Grades.astype(str))
    s_Art_Grade = ledata.fit_transform(data.s_Art_Grade.astype(str))
    s_Career_Grade = ledata.fit_transform(data.s_Career_Grade.astype(str))
    s_Foreign_language_Grade = ledata.fit_transform(
        data.s_Foreign_language_Grade.astype(str))
    s_GPAX = ledata.fit_transform(data.s_GPAX.astype(str))
    s_School_Name = ledata.fit_transform(data.s_School_Name.astype(str))
    s_Province_Name = ledata.fit_transform(data.s_Province_Name.astype(str))

    # data.s_prefix = s_prefix
    # data.s_Thai_Grade = s_Thai_Grade
    # data.s_Math_Grade = s_Math_Grade
    # data.s_Science_Grade = s_Science_Grade
    # data.s_Social_studies_Grades = s_Social_studies_Grades
    # data.s_Health_education_Grades = s_Health_education_Grades
    # data.s_Art_Grade = s_Art_Grade
    # data.s_Career_Grade = s_Career_Grade
    # data.s_Foreign_language_Grade = s_Foreign_language_Grade
    # data.s_GPAX = s_GPAX
    # data.s_School_Name = s_School_Name
    # data.s_Province_Name = s_Province_Name
    # if key == 'fit':
    #     print('fit')
    #     s_prefix = ledata.fit_transform(data['s_prefix'].astype(str))
    #     data.s_prefix = s_prefix
    #     s_Thai_Grade = ledata.fit_transform(data['s_Thai_Grade'].astype(str))
    #     data.s_Thai_Grade = s_Thai_Grade
    #     s_Math_Grade = ledata.fit_transform(data['s_Math_Grade'].astype(str))
    #     data.s_Math_Grade = s_Math_Grade
    #     s_Science_Grade = ledata.fit_transform(data['s_Science_Grade'].astype(str))
    #     data.s_Science_Grade = s_Science_Grade
    #     s_Social_studies_Grades = ledata.fit_transform(data['s_Social_studies_Grades'].astype(str))
    #     data.s_Social_studies_Grades = s_Social_studies_Grades
    #     s_Health_education_Grades = ledata.fit_transform(data['s_Health_education_Grades'].astype(str))
    #     data.s_Health_education_Grades = s_Health_education_Grades
    #     s_Art_Grade = ledata.fit_transform(data['s_Art_Grade'].astype(str))
    #     data.s_Art_Grade = s_Art_Grade
    #     s_Career_Grade = ledata.fit_transform(data['s_Career_Grade'].astype(str))
    #     data.s_Career_Grade = s_Career_Grade
    #     s_Foreign_language_Grade = ledata.fit_transform(data['s_Foreign_language_Grade'].astype(str))
    #     data.s_Foreign_language_Grade = s_Foreign_language_Grade
    #     s_GPAX = ledata.fit_transform(data['s_GPAX'].astype(str))
    #     data.s_GPAX = s_GPAX
    #     s_School_Name = ledata.fit_transform(data['s_School_Name'].astype(str))
    #     data.s_School_Name = s_School_Name
    #     s_Province_Name = ledata.fit_transform(data['s_Province_Name'].astype(str))
    #     data.s_Province_Name = s_Province_Name
    #     print(data)

    if key == 'inverse':
        print('inverse')
        # print(ledata.inverse_transform(s_prefix))
        # print(ledata.inverse_transform(s_Thai_Grade))
        # data.s_prefix = ledata.inverse_transform(s_prefix)
        # data.s_Thai_Grade = ledata.inverse_transform(s_Thai_Grade)
        # data.s_Math_Grade = ledata.inverse_transform(s_Math_Grade)
        # data.s_Science_Grade = ledata.inverse_transform(s_Science_Grade)
        # data.s_Social_studies_Grades = ledata.inverse_transform(s_Social_studies_Grades)
        # data.s_Health_education_Grades = ledata.inverse_transform(s_Health_education_Grades)
        # data.s_Art_Grade= ledata.inverse_transform(s_Art_Grade)
        # data.s_Career_Grade = ledata.inverse_transform(s_Career_Grade)
        # data.s_Foreign_language_Grade = ledata.inverse_transform(s_Foreign_language_Grade)
        # data.s_GPAX = ledata.inverse_transform(s_GPAX)
        # data.s_School_Name = ledata.inverse_transform(s_School_Name)
        # data.s_Province_Name = ledata.inverse_transform(s_Province_Name)

    # InverseTransform(data)
    # return data


def InverseTransform(data):
    # data.s_prefix = ledata.inverse_transform(data.s_prefix)
    # data.s_Thai_Grade = ledata.inverse_transform(data.s_Thai_Grade)
    # data.s_Math_Grade = ledata.inverse_transform(data.s_Math_Grade)
    # data.s_Science_Grade = ledata.inverse_transform(data.s_Science_Grade)
    # data.s_Social_studies_Grades = ledata.inverse_transform(data.s_Social_studies_Grades)
    # data.s_Health_education_Grades = ledata.inverse_transform(data.s_Health_education_Grades)
    # data.s_Art_Grade= ledata.inverse_transform(data.s_Art_Grade)
    # data.s_Career_Grade = ledata.inverse_transform(data.s_Career_Grade)
    # data.s_Foreign_language_Grade = ledata.inverse_transform(data.s_Foreign_language_Grade)
    # data.s_GPAX = ledata.inverse_transform(data.s_GPAX)
    # data.s_School_Name = ledata.inverse_transform(data.s_School_Name)
    # data.s_Province_Name = ledata.inverse_transform(data.s_Province_Name)
    print('DATA2', data)
    # print('Type',type(data))
    # data['s_prefix'] = ledata.inverse_transform(data['s_prefix'])
    # print('data.s_prefix',data.s_prefix)
    # data.s_Thai_Grade = ledata.inverse_transform(data.s_Thai_Grade)
    # data.s_Math_Grade = ledata.inverse_transform(data.s_Math_Grade)
    # data.s_Science_Grade = ledata.inverse_transform(data.s_Science_Grade)
    # data.s_Social_studies_Grades = ledata.inverse_transform(data.s_Social_studies_Grades)
    # data.s_Health_education_Grades = ledata.inverse_transform(data.s_Health_education_Grades)
    # data.s_Art_Grade= ledata.inverse_transform(data.s_Art_Grade)
    # data.s_Career_Grade = ledata.inverse_transform(data.s_Career_Grade)
    # data.s_Foreign_language_Grade = ledata.inverse_transform(data.s_Foreign_language_Grade)
    # data.s_GPAX = ledata.inverse_transform(data.s_GPAX)
    # data.s_School_Name = ledata.inverse_transform(data.s_School_Name)
    # data.s_Province_Name = ledata.inverse_transform(data.s_Province_Name)
    # print('DATA2',data)
    # return data


def Inverse(i, data):
    sta = preprocessing.LabelEncoder()
    status = {}
    # print(data.s_status)
    sta.fit(data.s_status)
    list(sta.classes_)
    # print(list(sta.classes_))
    for i in range(len(sta.classes_)):
        status[i] = sta.classes_[i]
    sta.transform(data.s_status)
    # print(sta.transform(data.s_status))
    # print('status',status)
    # list(sta.inverse_transform([]))
    # print(list(sta.inverse_transform([i])))
    return status


def DataTEST(i):
    df = DataFrame(DataStudents.objects.all().values())
    number = preprocessing.LabelEncoder()

    def convert(data):
        data['s_prefix'] = number.fit_transform(data.s_prefix)
        data['s_status'] = number.fit_transform(data.s_status)
        data['s_Applicant_type'] = number.fit_transform(data.s_Applicant_type)
        data['s_Field_of_study'] = number.fit_transform(data.s_Field_of_study)
        data['s_School_Name'] = number.fit_transform(data.s_School_Name)
        data['s_Province_Name'] = number.fit_transform(data.s_Province_Name)
        return data

    def convert_grade(grade):
        if grade >= 3.50:
            grade = "A"
        elif grade >= 3.00:
            grade = "B"
        elif grade >= 2.50:
            grade = "C"
        elif grade >= 2.00:
            grade = "D"
        elif grade >= 1.50:
            grade = "E"
        elif grade >= 1.00:
            grade = "F"
        elif grade >= 0.00:
            grade = "Fail"
        return grade

    def convertDataGrade(data):
        data['s_prefix'] = number.fit_transform(data.s_prefix)
        data['s_status'] = number.fit_transform(data.s_status)
        data['s_Applicant_type'] = number.fit_transform(data.s_Applicant_type)
        data['s_Field_of_study'] = number.fit_transform(data.s_Field_of_study)
        data['s_School_Name'] = number.fit_transform(data.s_School_Name)
        data['s_Province_Name'] = number.fit_transform(data.s_Province_Name)
        # Grade
        data['s_Thai_Grade'] = number.fit_transform(data.s_Thai_Grade)
        data['s_Math_Grade'] = number.fit_transform(data.s_Math_Grade)
        data['s_Science_Grade'] = number.fit_transform(data.s_Science_Grade)
        data['s_Social_studies_Grades'] = number.fit_transform(
            data.s_Social_studies_Grades)
        data['s_Health_education_Grades'] = number.fit_transform(
            data.s_Health_education_Grades)
        data['s_Art_Grade'] = number.fit_transform(data.s_Art_Grade)
        data['s_Career_Grade'] = number.fit_transform(data.s_Career_Grade)
        data['s_Foreign_language_Grade'] = number.fit_transform(
            data.s_Foreign_language_Grade)
        data['s_GPAX'] = number.fit_transform(data.s_GPAX)
        return data

    if i == 1:
        data = df.copy()
        sta = Inverse(i, data)
        data2 = convert(data)
        x_columns = list(data2.columns)
        #เอา column Status ออก
        x_columns = [
            's_prefix', 's_Thai_Grade', 's_Math_Grade', 's_Science_Grade',
            's_Social_studies_Grades', 's_Health_education_Grades',
            's_Art_Grade', 's_Career_Grade', 's_Foreign_language_Grade',
            's_GPAX', 's_School_Name', 's_Province_Name'
        ]

        x = data2.loc[:, x_columns]
        y = data2.loc[:, ['s_status']]

        print('ข้อมูลเดิม')
        print(len(x), len(y))
        Xtrain1, Xtest1, ytrain1, ytest1 = train_test_split(x,
                                                            y,
                                                            test_size=0.33,
                                                            random_state=0)
        pre = []
        Model5(i,pre, Xtrain1, Xtest1, ytrain1, ytest1)
        return Xtrain1, Xtest1, ytrain1, ytest1, sta, data2
    elif i == 2:
        data = df.copy()
        dropdata = data[data.s_status != 'ไม่มีสิทธิ์สัมภาษณ์']
        data = dropdata.reset_index(drop=True)
        sta = Inverse(i, data)
        number = preprocessing.LabelEncoder()
        data2 = convert(data)
        x_columns = list(data2.columns)
        #เอา column Status ออก
        x_columns = [
            's_prefix', 's_Thai_Grade', 's_Math_Grade', 's_Science_Grade',
            's_Social_studies_Grades', 's_Health_education_Grades',
            's_Art_Grade', 's_Career_Grade', 's_Foreign_language_Grade',
            's_GPAX', 's_School_Name', 's_Province_Name'
        ]

        x = data2.loc[:, x_columns]
        y = data2.loc[:, ['s_status']]
        Xtrain2, Xtest2, ytrain2, ytest2 = train_test_split(x,
                                                            y,
                                                            test_size=0.33,
                                                            random_state=0)

        print('ตัดข้อมูลไม่มีสิทธิ์สัมภาษณ์')
        print(len(x), len(y))
        pre= []
        Model5(i,pre, Xtrain2, Xtest2, ytrain2, ytest2)
        return Xtrain2, Xtest2, ytrain2, ytest2, sta, data2

    elif i == 3:
        data = df.copy()
        # ตัดขอมูล ไม่มีสิทธิ์สัมภาษณ์ ออก
        dropdata = data[data.s_status != 'ไม่มีสิทธิ์สัมภาษณ์']
        data = dropdata.reset_index(drop=True)
        sta = Inverse(i, data)
        #แปลงเกรดทุกวิชา และ Gpax ให้เป็นช่วงข้อมูล แต่แสดงในรูปแบบ A - Fail เพื่อเพิ่มความถี่ในการสร้างโมเดล
        for i in range(len(data.s_Thai_Grade)):
            data.s_Thai_Grade[i] = convert_grade(data.s_Thai_Grade[i])
            data.s_Math_Grade[i] = convert_grade(data.s_Math_Grade[i])
            data.s_Science_Grade[i] = convert_grade(data.s_Science_Grade[i])
            data.s_Social_studies_Grades[i] = convert_grade(
                data.s_Social_studies_Grades[i])
            data.s_Health_education_Grades[i] = convert_grade(
                data.s_Health_education_Grades[i])
            data.s_Art_Grade[i] = convert_grade(data.s_Art_Grade[i])
            data.s_Career_Grade[i] = convert_grade(data.s_Career_Grade[i])
            data.s_Foreign_language_Grade[i] = convert_grade(
                data.s_Foreign_language_Grade[i])
            data.s_GPAX[i] = convert_grade(data.s_GPAX[i])

        number = preprocessing.LabelEncoder()
        data2 = convertDataGrade(data)
        x_columns = list(data2.columns)
        #เอา column Status ออก
        x_columns = [
            's_prefix', 's_Thai_Grade', 's_Math_Grade', 's_Science_Grade',
            's_Social_studies_Grades', 's_Health_education_Grades',
            's_Art_Grade', 's_Career_Grade', 's_Foreign_language_Grade',
            's_GPAX', 's_School_Name', 's_Province_Name'
        ]

        x = data2.loc[:, x_columns]
        y = data2.loc[:, ['s_status']]

        print('ตัดข้อมูลไม่มีสิทธิ์สัมภาษณ์ และ แปลงเกรดทุกวิชา และ Gpax')
        print(len(x), len(y))

        Xtrain3, Xtest3, ytrain3, ytest3 = train_test_split(x,
                                                            y,
                                                            test_size=0.33,
                                                            random_state=0)
        pre = []
        Model5(i,pre, Xtrain3, Xtest3, ytrain3, ytest3)

        return Xtrain3, Xtest3, ytrain3, ytest3, sta, data2

    elif i == 4:
        data = df.copy()
        # ตัดขอมูล ไม่มีสิทธิ์สัมภาษณ์ ออก
        dropdata = data[data.s_status != 'ไม่มีสิทธิ์สัมภาษณ์']
        data = dropdata.reset_index(drop=True)
        #รวม status ผ่านแต่ไม่ชำระเงิน และ ไม่มาสัมภาษณ์ ให้เป็น "ไม่เลือกเรียน"
        count = 0
        for i in range(len(data.s_status)):
            x = re.findall("ไม่", data.s_status[i])
            if (x):
                data.s_status[i] = "ไม่เลือกเรียน"
                count = count + 1
        sta = Inverse(i, data)
        number = preprocessing.LabelEncoder()
        data2 = convertDataGrade(data)
        x_columns = list(data2.columns)
        #เอา column Status ออก
        x_columns = [
            's_prefix', 's_Thai_Grade', 's_Math_Grade', 's_Science_Grade',
            's_Social_studies_Grades', 's_Health_education_Grades',
            's_Art_Grade', 's_Career_Grade', 's_Foreign_language_Grade',
            's_GPAX', 's_School_Name', 's_Province_Name'
        ]

        x = data2.loc[:, x_columns]
        y = data2.loc[:, ['s_status']]

        print(
            'ตัดข้อมูลไม่มีสิทธิ์สัมภาษณ์ รวม status ผ่านแต่ไม่ชำระเงิน และ ไม่มาสัมภาษณ์ ให้เป็น "ไม่เลือกเรียน (ไม่แปลงเกรด)'
        )
        print(len(x), len(y))

        Xtrain4, Xtest4, ytrain4, ytest4 = train_test_split(x,
                                                            y,
                                                            test_size=0.33,
                                                            random_state=0)
        pre = []
        Model5(i, pre, Xtrain4, Xtest4, ytrain4, ytest4)

        return Xtrain4, Xtest4, ytrain4, ytest4, sta, data2

    elif i == 5:
        data = df.copy()
        # ตัดขอมูล ไม่มีสิทธิ์สัมภาษณ์ ออก
        dropdata = data[data.s_status != 'ไม่มีสิทธิ์สัมภาษณ์']
        data = dropdata.reset_index(drop=True)

        #รวม status ผ่านแต่ไม่ชำระเงิน และ ไม่มาสัมภาษณ์ ให้เป็น "ไม่เลือกเรียน"
        count = 0
        for i in range(len(data.s_status)):
            x = re.findall("ไม่", data.s_status[i])
            if (x):
                data.s_status[i] = "ไม่เลือกเรียน"
                count = count + 1
        # print(data)
        # le.fit(data.s_status)
        columns = [
            's_prefix', 's_Thai_Grade', 's_Math_Grade', 's_Science_Grade',
            's_Social_studies_Grades', 's_Health_education_Grades',
            's_Art_Grade', 's_Career_Grade', 's_Foreign_language_Grade',
            's_GPAX', 's_School_Name', 's_Province_Name'
        ]
        # print(data.info())
        # for feat in columns:
        #     data[feat] = le.fit_transform(data[feat].astype(str))

        #แปลงเกรดทุกวิชา และ Gpax ให้เป็นช่วงข้อมูล แต่แสดงในรูปแบบ A - Fail เพื่อเพิ่มความถี่ในการสร้างโมเดล
        for i in range(len(data.s_Thai_Grade)):
            data.s_Thai_Grade[i] = convert_grade(data.s_Thai_Grade[i])
            data.s_Math_Grade[i] = convert_grade(data.s_Math_Grade[i])
            data.s_Science_Grade[i] = convert_grade(data.s_Science_Grade[i])
            data.s_Social_studies_Grades[i] = convert_grade(
                data.s_Social_studies_Grades[i])
            data.s_Health_education_Grades[i] = convert_grade(
                data.s_Health_education_Grades[i])
            data.s_Art_Grade[i] = convert_grade(data.s_Art_Grade[i])
            data.s_Career_Grade[i] = convert_grade(data.s_Career_Grade[i])
            data.s_Foreign_language_Grade[i] = convert_grade(
                data.s_Foreign_language_Grade[i])
            data.s_GPAX[i] = convert_grade(data.s_GPAX[i])

        # sta.fit(data.s_status)
        # list(sta.classes_)
        # # print(list(number2.classes_))
        # sta.transform(data.s_status)
        # list(sta.inverse_transform([1]))
        # print(list(number2.inverse_transform([1])))

        # Inverse(data)
        # keyword = 'inverse'
        # fitdata = FITTRANSFORM(data.loc[:, columns],keyword)
        # testinverts = InverseTransform(fitdata)
        # print('testinverts',testinverts)
        sta = Inverse(i, data)
        data2 = convertDataGrade(data)
        # print(data2)
        x_columns = list(data2.columns)
        #เอา column Status ออก
        x_columns = [
            's_prefix', 's_Thai_Grade', 's_Math_Grade', 's_Science_Grade',
            's_Social_studies_Grades', 's_Health_education_Grades',
            's_Art_Grade', 's_Career_Grade', 's_Foreign_language_Grade',
            's_GPAX', 's_School_Name', 's_Province_Name'
        ]

        x = data2.loc[:, x_columns]
        y = data2.loc[:, ['s_status']]
        print(
            'ตัดข้อมูลไม่มีสิทธิ์สัมภาษณ์ รวม status ผ่านแต่ไม่ชำระเงิน และ ไม่มาสัมภาษณ์ ให้เป็น "ไม่เลือกเรียน (แปลงเกรด)'
        )
        print(len(x), len(y))
        Xtrain5, Xtest5, ytrain5, ytest5 = train_test_split(x,
                                                            y,
                                                            test_size=0.33,
                                                            random_state=0)
        # print(list(le.classes_))
        pre = []
        Model5(i, pre, Xtrain5, Xtest5, ytrain5, ytest5)
        return Xtrain5, Xtest5, ytrain5, ytest5, sta, data2


def RandomForestModel():
    #อัลกอรึทึม RandomForest
    # print("RandomForestClassifier")
    return RandomForestClassifier(n_estimators=1000)


def Naive_BayesModel():
    #อัลกอรึทึม naive_bayes
    # print("naive_bayes")
    return GaussianNB()


def MLPClassifierModel():
    #อัลกอรึทึม multilayer perceptron
    # print("MLPClassifier")
    return MLPClassifier(solver='lbfgs',
                         alpha=1e-5,
                         hidden_layer_sizes=(5, 2),
                         random_state=1)


def SVCModel():
    #อัลกอรึทึม Suppor Vector Machine
    # print("SVC")
    return make_pipeline(StandardScaler(), SVC(gamma='auto'))


def Model5(i, pre, Xtrain, Xtest, ytrain, ytest):
    print('pre', pre)
    models = {
        'RandomForest': RandomForestModel(),
        'Naive_Bayes': Naive_BayesModel(),
        'MLPClassifier': MLPClassifierModel(),
        'SVC': SVCModel()
    }
    MODEL = {}
    ListModel = {}
    if i == 1:
        for key, value in models.items():
            model = value
            model.fit(Xtrain, ytrain)
            ypred = model.predict(Xtest)
            mo = model
            predicts = mo.predict([pre])
            print('predicts 1 ',predicts)
            # sta = Inverse(i, data)
            # for s in predicts:
            #     complete = sta[s]

            #แสดงค่าความถูกต้อง
            acc = accuracy_score(ypred, ytest)
            MODEL[key] = acc

        all_values = MODEL.values()
        max_key = max(MODEL, key=MODEL.get)
        max_value = max(all_values)
        print(max_key,max_value)
        ListModel[i] = max_key, max_value
        return ListModel
    elif i == 2:
        for key, value in models.items():
            model = value
            model.fit(Xtrain, ytrain)
            ypred = model.predict(Xtest)
            mo = model
            predicts = mo.predict([pre])
            print('predicts 2 ',predicts)
            #แสดงค่าความถูกต้อง
            acc = accuracy_score(ypred, ytest)
            MODEL[key] = acc

        all_values = MODEL.values()
        max_key = max(MODEL, key=MODEL.get)
        max_value = max(all_values)
        # print(max_key,max_value)
        ListModel[i] = max_key, max_value
        return ListModel
    elif i == 3:
        for key, value in models.items():
            model = value
            model.fit(Xtrain, ytrain)
            ypred = model.predict(Xtest)
            mo = model
            predicts = mo.predict([pre])
            print('predicts 3 ',predicts)
            #แสดงค่าความถูกต้อง
            acc = accuracy_score(ypred, ytest)
            MODEL[key] = acc
            ListModel[i] = MODEL

        all_values = MODEL.values()
        max_key = max(MODEL, key=MODEL.get)
        max_value = max(all_values)
        # print(max_key,max_value)
        ListModel[i] = max_key, max_value
        return ListModel

    elif i == 4:
        for key, value in models.items():
            model = value
            model.fit(Xtrain, ytrain)
            ypred = model.predict(Xtest)
            mo = model
            predicts = mo.predict([pre])
            print('predicts 4 ',predicts)
            #แสดงค่าความถูกต้อง
            acc = accuracy_score(ypred, ytest)
            MODEL[key] = acc
            ListModel[i] = MODEL

        all_values = MODEL.values()
        max_key = max(MODEL, key=MODEL.get)
        max_value = max(all_values)
        # print(max_key,max_value)
        ListModel[i] = max_key, max_value
        return ListModel

    elif i == 5:
        predi = []
        # le = preprocessing.LabelEncoder()
        # le.fit(df['Status'])
        # list(le.classes_)
        # le.transform(df['Status'])
        # list(le.inverse_transform([1]))
        for key, value in models.items():
            model = value
            model.fit(Xtrain, ytrain)
            ypred = model.predict(Xtest)
            mo = model
            predicts = mo.predict([pre])
            predi.append(predicts)
            print('predicts 5 ',predicts)

            # mo = model
            # mo.predict([pre])
            # # print('PRE', [pre])
            # print(mo.predict([pre]))

            #แสดงค่าความถูกต้อง
            acc = accuracy_score(ypred, ytest)
            MODEL[key] = acc
            ListModel[i] = MODEL
        all_values = MODEL.values()
        max_key = max(MODEL, key=MODEL.get)
        max_value = max(all_values)
        print(max_key,max_value)
        ListModel[i] = max_key, max_value
        
        return ListModel 


def predict(pre, Xtrain, Xtest, ytrain, ytest):
    df = DataFrame(DataStudents.objects.all().values())
    data = df.copy()
    # ตัดขอมูล ไม่มีสิทธิ์สัมภาษณ์ ออก
    dropdata = data[data.s_status != 'ไม่มีสิทธิ์สัมภาษณ์']
    data = dropdata.reset_index(drop=True)

    #รวม status ผ่านแต่ไม่ชำระเงิน และ ไม่มาสัมภาษณ์ ให้เป็น "ไม่เลือกเรียน"
    count = 0
    for i in range(len(data.s_status)):
        x = re.findall("ไม่", data.s_status[i])
        if (x):
            data.s_status[i] = "ไม่เลือกเรียน"
            count = count + 1

    models = {
        'RandomForest': RandomForestModel(),
        'Naive_Bayes': Naive_BayesModel(),
        'MLPClassifier': MLPClassifierModel(),
        'SVC': SVCModel()
    }
    MODEL = {}
    ListModel = {}
    predi = []
    for key, value in models.items():
        model = value
        model.fit(Xtrain, ytrain)
        ypred = model.predict(Xtest)
        # mo = model
        # predicts = mo.predict([pre])
        mo = model
        predicts = mo.predict([pre])
        predi.append(predicts)
        

        sta = Inverse(i, data)
        # print('predi',predi)
        

        #แสดงค่าความถูกต้อง
        acc = accuracy_score(ypred, ytest)
        MODEL[key] = acc
        ListModel[5] = MODEL
    all_values = MODEL.values()
    max_key = max(MODEL, key=MODEL.get)
    max_value = max(all_values)
    print(max_key,max_value)
    ListModel[5] = max_key, max_value

    print('predicts 5 ',predicts)
    compre = []
    for i in predi:
        for j in i:
            compre.append(j)
            # print(j)
    # print('ค่าซ่ำกันมากที่สุด',[item for item, count in collections.Counter(compre).items() if count > 1])
    print('compre',compre)
    gg = [item for item, count in collections.Counter(compre).items() if count > 1]
    for s in gg:
        complete = sta[s]
    # m = Model5(5,pre,Xtrain, Xtest, ytrain, ytest)
    # mo = models[max_key]
    # predicts = mo.predict([pre])
    # sta = Inverse(i, data)
    # for s in predicts:
    #     complete = sta[s]
    
    # print('predicts',predicts)
    return complete
    # models = {
    #     'RandomForest': RandomForestModel(),
    #     'Naive_Bayes': Naive_BayesModel(),
    #     'MLPClassifier': MLPClassifierModel(),
    #     'SVC': SVCModel()
    # }
    # mo = Naive_BayesModel(Xtrain5, Xtest5, ytrain5, ytest5)
    # print(mo)
    # print(i)
    
    # print("predict ", mo.predict( [ pre ]) )
    # mo.predict([[1,1,2,1,1,0,0,2,1,128,463,48]])
    # print(mo.predict([[1,1,2,1,1,0,0,2,1,128,463,48]]))
    # print('model=',models[model])