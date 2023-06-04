"""GYMSTREAMLINE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from gym.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('about/', About, name = 'about'),
    path('contact/', Contact, name = 'contact'),
    path('admin_login', Login, name='login'),
    path('logout/', Logout, name='logout'),

    path('add_coach/',Add_Coach,name='add_coach'),
    path('view_coach/',View_Coach,name='view_coach'),
    path('delete_coach(?p<int:coa_id>)', Delete_Coach, name='delete_coach'),

    path('add_memberplan/',Add_MemberPlan,name='add_memberplan'),
    path('view_memberplan/',View_MemberPlan,name='view_memberplan'),
    path('delete_memberplan(?p<int:member_id>)', Delete_MemberPlan, name='delete_memberplan'),

    path('add_plan/',Add_Plan,name='add_plan'),
    path('view_plan/',View_Plan,name='view_plan'),
    path('delete_plan(?p<str:plan_id>)', Delete_Plan, name='delete_plan'),

    path('add_member/',Add_Member,name='add_member'),
    path('view_member/',View_Member,name='view_member'),
    path('delete_member(?p<int:mem_id>)', Delete_Member, name='delete_member'),
]
 