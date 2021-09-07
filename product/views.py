from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


# Create your views here.

def product_list(request):

    product_list = Product.objects.all()
    paginator = Paginator(product_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'Product/product_list.html', {'list':page_obj})


def product_detail(request, product_slug):
    
    product_detail = Product.objects.get(prdslug = product_slug)
    context = {'detail': product_detail}
    return render(request, 'Product/product_detail.html', context)