from django.contrib import admin
from django.urls import path
from home import views
admin.site.site_header = "Ronish IceCream Admin"
admin.site.site_title = "Ronish IceCream Admin Portal"
admin.site.index_title = "Welcome to Ronish IceCream Portal"

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("services", views.services, name="services"),
    path("options", views.options, name="options"),
    path("tour", views.tour, name="tour"),
    path("view",views.view, name="view"),
    path("login", views.loginUser, name="login"),
    path("logout", views.logoutUser, name="logout")
]
