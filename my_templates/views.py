"""View layer for `my_templates`."""

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import *


from medication_productsapp.models import *
from lab_productsapp.models import *
from procedure_productsapp.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



# Create your views here.


def template_index1(request):

    return render(request, 'template_index1.html')



# Handle the `template_medications` page flow for this app.
def template_medications(request, id):
    # here id is the doctor / user id
    templates_list = Medication_Templates.objects.filter(clinicians_name_id=id).order_by('title')
    # this gives us all the sets of medications written by this user


    return render(request, 'medications.html', {'context1': templates_list })


# Handle the `template_labs` page flow for this app.
def template_labs(request, id):
    # here id is the doctor / user id
    templates_list = Lab_Templates.objects.filter(clinicians_name_id=id).order_by('title')
    # this gives us all the sets of labs written by this user

    return render(request, 'labs.html', {'context1': templates_list})




# Handle the `medication_alphabet_pagination` page flow for this app.
def medication_alphabet_pagination(request, id, alphabet):
    # here id is the doctor / user id
    templates_list = Medication_Templates.objects.filter(clinicians_name_id=id, title__istartswith=alphabet ).order_by('title')

    return render(request, 'medications.html', {'context1': templates_list})
