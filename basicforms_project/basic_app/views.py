from django.shortcuts import render
from basic_app import forms

# Create your views here.
def index(request):
    return render(request,'basic_app/index_b.html')


def form_name_view(request):
    form= forms.FormName()
    return render(request,'basic_app/form_page.html',{'form':form})
