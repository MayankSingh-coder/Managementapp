from django.contrib import admin
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="home"),
    path('accounts',views.accounts,name="accounts"),
    path('add/',views.add,name="add"),
    # path('add_reference',views.add_reference,name="add_reference"),
] 

