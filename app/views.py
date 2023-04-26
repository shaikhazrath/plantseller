from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact,products,youtube
from django.contrib import messages
# Create your views here.
def home(request):
    product = products.objects.all()
    yt = youtube.objects.all()
    return render( request,'home.html',{'products':product,'yt':yt})






def contact_form(request):
    if request.method == 'POST':
        # Get the data from the form
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Create a new Contact object and save it to the database
        contact = Contact(email=email, subject=subject, message=message)
        contact.save()
        
        # Return a response to the user
        messages.success(request, 'Thanks for contacting us!')
        
        # Redirect to the same page
        return redirect('/#contact')
    # If the request method is not POST, render the form template
    return render(request, 'contact_form.html')