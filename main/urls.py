
from django.urls import path
from main import views

urlpatterns = [
    path('', views.blog_home, name="home"),
    path('blog_details/', views.blog_details, name="details"),
    path('profile/', views.profile, name="profile"),
    path('contact_us/', views.contact_us, name="contact_us")
]
