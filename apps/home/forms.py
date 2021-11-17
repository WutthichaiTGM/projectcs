from django import forms
from .models import DataStudents
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

PREFIX = (
    ('นาย', 'นาย'),
    ('นางสาว', 'นางสาว'),
)

STATUS_CHOICES = (
    ('ไม่มีสิทธิ์สัมภาษณ์','ไม่มีสิทธิ์สัมภาษณ์'),
    ('ไม่มาสัมภาษณ์','ไม่มาสัมภาษณ์'),
    ('ผ่านแต่ไม่ชำระเงิน','ผ่านแต่ไม่ชำระเงิน'),
    ('ชำระเงินเรียบร้อย','ชำระเงินเรียบร้อย')
)

class StudentsForm(forms.ModelForm):

    s_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ID",
                "class": "form-control"
            }
        )
    )
    s_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "รหัสผู้สมัคร",
                "class": "form-control"
            }
        )
    )
    s_prefix = forms.ChoiceField(
        choices=PREFIX,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
    s_status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
    s_Applicant_type = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ประเภทผู้สมัคร",
                "class": "form-control"
            }
        )
    )
    s_Faculty_Code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "รหัสคณะ",
                "class": "form-control"
            }
        )
    )
    s_Field_of_study = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "สาขาวิชา",
                "class": "form-control"
            }
        )
    )
    s_Year = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ปีการศึกษา",
                "class": "form-control"
            }
        )
    )
    s_Thai_Grade = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดภาษาไทย",
                "class": "form-control"
            }
        )
    )
    s_Math_Grade = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดคณิตศาสตร์",
                "class": "form-control"
            }
        )
    )
    s_Science_Grade = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดวิทยาศาสตร์",
                "class": "form-control"
            }
        )
    )
    s_Social_studies_Grades = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดสังคมศึกษา",
                "class": "form-control"
            }
        )
    )
    s_Health_education_Grades = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดสุขศึกษา",
                "class": "form-control"
            }
        )
    )
    s_Art_Grade = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดศิลปะ",
                "class": "form-control"
            }
        )
    )
    s_Career_Grade = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดการงานอาชีพ",
                "class": "form-control"
            }
        )
    )
    s_Foreign_language_Grade = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดภาษาต่างประเทศ",
                "class": "form-control"
            }
        )
    )
    s_GPAX = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดเฉลี่ยรวม",
                "class": "form-control"
            }
        )
    )
    s_School_Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ชื่อโรงเรียน",
                "class": "form-control"
            }
        )
    )
    s_Province_Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ชื่อจังหวัด",
                "class": "form-control"
            }
        )
    )


    class Meta:
        model = DataStudents
        fields = '__all__'



class StudentsSearchForm(forms.ModelForm):
    class Meta:
        model = DataStudents
        fields = ['s_id', 's_code', 's_Applicant_type',
                  's_Field_of_study', 's_Year', 's_School_Name', 's_Province_Name']
        labels = {
            's_id': 'ID',
            's_code': 'รหัสผู้สมัคร',
            's_Applicant_type': 'ประเภทผู้สมัคร',
            's_Field_of_study': 'สาขาวิชา',
            's_Year': 'ปีการศึกษา',
            's_School_Name': 'ชื่อโรงเรียน',
            's_Province_Name': 'ชื่อจังหวัด'
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "password1", "password2", 'is_superuser',
                  'is_staff', 'is_active', 'email', 'first_name', 'last_name']
        # fields = '__all__'
        labels = {
            'username': 'Username',
            'password1': 'Password1',
            'is_superuser': 'Superuser',
            'is_staff': 'Staff',
            'is_active': 'Active',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }


class UploadContactForm(forms.Form):
    file = forms.FileField(label='File:', error_messages={
                           'required': 'File required'})


class UploadFileForm(forms.Form):
    file = forms.FileField()


class PredictForm(forms.ModelForm):
    s_prefix = forms.ChoiceField(
        choices=PREFIX,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
    s_Thai_Grade = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดภาษาไทย",
                "class": "form-control"
            }
        )
    )
    s_Math_Grade = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดคณิตศาสตร์",
                "class": "form-control"
            }
        )
    )
    s_Science_Grade = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดวิทยาศาสตร์",
                "class": "form-control"
            }
        )
    )
    s_Social_studies_Grades = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดสังคมศึกษา",
                "class": "form-control"
            }
        )
    )
    s_Health_education_Grades = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดสุขศึกษา",
                "class": "form-control"
            }
        )
    )
    s_Art_Grade = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดศิลปะ",
                "class": "form-control"
            }
        )
    )
    s_Career_Grade = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดการงานอาชีพ",
                "class": "form-control"
            }
        )
    )
    s_Foreign_language_Grade = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดภาษาต่างประเทศ",
                "class": "form-control"
            }
        )
    )
    s_GPAX = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "เกรดเฉลี่ยรวม",
                "class": "form-control"
            }
        )
    )
    s_School_Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ชื่อโรงเรียน",
                "class": "form-control"
            }
        )
    )
    s_Province_Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ชื่อจังหวัด",
                "class": "form-control"
            }
        )
    )


    class Meta:
        model = DataStudents
        fields = ['s_prefix', 's_Thai_Grade', 's_Math_Grade', 's_Science_Grade', 's_Social_studies_Grades', 's_Health_education_Grades',
                  's_Art_Grade', 's_Career_Grade', 's_Foreign_language_Grade', 's_GPAX', 's_School_Name', 's_Province_Name']
    # class Meta:
    #     model = DataStudents
    #     fields = ['s_prefix', 's_Thai_Grade', 's_Math_Grade', 's_Science_Grade', 's_Social_studies_Grades', 's_Health_education_Grades',
    #               's_Art_Grade', 's_Career_Grade', 's_Foreign_language_Grade', 's_GPAX', 's_School_Name', 's_Province_Name']
    #     labels = {
    #         's_prefix': 'คำนำหน้า',
    #         's_Thai_Grade': 'เกรดภาษาไทย',
    #         's_Math_Grade': 'เกรดคณิตศาสตร์',
    #         's_Science_Grade': 'เกรดวิทยาศาสตร์',
    #         's_Social_studies_Grades': 'เกรดสังคมศึกษา',
    #         's_Health_education_Grades': 'เกรดสุขศึกษา',
    #         's_Art_Grade': 'เกรดศิลปะ',
    #         's_Career_Grade': 'เกรดการงานอาชีพ',
    #         's_Foreign_language_Grade': 'เกรดภาษาต่างประเทศ',
    #         's_GPAX': 'เกรดเฉลี่ยรวม',
    #         's_School_Name': 'ชื่อโรงเรียน',
    #         's_Province_Name': 'ชื่อจังหวัด'
    #     }
