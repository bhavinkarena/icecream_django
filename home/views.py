from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact,Order
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


def service(request):
    return render(request,"service.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your Massege Has Been Sent !")
    return render(request,"contact.html")

def order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip_code=request.POST.get('zip_code')
        order = Order(order_id=order_id,amount=amount,name=name,email=email,phone=phone,address=address,city=city,state=state,zip_code=zip_code)
        order.save()
        messages.success(request, "Your Massege Has Been Sent !")
    return render(request,"order.html")

