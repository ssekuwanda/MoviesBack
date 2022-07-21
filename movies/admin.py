from django.contrib import admin
from .models import Movie, Downloaded, QrCodePayment

admin.site.register(Movie)
admin.site.register(Downloaded)
admin.site.register(QrCodePayment)

