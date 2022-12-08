from django.shortcuts import render,redirect
from employee_app.models import employee
from django.http import HttpResponse

from django.views.generic import (ListView, DetailView,CreateView, UpdateView, DeleteView)

class emlpoyeelistview(ListView):
    model = employee
    template_name = 'employee_app/employee_list.html'
    context_object_name = 'employee_list'

    ordering = ('-id')

class emlpoyeedetailview(DetailView):
    model = employee
    template_name = 'employee_app/employee_detail.html'
    context_object_name = 'employee'

class emlpoyeecreateview(CreateView):
    model = employee
    fields = '__all__'
    template_name = 'employee_app/employee_create.html'
    context_object_name = 'form'

class emlpoyeeupdateview(UpdateView):
    model = employee
    fields = '__all__'
    template_name = 'employee_app/employee_create.html'
    context_object_name = 'form'

class emlpoyeedeletelview(DeleteView):
    model = employee
    success_url = '/employees/'
    template_name = 'employee_app/employee_delete.html'
    context_object_name = 'employee'

