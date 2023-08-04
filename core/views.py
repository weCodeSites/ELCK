from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Members,Events,Gallery,WeeklyDevotion,Sermon
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def home(request):
    sermons=Sermon.objects.all()
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
    if request.method =="POST":
        query=request.POST.get('search')
        print(query)
        results=Events.objects.filter(Q(title__contains=query))
        if results:
            messages.success(request,"results found")
        else:
            messages.error(request,"results not found")
    return render(request,"core/events.html",locals())
def gallery(request):
    images=Gallery.objects.all()
    return render(request,"core/gallery.html",locals())
    

def devotions(request):
    devotions=WeeklyDevotion.objects.all()
    return render(request,"core/devotion.html",locals())

def donations(request):
    return render(request,"core/donate.html")

def search(request):
    pass
#     query=request.GET['what']
#     results=Events.objects.filter(Q(title__icontains=query))
#     return render(request,"core/search.html",locals())

def calendar(request):
    return render(request,"core/calendar.html")