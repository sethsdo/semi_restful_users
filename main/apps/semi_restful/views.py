from django.contrib import admin
from django.shortcuts import render, HttpResponse, redirect
from models import user

def user_table(request):
    context = {
        "users": user.objects.all(),
    }
    return render(request, 'semi_restful/user_table.html', context)


def index(request):
    return render(request, 'semi_restful/index.html')


def new(request):
    print 'hello'
    user.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect('/')

def user_info(request, num):
    context = {
        "users": user.objects.get(id=num),
    }
    return render(request, 'semi_restful/user.html', context)

def edit_info(request, num):
    context = { "num": num, }
    return render(request, 'semi_restful/edit.html', context)


def edit(request, num):
    print "hello"
    current = user.objects.get(id=num)
    print request.POST['first_name']
    current.first_name = request.POST['first_name']
    current.last_name = request.POST['last_name']
    current.email = request.POST['email']
    current.save()
    return redirect("/")



def delete(request, num):
    current = user.objects.get(id=num)
    current.delete()
    print "hello"
    return redirect("/")
