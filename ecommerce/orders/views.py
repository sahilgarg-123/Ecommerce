from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from accounts.models import MyUser
from products.models import Product
from orders.models import OrderItem, Order

# Create your views here.


def get_user_pending_order(request):
    user_profile = get_object_or_404(MyUser, id=request.user.id)
    order = Order.objects.filter(owner=user_profile)
    if order.exists():
        return order[0]
    return 0


def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(MyUser, id=request.user.id)
    product = Product.objects.filter(id=kwargs.get('pk', '')).first()
    order_item = OrderItem.objects.get_or_create(product=product)
    user_order = Order.objects.get_or_create(owner=user_profile)
    user_order[0].items.add(order_item[0])
    user_order[0].save()
    messages.info(request, "Item added to cart")
    return redirect(reverse('list-product'))


def delete_from_cart(request, pk):
    item_to_delete = OrderItem.objects.filter(pk=pk)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('order-details'))


def order_details(request):
    if request.method == 'POST':
        send_mail('Ecommerce order',
                  'Your order was successful! Thank you for using Ecommerce services!',
                  'no-reply@ecommerce.com',
                  ['{}'.format(request.user.email)],
                  fail_silently=False)
        return redirect('/order-checkout/')

    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'orders/order_detail.html', context)


def order_checkout(request):
    return render(request, 'orders/order_checkout.html')
