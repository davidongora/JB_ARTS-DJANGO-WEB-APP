from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Canvas, Bottles, Gallery, Testimonials, Artists, OtherImages, Order
from django.urls import reverse


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
    

def checkout(request, product_type, product_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        if product_type == 'canvas':
            product = get_object_or_404(Canvas, id=product_id)
        elif product_type == 'bottle':
            product = get_object_or_404(Bottles, id=product_id)
        else:
            messages.error(request, 'Invalid product type')
            return redirect('store')

        order = Order.objects.create(
            product_type=product_type,
            product_id=product.id,
            name=name,
            email=email,
            address=address,
            phone=phone,
            quantity=1,
            total_price=product.price
        )

        # Send email
        email_message = f"A new order has been placed for {name} Address: \n{address}\n\n\n From {name}\n{email}"
        try:
            send_mail(
                subject="New Order",
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['josephbarasa622@gmail.com','kelalianda@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'YOUR REQUEST HAS BEEN SENT, KINDLY WAIT AS WE PROCESS YOUR ORDER')
        except Exception as e:
            print(f'Error sending email! {e}')
            messages.error(request, 'Failed to send email')
        user_email_message = f"Dear {name},\n\nYour order has been recieved and it's being processed.\n\nProduct : {product.name}\nQuantity : 1\nTotal Price : Kshs.{product.price}\n\nWe will get back to you shortly.\n\nThankyou,\nJB ARTS"
        try:
            send_mail(
                subject="Order Confirmation",
                message=user_email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception as e:
            print(f'Error sending email to user! {e}')
            messages.error(request, 'Failed to send order confirmation email to you')
        return redirect('order_detail', order_id=order.id)

    else:
        if product_type == 'canvas':
            product = get_object_or_404(Canvas, id=product_id)
        elif product_type == 'bottle':
            product = get_object_or_404(Bottles, id=product_id)
        else:
            messages.error(request, 'Invalid product type')
            return redirect('store')

        return render(request, 'checkout.html', {'product': product})
    
    
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.product_type == 'canvas':
        product = get_object_or_404(Canvas, id=order.product_id)
    elif order.product_type == 'bottle':
        product = get_object_or_404(Bottles, id=order.product_id)
    return render(request, 'checkout.html', {'order': order, 'product': product})
