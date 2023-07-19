from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Members,Events,Gallery,WeeklyDevotion
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request,"core/index.html")

# def about(request):
#     return render(request,"core/about.html")

def contact(request):
    return render(request,"core/contact.html")

def member_join(request):
    if request.method =="POST":
        phonenumber=request.POST.get('phonenumber')
        county=request.POST.get('county')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        college=request.POST.get("college")
        criterion1 = Q(phonenumber__contains=phonenumber)
        criterion2 = Q(college__contains=college)
        member=Members(phonenumber=phonenumber,county=county,firstname=firstname,lastname=lastname,college= college)
        member_find=Members.objects.filter(criterion1 & criterion2)
        if member_find:
            messages.error(request,"member with the above details already exists")
            return redirect("core:home")
        else:
            member.save()
            messages.success(request,"member added successfully")
            return redirect("core:home")
    return render(request,"core/index.html")
    # return render(request,"core/form.html")

def success(request):
    return render(request,"core/success.html")

def events(request):
    events=Events.objects.all()
    context={"events":events}
    return render(request,"core/events.html",context)

def gallery(request):
    images=Gallery.objects.all()
    print(len(images))
    return render(request,"core/gallery.html",locals())
    

def devotions(request):
    devotions=WeeklyDevotion.objects.all()
    return render(request,"core/devotion.html")

def donations(request):
    return render(request,"core/donate.html")