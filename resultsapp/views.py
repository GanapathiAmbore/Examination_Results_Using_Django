from django.shortcuts import render
from django.views.generic import ListView
from resultsapp.models import Hallticket,Student
from django.db.models import Q

class Results(ListView):
    model = Student
    template_name = 'results.html'


def search(request):
    queryset=Student.objects.filter(name__icontains='Ganapathi')
    return render(request,'search.html',{'qurey':queryset})

