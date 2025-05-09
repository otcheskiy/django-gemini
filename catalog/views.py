from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 6)  # товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/product_list.html', {'page_obj': page_obj})

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'catalog/product_detail.html', {'product': product})