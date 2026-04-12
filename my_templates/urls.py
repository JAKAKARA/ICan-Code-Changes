"""URL routing for `my_templates`."""

from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings


urlpatterns = [

    # Route `template_index1` for `template_index1/`.
    url(r'template_index1/', views.template_index1, name= 'template_index1' ),	
    

    # Route `template_labs` for `template_labs/(?P<id>\d+)/`.
    url(r'template_labs/(?P<id>\d+)/', views.template_labs, name= 'template_labs' ),	
    # Route `template_medications` for `template_medications/(?P<id>\d+)/`.
    url(r'template_medications/(?P<id>\d+)/', views.template_medications, name= 'template_medications' ),

    # Route `medication_alphabet_pagination` for `medication_alphabet_pagination/(?P<id>\d+)/(?P<alphabet>[\w\-]+)/`.
    url(r'medication_alphabet_pagination/(?P<id>\d+)/(?P<alphabet>[\w\-]+)/', views.medication_alphabet_pagination, name= 'medication_alphabet_pagination' ),


    # url(r'copy/(?P<c_id>\d+)/(?P<p_id>\d+)/', views.copy, name= 'copy' ),	
	]
