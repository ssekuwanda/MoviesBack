from .models import QrCodePayment
from django import forms


class QrCodePaymentForm(forms.ModelForm):
    class Meta:
        model = QrCodePayment
        fields = ['amount', 'password',]
