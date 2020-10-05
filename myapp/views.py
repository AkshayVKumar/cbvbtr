from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView,ListView
from myapp.forms import *
from myapp.models import School,Student
#Basic View
# Create your views here.
def sample(request):
    return HttpResponse("<h1>Function Based Views</h1>")

class SampleView(View):
    def get(self,request):
        return HttpResponse("<h1>Class Based Views</h1>")

class Sample1View(View):
    def get(self,request):
        return render(request,"sample.html")
    
    def post(self,request,*args,**kwargs):
        data=request.POST.get("name")
        return HttpResponse("<h1>{}</h1>".format(data))

class Sample2View(View):
    form_name=SampleForm
    def get(self,request):
        form=self.form_name()
        return render(request,"sample1.html",{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=self.form_name(request.POST)
        if form.is_valid():
            return HttpResponse("<h1>{}</h1>".format(form.cleaned_data['name']))

        return render(request,"sample1.html",{'form':form})

class Template_View(TemplateView):
    template_name="sample.html"


class Template_DemoView(TemplateView):
    template_name="sample2.html"

class School_ListView(ListView):
    model=School
    template_name="school_list.html"
    context_object_name="schools"

class Student_ListView(ListView):
    model=Student
