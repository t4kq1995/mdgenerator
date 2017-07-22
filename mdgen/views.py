# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Rest framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# Django http
from django.http import JsonResponse

# Models
from mdgen.models import Member, Country, UserData, CountryData

# Exceptions
from django.core.exceptions import ObjectDoesNotExist

# Random
import random


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def login(request):
    """ Auth login view """
    if request.method == 'POST':
        username = request.data.get('login', '')
        password = request.data.get('password', '')

        if login != '' and password != '':
            try:
                Member.objects.get(login=username, password=password)
                return JsonResponse({'status': True})
            except ObjectDoesNotExist:
                return JsonResponse({'status': False})
        return JsonResponse({'status': False})


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def get_country_full(request):
    """ Get full country name """
    if request.method == 'POST':
        country = request.data.get('country', '')
        if country != '':
	        try:
		        country_object = Country.objects.get(country=country)
		        return JsonResponse({'status': True, 'country_full': country_object.country_full})
	        except ObjectDoesNotExist:
		        return JsonResponse({'status': False})
        return JsonResponse({'status': False})
    

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def get_user_data(request):
    """ Get full country name """
    if request.method == 'POST':
	    amount = request.data.get('amount', '')
	    if amount != '':
	        try:
		        answer = []
		        user_data = UserData.objects.all()
		        for element in user_data:
			        element_data = element.data.split(',')
			        random.shuffle(element_data)
			        answer.append(
				        {'type': element.type,
				         'data': [s.replace("'", "").strip() for s in element_data[:int(amount)]]
				         })
		        return JsonResponse({'status': True, 'user_data': answer})
	        except ObjectDoesNotExist:
		        return JsonResponse({'status': False})
	    return JsonResponse({'status': False})

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def get_country_data(request):
    """ Get full country name """
    if request.method == 'POST':
	    amount = request.data.get('amount', '')
	    country = request.data.get('country', '')
	    if amount != '' and country != '':
	        try:
		        answer = []
		        country_data = CountryData.objects.get(country=country)
		        data_country = country_data.data.split('\n')
		        random.shuffle(data_country)
		        return JsonResponse(
			        {
				        'status': True,
			            'country_data': [s.replace("\r", "").strip() for s in data_country[:int(amount)]]
			        }
		        )
	        except ObjectDoesNotExist:
		        return JsonResponse({'status': False})
	    return JsonResponse({'status': False})