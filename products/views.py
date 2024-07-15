from django.shortcuts import render

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
    return render(request,'products.html')

def detail_products(request):
    return render(request,'products.html')