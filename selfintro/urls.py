from django.contrib import admin
from django.urls import path
import selfintro.views

urlpatterns = [
    path('selfhome/', selfintro.views.selfhome, name='selfhome'),
    path('post2/<int:post_id>/', selfintro.views.selfdetail, name='selfdetail'),
    path('post2/new2/', selfintro.views.post_new2, name='new2'),
]
