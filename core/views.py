from django.shortcuts import render,redirect
from .models import Members
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"core/index.html")

def about(request):
    return render(request,"core/about.html")

def contact(request):
    return render(request,"core/contact.html")

def member_join(request):
    if request.method =="POST":
        phonenumber=request.POST.get('phonenumber')
        county=request.POST.get('county')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        college=request.POST.get("college")
        member=Members(phonenumber=phonenumber,county=county,firstname=firstname,lastname=lastname,college= college)
        member.save()
        messages.success(request,"member added successfully")
    #return redirect("core:join")
    return render(request,"core/form.html")
    