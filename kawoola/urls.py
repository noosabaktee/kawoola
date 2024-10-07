"""kawula URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from abdi.views import profile, customhandler404
from show.views import show_cv
from asup.views import register, login_view
from django.contrib.auth.views import LogoutView
from update.views import *
from create.views import *
from delete.views import *
from help.decorators import is_staff
from setpassword.views import get_token, change
from django.views.generic import TemplateView

# Check if user is staff
admin.site.login = is_staff(admin.site.login)


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('faq/', TemplateView.as_view(template_name="faq.html"), name="faq"),
    path('rnb/', admin.site.urls),
    # Authentication
    path('register/', register, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    # Abdi
    path('abdi/', profile, name="abdi"),
    # Social
    path('social/update/', update_social, name="update_social"),
    # Color
    path('color/update/', update_color, name="update_color"),
    # Summary
    path('summary/update/', update_summary, name="update_sum"),
    # Career
    path('career/update/', update_career, name="update_career"),
    # Profile
    path('profile/update/', update_profile, name="update_profile"),
    # Education
    path('education/add/', add_edu, name="add_edu"),
    path('education/delete/', del_edu, name="del_edu"),
    path('education/update/', update_edu, name="update_edu"),
    # Achievement
    path('achievement/add/', add_achievement, name="add_ach"),
    path('achievement/delete/', del_achievement, name="del_ach"),
    path('achievement/update/', update_achievement, name="update_ach"),
    # Experience
    path('experience/add/', add_experience, name="add_exp"),
    path('experience/delete/', del_experience, name="del_exp"),
    path('experience/update/', update_experience, name="update_exp"),
    # Skill
    path('skill/add/', add_skill, name="add_skill"),
    path('skill/delete/', del_skill, name="del_skill"),
    path('skill/update/', update_skill, name="update_skill"),
    # Template
    path('template/update/', update_template, name="update_template"),
    # Set Password
    path('password/get-token/', get_token, name="get_token"),
    path('password/set/<uuid:token>/', change, name="set_password"),
    # Photo
    path('photo/update/', update_photo, name="update_photo"),
    # Show
    path('<str:username>/', show_cv, name="show"),
]

handler404 = customhandler404
