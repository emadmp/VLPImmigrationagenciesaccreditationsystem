from django.contrib import admin
from django.urls import path ,include
from base import views as Bview
 
urlpatterns = [
    path('' , Bview.mainView.as_view() , name = 'main'),
    path('bycountry/<int:cu_id>/<int:page>' , Bview.bycountryView.as_view() , name = 'bycountry',)

]
