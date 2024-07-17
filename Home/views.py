from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import *
from django.urls import reverse
from django.http import HttpResponse
# Canvas, Bottles, Gallery, Testimonials, Artists, OtherImages, Order
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

        Order.objects.create(
            name=name,
            email=email,
            address=address
        )

        # send email
        email_message = f"Address: \n{address}\n\n\n From: \n{name}\n{email}"
        try:
            send_mail(
                subject="New Order",
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['josephbarasa622@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'You have an email')
        except Exception as e:
            print(f'Error sending email! {e}')
            messages.error(request, 'Failed to send email')

    return render(request, 'checkout.html')
