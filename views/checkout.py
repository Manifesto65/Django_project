from django.shortcuts import render, redirect
from django.views import View

from store.models import Customer
from store.models.order import Order
from store.models.product import Product


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phoneno')
        cart = request.session.get('cart')
        product_id = list(cart.keys())
        products = Product.get_cart_products(product_id)
        customer = request.session.get('customer_id')
        print(address,phone,cart,customer,products)
        for product in products:
            print(product)
            order = Order(customer= Customer(id = customer),
                          product=product,
                          quantity=cart.get(str(product.id)),
                          price=product.price,
                          address=address,
                          phone=phone)

            order.placeOrder();

        request.session['cart'] = {}

        return redirect('cart')
