from django.shortcuts import render
from .models import Canvas, Bottles, Gallery, Testimonials, Artists, OtherImages

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


