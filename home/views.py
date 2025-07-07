from django.shortcuts import render, redirect

from item.models import Category, Item
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'home/index.html', {
        'categories': categories,
        'items': items,
        'signup_form': SignupForm()
    })

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')


def signup(request):
    if request.method == 'POST':  
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'home/signup.html', {
        'form': form
    })
