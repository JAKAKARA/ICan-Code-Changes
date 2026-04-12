"""Admin configuration for `my_templates`."""

# Admin username = hamza password = Randymx8
from datetime import datetime, timedelta, time

from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from django.contrib.admin import DateFieldListFilter
from billingapp.models import *
from django.forms import ModelForm, Textarea, TextInput, NumberInput
from django.utils.html import format_html
# from django.contrib.admin import widgets
import unicodedata
from django.utils.safestring import mark_safe
from tabbed_admin import TabbedModelAdmin
from django.contrib import admin
from django import forms
admin.autodiscover()


from easy_select2 import select2_modelform
from easy_select2 import select2_modelform_meta
from django.contrib.auth.models import User


from .models import *



# Register your models here.
from medication_ordersapp.models import *
from medication_productsapp.models import *




from lab_ordersapp.models import *
from lab_productsapp.models import *



today = datetime.now().date()


'''
Begin Inline:
Beginning of the inline additions from the
Medications_productsapp and orders app
Lab_productsapp and orders app
Procedure_productsapp and orders app

'''


class Medications_Bridge2Inline (admin.TabularInline):
    # Inline configuration for Django's admin on the Medications_Bridge model

    form = select2_modelform(Medications_Bridge2)
    model = Medications_Bridge2

    fields = [
    'medication_name_id', 'dosage', 'duration', 
    'other_notes',]


    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'12'})},
    }
    extra = 1
    # can_delete = False

    def get_formset(self, request, obj=None, **kwargs):
        """
        Override the formset function in order to remove the add and change buttons beside the foreign key pull-down
        menus in the inline.
        """
        formset = super(Medications_Bridge2Inline, self).get_formset(request, obj, **kwargs)
        form = formset.form
        widget = form.base_fields['medication_name_id'].widget
        widget.can_add_related = False
        widget.can_change_related = False
        widget = form.base_fields['medication_name_id'].widget
        widget.can_add_related = False
        widget.can_change_related = False
        return formset

'''
this code is not really working for now
    # Implement `get_form` behavior in this module.
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.exclude = ('paid', 'payment_type', 'payment_id',)
        else:
            pass

        return super(Medications_BridgeInline, self).get_form(request, obj, **kwargs)
'''


class Labs_Bridge2Inline (admin.TabularInline):
    # Inline configuration for Django's admin on the Labs_Bridge model
    form = select2_modelform(Labs_Bridge2)
    model = Labs_Bridge2

    # exclude = ('paid', 'payment_type',"created_date",
    # 'quantity','unit_price',
    # 'amount', 'payment_id',
    # 'lab_requested_by','insurance_covered',
    #   )
    fields = ['lab_name_id',]
    extra = 1





'''
End Inline
'''



class Age_GroupsAdmin(admin.ModelAdmin):

    list_display = ['age_group',]
    list_per_page = 50
    list_display_links = ['age_group']




# Admin configuration for `Medication_TemplatesAdmin` in this module.
class Medication_TemplatesAdmin(TabbedModelAdmin):
    model = Medication_Templates

    tab_template = (
        (None, {
            'fields': ('title','age_group',)
        }), Medications_Bridge2Inline,
		)

    tabs = [
        ('My Template', tab_template),

    ]


    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'30'})},
        models.IntegerField: {'widget': NumberInput(attrs={'size':'20'})},
    }

    search_fields = ["title", ]
    list_display = ['title', 'age_group',]
    readonly_fields = ["clinicians_name",]
    ordering = ('-created_date',)
    list_per_page = 50
    list_display_links = ['title']
    list_filter = ['age_group',]


# This is how you insert the user details in an inline form
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.prescribed_by = request.user
            instance.save()
        formset.save_m2m()

    # Implement `save_model` behavior in this module.
    def save_model(self, request, obj, form, change):
        if not obj.clinicians_name:
            obj.clinicians_name = request.user


        super(Medication_TemplatesAdmin, self).save_model(request, obj, form, change)

    # Customize the response after add operations.
    def response_add(self, request, obj, post_url_continue=None):
    # # """This makes the response after adding a new record go to the given url"""
        # return redirect('/smcproject/index/cashier/')
        return HttpResponseRedirect('/smcproject/my_templates/template_medications/%s/' % int(obj.clinicians_name.id))
		
		
    # Customize the response after change operations.
    def response_change(self, request, obj, post_url_continue=None):
    # # """This makes the response after changing a new record go to the given url"""
        # return redirect('/smcproject/index/cashier/')		
        return HttpResponseRedirect('/smcproject/my_templates/template_medications/%s/' % int(obj.clinicians_name.id))

    # def has_add_permission(self, request, obj=None):
    #     return False


    # def has_delete_permission(self, request, obj=None):
    #     return False





class Lab_TemplatesAdmin(TabbedModelAdmin):
    model = Lab_Templates

    tab_template = (
        (None, {
            'fields': ('title',)
        }),Labs_Bridge2Inline,
		)


    tabs = [
        ('My Template', tab_template),
    ]


    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'30'})},
        models.IntegerField: {'widget': NumberInput(attrs={'size':'20'})},
    }

    search_fields = ["title", "clinicians_name", ]
    list_display = ['title', 'created_date',]
    ordering = ('-created_date',)
    readonly_fields = ["clinicians_name",]
    list_per_page = 50
    list_display_links = ['title']
    # save_on_top = True

# This is how you insert the user details in an inline form
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.lab_requested_by = request.user
            instance.save()
        formset.save_m2m()

    # Implement `save_model` behavior in this module.
    def save_model(self, request, obj, form, change):
        if not obj.clinicians_name:
            obj.clinicians_name = request.user


        super(Lab_TemplatesAdmin, self).save_model(request, obj, form, change)




    # Customize the response after add operations.
    def response_add(self, request, obj, post_url_continue=None):
    # # """This makes the response after adding a new record go to the given url"""
        # return redirect('/smcproject/index/cashier/')
        return HttpResponseRedirect('/smcproject/my_templates/template_labs/%s/' % int(obj.clinicians_name.id))
		
		
    # Customize the response after change operations.
    def response_change(self, request, obj, post_url_continue=None):
    # # """This makes the response after changing a new record go to the given url"""
        # return redirect('/smcproject/index/cashier/')		
        return HttpResponseRedirect('/smcproject/my_templates/template_labs/%s/' % int(obj.clinicians_name.id))
 
#admin.site.register(Your_model_name, Your_model_nameAdmin)

admin.site.register(Medication_Templates, Medication_TemplatesAdmin)
admin.site.register(Lab_Templates, Lab_TemplatesAdmin)

admin.site.register(Age_Groups, Age_GroupsAdmin)