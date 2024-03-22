from django.shortcuts import render,redirect
from .forms import RegisterForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

 
    
def contact(request):
    return render(request,'contact.html')


def register_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register_form.html', {'form':form})        