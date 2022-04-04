"""myadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 
from django.contrib.auth.views import LoginView,LogoutView

from myadmin import views

from django.shortcuts import redirect, render

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth.decorators import login_required
admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.button),
    #path('output/', views.output,name="script"),
    path('commandlogger/external', views.external,name="external"),
    #path('login/',views.LoginView,name="login_url"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home1.html'), name='home'),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('commandlogger/',views.commandloggerView,name="commandlogger",),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
    path('jira1/jiratest',views.jiratest,name="jira",),
    path('jira1/',views.jiratest,name="jira",),
    path('jirainp/',views.jirainp,name="jirainp",),
    #path('commandlogger/external',views.jiraupload,name="",),
    path('servicenowupload/',views.servicenowuploader,name="servicenowuploader",),
    path('frontpage/',views.frontpage,name="frontpage",),
    path('documentation1/',views.documentation1,name="documentation1",),
]

urlpatterns += staticfiles_urlpatterns()