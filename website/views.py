from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Receipt
from .models import ReceiptIngredient
from .models import IngredientMeta
from .models import QuantityUnit
from .models import Category

def receipt_list(request):
    receipts = Receipt.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/receipt_list.html', {'receipts': receipts})
    
def receipt_detail(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    return render(request, 'website/receipt_detail.html', {'receipt': receipt})