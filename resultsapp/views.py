from django.shortcuts import render
from django.views.generic import ListView,DetailView
from resultsapp.models import Hallticket,Student
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from reportlab.pdfgen import canvas

class Results(ListView):
    model = Student
    template_name = 'results.html'

def search(request):
    if request.method=='POST':
        srch=request.POST['srh']
        if srch:
            query=Student.objects.filter(name__icontains=srch)
            if query:
                return render(request,'search.html',{"sr":query})
            else:
                return  HttpResponse("<h1>Results Not found!!</h1>")
        else:
            return HttpResponse("No Records Found!!")
    return render(request,'search.html')






