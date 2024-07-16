from django.shortcuts import render,redirect
from .models import Canvas, Bottles, Gallery, Testimonials, Artists, OtherImages, Order
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from . import views
from django.core.mail import send_mail

# Create your views here.


def home(request):
   
    canvas = Canvas.objects.all()
    bottle = Bottles.objects.all()  
    gall = Gallery.objects.all()
    testimonial = Testimonials.objects.all()
    artist = Artists.objects.all()
    otherImages = OtherImages.objects.all()
    return render(request, 'index.html',
                  {'canvas': canvas, 'bottle': bottle, 'gall': gall,
                   'testimonial': testimonial, 'artist': artist, 
                   'otherImages': otherImages}
                  )


def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email') 
        address = request.POST.get('address')
        canvas = Canvas.objects.get(id=pk)
        
        order = Order(name=name, email=email, address=address)
        order.save()
    
        # Display success message using Django messages framework
        messages.success(request, 'Your order was successfully placed and a confirmation email has been sent!')
            
        messages.info(request, 'THANKYOU FOR SHOPPING WITH US.KINDLY WAIT AS WE PROCESS YOUR ORDER!')
        return redirect('checkout') 
        # return HttpResponse(f"Thank you for your order, {name}!Kindly wait as we process your purcase.")
    return render(request, 'checkout.html')
