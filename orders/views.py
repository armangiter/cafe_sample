from django.shortcuts import render
from django.views.generic import CreateView
from .models import Order, OrderItem


# Create your views here.

class OrderCreateView(CreateView):
    model = OrderItem
    fields = '__all__'
    template_name = 'orders/sample.html'
