from django import forms
from .models import Transaction

class CancelTransactionForm(forms.Form):
    transaction_id = forms.ModelChoiceField(queryset=Transaction.objects.all())