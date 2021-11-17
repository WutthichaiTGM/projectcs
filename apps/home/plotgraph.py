# import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import base64
from io import  BytesIO
from .models import DataStudents
import pandas as pd
import numpy as np
# set Font
from matplotlib import rcParams
import seaborn as sns

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Tahoma']


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('UTF-8')
    buffer.close()
    fig = plt.figure()
    plt.switch_backend('agg')
    return graph

def pie_chart(x,y):
    mycolors = ['#10B981','#2361ce','#f3c78e','#E11D48']
    explode = (0.1, 0, 0, 0)
    plt.pie(y,labels=x, colors = mycolors,autopct='%1.2f%%')
    graph = get_graph()
    return graph

def dashboard_graph(x,y):
    if type(x) == str:
        Colors = []
        Color = []
        if x == 'ชำระเงินเรียบร้อย':
            Colors = '#10B981'
            Color.append('#10B981')
        elif x == 'ผ่านแต่ไม่ชำระเงิน':
            Colors = '#2361ce'
            Color.append('#2361ce')
        elif x =='ไม่มาสัมภาษณ์':
            Colors  == '#f3c78e'
            Color.append('#f3c78e')
        elif x =='ไม่มีสิทธิ์สัมภาษณ์':
            Colors  == '#E11D48'
            Color.append('#E11D48')
        plt.bar(x,y, color=Color)
        
    elif type(x) == list:
        mycolors = ['#10B981','#2361ce','#f3c78e','#E11D48']
        plt.bar(x,y, color=mycolors,label ='y')
    graph = get_graph()
    
    return graph

def school_data(x,y):
    plt.bar(x,y)
    plt.xticks(rotation=15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    graph = get_graph()
    return graph

# def admissions(x,y):
#     plt.bar(x,y)
#     plt.xticks(rotation=15)
#     plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
#     graph = get_graph()
#     return graph