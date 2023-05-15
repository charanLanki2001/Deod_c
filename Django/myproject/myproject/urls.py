
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginpage,name='loginpage'),
    path('signup/',views.signup,name='signuppage'),
    path('home/',views.Homepage,name='homepage'),
    path('video/',views.video,name='video'),

]
