from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import CancelTransactionForm
from .models import Transaction

def cancel_transaction(request):
    if request.method == 'POST':
        form = CancelTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.cleaned_data['transaction_id']
            transaction.status = 'Canceled'
            transaction.save()
            return render(request, 'canceled.html')
    else:
        form = CancelTransactionForm()
    return render(request, 'cancel_transaction.html', {'form': form})