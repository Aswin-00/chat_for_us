from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    data=chat_data.objects.all()
    me=data.filter(name='me')
    her=data.filter(name = 'she')
    print(me)
    print(her)
    # print(her)
    return render(request,'index.html')



def send(request):
    
    return redirect('index')