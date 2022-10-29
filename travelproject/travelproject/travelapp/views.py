

from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from.models import crickter

# Create your views here.
def demo(request):
    obj=crickter.objects.all()
    obj1=Place.objects.all()
    return render(request,"index.html",{'results':obj,'result':obj1})

#def about(request):
  #  return  render(request,'about.html')
#def contact(request):
   # return  render(request,"contact.html")