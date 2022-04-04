from asyncio.subprocess import PIPE, STDOUT
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import jira
import requests
import sys
import subprocess
import jiratest1
from jira import JIRA 
from django.contrib import messages
import os
import gc
import servicenowupload
import json
import base64
#a=''
l=[]
def button(request):
    return render(request,'jira1.html')
'''def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home.html',{'data':data})'''
@login_required
def external(request):
    #inp= request.POST.get('param')
    a=request.POST.get('jira')
    out= subprocess.run([sys.executable,'C://Users//gvarshini//Desktop//djangoproj//test.py'],shell=False,stdout=PIPE)
    #print(out)
    
    jiratest1.ssuploader(a)
    
    return render(request,'jiraupload.html')
@login_required
def dashboardView(request):
    return render(request,'dashboard.html')
def LoginView(request):
    return render(request,'login.html')
@login_required
def commandloggerView(request):
    a=request.POST.get('jira')
    l.append(a)
    
    c=jiratest1.getIssue(a)
    #d=jiratest1.ssuploader(a)


    return render(request,'commandlogger.html',{'data': c})
@login_required
def LogoutView(request):
    return render(request,'logout.html')

@login_required
def frontpage(request):
    return render(request,'frontpage.html')

def jiratest(request):
    inp= request.POST.get('param')
    out= subprocess.check_output([sys.executable,'C:\\Users\\gvarshini\\Desktop\\jiratest.py'])
    #out=subprocess.run(jiratest1.getVendorMaintainanceIssue())
    s = ''.join(map(chr, out))
    
    l=s.split('/r/r/n')
    s1="\n".join(l)
    #print(s)
    
    
    #print(b.decode())
    #data='123'


    return render(request,'jira1.html',{'data': s1})
def jirainp(request):
    #print(request.POST)
    '''a=request.POST.get('jira')
    print(a)
    c=jiratest1.getVendorMaintainanceIssue(a)

    return render(request, "jirainp.html",{'data': c})'''
    

    '''a=request.POST.get('jira')
    l.append(a)
    c=jiratest1.getVendorMaintainanceIssue(a)
    #print(a)'''
    
    
    '''print(a)
    print(l)'''

    return render(request, "jirainp.html")
#print(jiratest1.getVendorMaintainanceIssue(a))
def jiraupload(request):
    a=request.POST.get('jira')
    jiratest1.ssuploader(a)
    return render(request, "jiraupload.html")
@login_required
def servicenowuploader(request):
    
    '''user=request.POST.get('username')
    pwd=request.POST.get('spassword')'''
    s=request.POST.get('snow')
    l=[s]
    print(l)
    servicenowupload.upload123(request.POST.get('username'),request.POST.get('spassword'),l[0])
    return render(request, "servicenowupload.html")

def documentation1(request):
    
    return render(request, "documentation1.html")
