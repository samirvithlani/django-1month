
from django.http import HttpResponse

from django.shortcuts import render

from .models import Employee, Student
from django.template import context
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.
#function based view

def home(request):
    return HttpResponse("Hello World")

def contactus(request):
    return render(request,'contactus.html')

def aboutus(request):
    return render(request,' l')


# order by name
# married wf saalry 5000

def getEmployees(request):
    #queryset
    employees = Employee.objects.all().values_list()
    employees1 = Employee.objects.filter(name='amit').values_list()
    employees2  =Employee.objects.filter(name__endswith='t').values_list()
    employees3 = Employee.objects.filter(salary__gte=(1500)).values_list()
    employees4 = Employee.objects.filter(workchoice="work from home").values_list()
    employees5 = Employee.objects.filter(isMarried=True).values_list()
    #salary gt 1500 and work from homr
    employees6 = Employee.objects.filter(salary__gt=(1500),workchoice="work from home").values_list()
    employees7 = Employee.objects.filter(salary__gt=(1500)).order_by('salary').values_list()
    context = {
        'employees':employees7
    }
    return render(request,"home/employees.html",context)
    
class StudentView(CreateView):
    model=Student
    fields= '__all__'
    template_name = 'home/student.html'
    success_url="/home/studentlist"
    
class StudentListView(ListView):
    model = Student
    template_name = 'home/studentlist.html'
    context_object_name = 'students'
    
        
         