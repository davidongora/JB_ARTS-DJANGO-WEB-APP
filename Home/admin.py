from django.contrib import admin
from .models import Canvas, Bottles, Gallery, Testimonials, Artists, OtherImages, Order

# Register your models here.

admin.site.register(Canvas)
admin.site.register(Bottles)
admin.site.register(Gallery)
admin.site.register(Testimonials)
admin.site.register(Artists)
admin.site.register(OtherImages)
admin.site.register(Order)
