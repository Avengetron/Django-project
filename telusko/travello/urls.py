from django.urls import path
from . import views #this view belogs to travello app

urlpatterns = [
    path('',views.index,name = 'index'),  #Calling home function from views module of calc app
]