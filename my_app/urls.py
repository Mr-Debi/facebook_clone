from django.urls import path
from. import views

urlpatterns = [
    path('',views.Login, name = 'login'),
    path('home',views.home, name = 'home'),
    path('profile',views.profile, name = 'profile'),
    path('contact',views.contact,name = 'contact'),
    path('logout',views.Logout, name = 'logout'),
    path('register',views.register,name='register'),
    path('post',views.create_post,name='post'),
    path('update',views.update_profile,name='update'),
    path('full_name',views.full_name,name='full_name'),
    
]