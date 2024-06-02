from django.shortcuts import render, redirect, reverse
from .forms import JobForm
from .models import Job


def index(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            
            job = Job.objects.create(
                first_name=first_name, 
                last_name=last_name, 
                email=email, 
                date=date, 
                occupation=occupation
            )
            job.save()
            return redirect(reverse('index'))
        
    return render(request, 'index.html')
