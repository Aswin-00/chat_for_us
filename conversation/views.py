from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    data=chat_data.objects.all()
    context={
        'chats':data
    }
    # print(her)
    return render(request,'index.html',context)



def send(request):
    if request.method=='POST':
        content=request.POST.get('msg')
        print(request.headers)
        if request.user.is_authenticated :
            chat_data(
                name='me',
                content=content

            ).save()
        else:
            chat_data(
                name='she',
                content=content
            ).save()
    return redirect('home')