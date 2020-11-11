"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from conf.views import MainView
from example.views import AboutView
from example.views import FirstView
from example.views import SecondView
from example.views import StudentView
from example.views import ThirdView
from example.views import WelcomeView

urlpatterns = [
    path('', MainView.as_view()),
    path('students/<int:student_id>/', StudentView.as_view()),
    path('welcome/', WelcomeView.as_view()),
    path('about/', AboutView.as_view()),
    path('first/', FirstView.as_view()),
    path('second/', SecondView.as_view()),
    path('third/', ThirdView.as_view()),
    path('admin/', admin.site.urls),
]
