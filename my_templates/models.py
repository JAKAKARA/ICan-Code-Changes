"""Model definitions for `my_templates`."""

from __future__ import unicode_literals
from datetime import datetime
#from tabbed_admin import TabbedModelAdmin
from django.db import models

from smcapp1.models.patientsmodels import *
from smcapp1.models.listmodels import *
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db.models import signals
from django.dispatch import receiver

from django.utils.encoding import python_2_unicode_compatible


from django.forms import ModelForm, Textarea, TextInput
from django.contrib.admin import widgets
from django.utils.safestring import mark_safe
from django.utils.html import format_html
# from django.db.models.signals import m2m_changed

class Age_Groups(models.Model):

    id = models.AutoField(primary_key=True)
    age_group =  models.CharField(max_length=250) 

        # 'Neonates', 'Neonates'
        # '1 month - 6 months'
        # '7 months - 2years' 
        # '2+ years - 5 years' 
        # '5+ years - 12 years' 
        # '12+ years - 18 years,
        #  Adults 
        # 'Geriatric Age Group'

    class Meta:
        verbose_name = "Age_Group"
        verbose_name_plural = "Age_Groups"

    # Return a readable string for this object.
    def __str__(self):
        return "%s" % (self.age_group,)




# Class `Medication_Templates` used in `my_templates/models.py`.
class Medication_Templates(models.Model):	

    id = models.AutoField(primary_key=True)
    clinicians_name =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250)   
    short_description = models.CharField(max_length=250, blank=True, null=True)
    age_group = models.ForeignKey(Age_Groups, on_delete=models.CASCADE, null=True, blank=True)  

    '''

	Inlines will be inserted at the admin.py
	to allow for adding medications/prescriptions
	adding Complaints
	adding Lab requests
	adding Procedures
	But where are the models for these ones?
	Answer = in the listmodels.py
	one other thing  to remember is that these models are linked
	to the general consulting model through the bridge_models e.g. in the procedures_productsapp
	'''
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    created_date = models.DateField(default=datetime.today, blank=True)



    # checked_in_by =  models.ForeignKey(User, null=True, blank=True) # this is just to know which nurse did the vitals and consultation bills


    class Meta:
        verbose_name = "Medication_Templates"
        verbose_name_plural = "Medication_Templates"

    # Return a readable string for this object.
    def __str__(self):
        return "%s %s" % (self.clinicians_name, self.created_date)





# Class `Lab_Templates` used in `my_templates/models.py`.
class Lab_Templates(models.Model):


    id = models.AutoField(primary_key=True)
    clinicians_name =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250)   
    short_description = models.CharField(max_length=250, blank=True, null=True) 

    '''

	Inlines will be inserted at the admin.py
	to allow for adding medications/prescriptions
	adding Complaints
	adding Lab requests
	adding Procedures
	But where are the models for these ones?
	Answer = in the listmodels.py
	one other thing  to remember is that these models are linked
	to the general consulting model through the bridge_models e.g. in the procedures_productsapp
	'''
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    created_date = models.DateField(default=datetime.today, blank=True)



    # checked_in_by =  models.ForeignKey(User, null=True, blank=True) # this is just to know which nurse did the vitals and consultation bills


    class Meta:
        verbose_name = "Lab_Template"
        verbose_name_plural = "Lab_Templates"

    # Return a readable string for this object.
    def __str__(self):
        return "%s %s" % (self.clinicians_name, self.created_date)

