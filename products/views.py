from django.shortcuts import render
from . models import Product

# Create your views here.
def index(request):
    return render(request,'index.html')

def list_products(request):
    """"_summary_
    return product list page
    Args:
        request (_type_): _description_
        
    Returns:
        _types_: _description_
    """
    product_list=Product.objects.all()
    context={ 'products' : product_list}
    return render(request,'products.html',context)

def detail_products(request):
    return render(request,'product_details.html')