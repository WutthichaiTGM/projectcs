# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


STATUS_CHOICES = (
    ('ไม่มีสิทธิ์สัมภาษณ์','ไม่มีสิทธิ์สัมภาษณ์'),
    ('ไม่มาสัมภาษณ์','ไม่มาสัมภาษณ์'),
    ('ผ่านแต่ไม่ชำระเงิน','ผ่านแต่ไม่ชำระเงิน'),
    ('ชำระเงินเรียบร้อย','ชำระเงินเรียบร้อย')
)
PREFIX = (
    ('นาย','นาย'),
    ('นางสาว','นางสาว')
)
class DataStudents(models.Model):
    s_id = models.CharField(max_length=999, blank=True)
    s_code = models.CharField(max_length=999, blank=True)
    s_prefix = models.CharField(max_length=999, choices=PREFIX)
    s_status = models.CharField(max_length=999 , choices=STATUS_CHOICES, blank=True)
    s_Applicant_type = models.CharField(max_length=999, blank=True)
    s_Faculty_Code = models.CharField(max_length=999, blank=True)
    s_Field_of_study = models.CharField(max_length=999, blank=True)
    s_Year = models.CharField(max_length=5, blank=True)
    s_Thai_Grade = models.FloatField()
    s_Math_Grade = models.FloatField()
    s_Science_Grade = models.FloatField()
    s_Social_studies_Grades = models.FloatField()
    s_Health_education_Grades = models.FloatField()
    s_Art_Grade = models.FloatField()
    s_Career_Grade = models.FloatField()
    s_Foreign_language_Grade = models.FloatField()
    s_GPAX = models.FloatField()
    s_School_Name = models.CharField(max_length=999, blank=True)
    s_Province_Name = models.CharField(max_length=999, blank=True)

    class Meta:
        ordering =['id']