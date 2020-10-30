from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    # email = forms.EmailField(required='True')
    #configurations
    class Meta:
        model = Ticket
        fields = ['flight', 'row', 'column', 'first_name', 'last_name', 'passenger']
