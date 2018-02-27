# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from customer.models import Customer
from customer.serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    model = Customer
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
