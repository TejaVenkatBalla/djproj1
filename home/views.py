from django.shortcuts import render,redirect
from home.models import user

# Create your views here.
def home(request):
    return render(request,'entry.html')

def save(request):
    if request.method=='POST':
        n=request.POST.get('name')
        a=request.POST.get('age')
        x=user(name=n,age=a)
        x.save()
    users = user.objects.all()  # Retrieve all User objects
    context = {'users': users}
    return render(request,'show2.html',context)

def show2(request):
    users = user.objects.all()  # Retrieve all User objects
    context = {'users': users}
    return render(request,'show2.html',context)

def delete(request,id):
    obj = user.objects.get(id=id)
    obj.delete()
    users = user.objects.all()  # Retrieve all User objects
    context = {'users': users}
    return render(request,'show2.html',context)
def update(request,id):
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_age = request.POST.get('age')
        obj = user.objects.get(id=id)
        obj.name = new_name
        obj.age = new_age
        obj.save()
        users = user.objects.all()  
        context = {'users': users}
        return render(request,'show2.html',context) 

    user_to_update = user.objects.get(id=id)
    context = {'user': user_to_update}
    return render(request, 'update.html', context)