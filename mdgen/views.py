# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Rest framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# Django http
from django.http import JsonResponse

# Models
from mdgen.models import Member

# Exceptions
from django.core.exceptions import ObjectDoesNotExist


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
