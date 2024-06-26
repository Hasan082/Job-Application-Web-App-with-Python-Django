from django.shortcuts import render, redirect, reverse
from .forms import JobForm
from .models import Job
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            
            Job.objects.create(
                first_name=first_name, 
                last_name=last_name, 
                email=email, 
                date=date, 
                occupation=occupation
            )

            # Todo: send email
            msg_body = (f"Thank you for expressing interest in the position, {first_name}. We appreciate your "
                        f"application and will review it carefully. Expect to hear from us soon regarding the next "
                        f"steps in the hiring process. Here is your data: \n\nFirst Name: {first_name}\nLast Name: "
                        f"{last_name}\nEmail: {email}\nOccupation: {occupation}\nDate: {date}. \nThank you!")

            email_send = EmailMessage(
                'Job Application for the Position',
                body=msg_body,
                to=[email]
            )

            email_send.send()

            messages.success(request,
                             'Your application has been submitted successfully!')

            return redirect(reverse('index'))
        
    return render(request, 'index.html')

# https://gale.udemy.com/course/the-python-mega-course/learn/lecture/36906752#overview