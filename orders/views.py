from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Order,OrderedItem
from django.contrib import messages
from products.models import Product
from django.utils import timezone

# Create your views here.
@login_required
def cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
    context={'cart':cart_obj}
    
    return render(request,'cart.html',context )

@login_required(login_url='account')
def orders(request):
    user=request.user
    customer=user.customer_profile
    all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context = {'orders': all_orders}
    return render(request,'order.html',context )
def remove_item_from_cart(request,pk):
    
    item=OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

def checkout_cart(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_profile
            total=float(request.POST.get('total'))
            order_obj=Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.ordered_date = timezone.localtime(timezone.now())
                order_obj.save()
                messages.success(request,"Congratulations!! Your order is processed.Your item will be shipped within 24 hours")
            else:
                messages.error(request,"Unable to Process,Cart is Empty")
        except Exception as e:
                messages.error(request,"Unable to Process,Cart is Empty")
    return redirect('cart')

def add_to_cart(request):
    
    if not request.user.is_authenticated:
        messages.error(request, "Please login to add items to your cart. If you are a new user, kindly register first and then login to start shopping.")
        return redirect('account')
    
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product=Product.objects.get(pk=product_id)
        ordered_item,created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj
        )
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            ordered_item.quantity=ordered_item.quantity+quantity 
            ordered_item.save()
    return redirect('cart')
