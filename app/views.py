from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def Student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SO=StudentForm(request.POST)
        if SO.is_valid():
            return HttpResponse(f'<h1>{str(SO.cleaned_data)}</h1>')
        else:
            return HttpResponse('<h1>the data is not valid</h1>')

    return render(request,'Student.html',d)