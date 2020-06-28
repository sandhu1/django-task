from django.urls import path
from myapp import views
#from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('date/',views.date_view,name='date_view'),
    path("ping/",views.ping,name='ping')

]
