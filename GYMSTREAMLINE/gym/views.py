from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import *

# Create your views here.


def Home(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def Add_Coach(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        coa_id = request.POST['coa_id']
        name = request.POST['name']
        surname = request.POST['surname']
        contact = request.POST['contact']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        job_title = request.POST['job_title']
        try:
            Coach.objects.create(CoaId=coa_id, Name=name, Surname=surname, Contact=contact, Emailid=email, Age=age, Gender=gender, JobTitle=job_title)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_coach.html', d)


def View_Coach(request):
    coa = Coach.objects.all()
    d = {'coa': coa}
    return render(request, 'view_coach.html', d)


def Delete_Coach(request,coa_id):
    coach = Coach.objects.get(CoaId=coa_id)
    coach.delete()
    return redirect('view_coach')


def Add_MemberPlan(request):
    error = ""
    plan1 = Plan.objects.all()
    memb1 = Member.objects.all()
    coach1 = Coach.objects.all()
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        member_id = request.POST['member_id']
        plan_id_name = request.POST['plan_id_name']
        join_date = request.POST['join_date']
        exp_date = request.POST['exp_date']
        state = request.POST['state']
        coach_id = request.POST.get('coach_id', None)
        plan = Plan.objects.filter(NameId=plan_id_name).first()
        memb = Member.objects.filter(MemId=member_id).first()
        coach = Coach.objects.filter(CoaId=coach_id).first()
        try:
            MemberPlan.objects.create(MemberId=memb, PlanIdName=plan, Joindate=join_date, Expdate=exp_date, State=state, CoachId=coach)
            error = "no"
        except:
            error = "yes"
    d = {'error': error, 'memberID':memb1, 'plan':plan1, 'coachID':coach1}
    return render(request, 'add_memberplan.html', d)


def View_MemberPlan(request):
    mep = MemberPlan.objects.all()
    d = {'mep': mep}
    return render(request, 'view_memberplan.html', d)


def Delete_MemberPlan(request,member_id):
    memberplan = MemberPlan.objects.get(MemberId=member_id)
    memberplan.delete()
    return redirect('view_memberplan')

def Add_Plan(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        name = request.POST['name']
        amount = request.POST['amount']
        duration = request.POST['duration']
        try:
            Plan.objects.create(NameId=name, Amount=amount, Duration=duration)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_plan.html', d)


def View_Plan(request):
    pln = Plan.objects.all()
    d = {'pln': pln}
    return render(request, 'view_plan.html', d)

def Delete_Plan(request,plan_id):
    plan = Plan.objects.get(NameId=plan_id)
    plan.delete()
    return redirect('view_plan')

def Add_Member(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        mem_id = request.POST['mem_id']
        name = request.POST['name']
        surname = request.POST['surname']
        contact = request.POST['contact']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        try:
            Member.objects.create(MemId=mem_id, Name=name, Surname=surname, Contact=contact, Emailid=email, Age=age, Gender=gender)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_member.html', d)


def View_Member(request):
    member = Member.objects.all()
    d = {'member': member}
    return render(request, 'view_member.html', d)

def Delete_Member(request,mem_id):
    member = Member.objects.get(MemId=mem_id)
    member.delete()
    return redirect('view_member')