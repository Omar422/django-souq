from django.shortcuts import render
from .models import Product
# Create your views here.

def product_list(request):
    
    product_list = Product.objects.all()
    return render(request, 'Product/product_list.html', {'list':product_list})


def product_detail(request, product_id):
    
    product_detail = Product.objects.get(id = product_id)
    context = {'detail': product_detail}
    return render(request, 'Product/product_detail.html', context)