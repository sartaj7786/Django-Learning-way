from django.shortcuts import render,HttpResponse
from datetime import datetime
from home1.models import Contact 
from django.contrib import messages

# Create your views here.

def index(request):
    context={
        "variable1":"This is set",
        "variable2":"Its a Universe"
    }
    return render(request,'index.html',context)
    # return HttpResponse("<h1>This is first Page</h1>")/


def about(request):
    return render(request, 'about.html')  


def services(request):
     return render(request, 'services.html')
    # return HttpResponse("This is services Page")  


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date= datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent!')
    return render(request, 'contact.html')
    # return HttpResponse("This is contact Page")   
def course(request):
    return render(request, 'course.html')
