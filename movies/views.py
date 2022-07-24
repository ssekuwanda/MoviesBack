from django.shortcuts import render
from .models import Movie, QrCodePayment
from .serializers import MovieSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import permissions
from rest_framework.permissions import IsAuthenticated
from .forms import QrCodePaymentForm
from django.shortcuts import render, redirect, get_object_or_404


class MoviesListAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.order_by('?')
    # permission_classes = (permissions.IsOwner,IsAuthenticated)

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    lookup_fields = "id"

def qrcode_generation(request):
    if request.method == "POST":
        form = QrCodePaymentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('qrcode',form.code)
    else:
        form = QrCodePaymentForm()
    context = {'form': form}
    return render(request, 'sale.html', context)

def gen_code(request, slug):
    code = get_object_or_404(QrCodePayment, code=slug)
    return render(request, 'qrcode.html', {'code':code})


