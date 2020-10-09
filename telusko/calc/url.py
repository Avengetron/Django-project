from django.urls import path
from . import views #this view belogs to calc app

urlpatterns = [
    path('',views.cal,name = 'cal'),  #Calling .cal function from views module of calc app
    path('add',views.add,name = 'add')
]