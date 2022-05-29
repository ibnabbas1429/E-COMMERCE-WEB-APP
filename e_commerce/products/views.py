from pickle import NONE
import django
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from . models import Products
from .form import ProductForm


def homepage(request):
    product = Products.objects.all()
    print(product)
    return render(request, 'home.html', context={"product":product})
def about(request,*args, **kwargs):
    print(*args,**kwargs)
    print(request.user)
    return HttpResponse("<h1> about page </h1>")
#creating view to render the form

def create_form_view(request):
    form = ProductForm(request.POST or NONE)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request, "products/create_form.html", context)


