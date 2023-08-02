from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
app_name="core"
urlpatterns = [
    path("",views.home,name="home"),
    
    path("contact/",views.contact,name="contact"),
    path("join/",views.member_join,name="join"),
    path("succes_join/",views.success,name="success"),

    path("devotion/",views.devotions,name="devotion"),
    path("gallery/",views.gallery,name="gallery"),
    path("events/",views.events,name="events"),
    path("donate/",views.donations,name="donate"),
    path("search/",views.search,name="search"),
    path("calendar/",views.calendar,name="calendar")

    
]
# path("about/",views.about,name="about"),
#path("join/",views.member_join,name="join")
