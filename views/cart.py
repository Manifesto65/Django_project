from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        print(ids)
        products = Product.get_cart_products(ids)
        print(products)
        return render(request, 'cart.html',{'products' :products})

