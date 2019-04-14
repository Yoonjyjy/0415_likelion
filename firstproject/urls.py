"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import blog.views
import selfintro.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/home/', blog.views.home, name='home'),
    path('blog/post/<int:post_id>/', blog.views.detail, name='detail'),
        ##포스트마다 수동으로 할당X, 자동으로 부여해주도록 됨!
    path('blog/post/new/', blog.views.post_new, name='new'),
    path('selfintro/selfhome/', selfintro.views.selfhome, name='selfhome'),
    path('selfintro/post2/<int:post_id>/', selfintro.views.selfdetail, name='selfdetail'),
    path('selfintro/post2/new2/', selfintro.views.post_new2, name='new2'),
]
