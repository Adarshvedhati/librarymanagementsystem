from django.http import HttpResponse
from django.shortcuts import redirect, render

from Book.forms import BooksForms
from Book.models import Books

# Create your views here.
def home(request):
    context={
        'title':'home'
    }
    return render(request,'base.html',context)
def add_book(request):
    form=BooksForms()
    if request.method=='POST':
        x=BooksForms(data=request.POST)
        if x.is_valid():
            title=x.cleaned_data['title']
            author=x.cleaned_data['author']
            published_date=x.cleaned_data['published_date']
            desc=x.cleaned_data['desc']
            Books.objects.create(title=title,author=author,published_date=published_date,desc=desc)
            return redirect('list')
    
        
    context={
        'title':'addbook',
        'form':form,
    }
    return render(request,'add.html',context)
def display(request):
    add=Books.objects.all().order_by('-id')
    search=request.GET.get('search')
    if search:
        add=Books.objects.filter(title__contains=search)
            
    context={
        'title':'display',
        'data':add

    }
    return render(request,'display_all.html',context)
def update(request,id):
    try:
        y=Books.objects.get(id=id)
    except:
        return HttpResponse('hi hello ')
    add=BooksForms()
    if request.method=='POST':
        x=BooksForms(data=request.POST)
        if x.is_valid():
            y.title=x.cleaned_data['title']
            y.author=x.cleaned_data['author']
            y.published_date=x.cleaned_data['published_date']
            y.desc=x.cleaned_data['desc']
            y.save()
            return redirect('list')

    context={
        'title':'update',
        'form':add

    }
    return render(request,'update.html',context)

def delete_book(request,id):
    try:
        y=Books.objects.get(id=id)
    except:
        return HttpResponse('hi hello ')
    y.delete()
    return redirect('list')

