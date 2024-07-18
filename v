from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
# from .models import *
from .models import Canvas, Bottles, Gallery, Testimonials, Artists, OtherImages, Order
from django.urls import reverse
from django.http import HttpResponse
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


# function for creating orders
def checkout(request, order_id, product_type, product_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        Order.objects.create(
            product_type=product_type,
            product_id=product.id,
            name=name,
            email=email,
            address=address,
            phone=phone,
            quantity=1,
            total_price=product.price
        )

        # send email
        email_message = f"Address: \n{address}\n\n\n From {name}\n{email}"
        try:
            send_mail(
                subject="New Order",
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['josephbarasa622@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your request has been sent, kindly wait as we process your order.')
        except Exception as e:
            print(f'Error sending email! {e}')
            messages.error(request, 'Failed to send email')
            
    else:
        order = get_object_or_404(Order, id=order_id)
        if order.product_type == 'canvas':
            product = get_object_or_404(Canvas, id=order.product_id)
        elif order.product_type == 'bottle':
            product = get_object_or_404(Bottles, id=order.product_id)
        return render(request, 'store/order_detail.html', {'order': order, 'product': product})
        
    return render(request, 'checkout.html')
