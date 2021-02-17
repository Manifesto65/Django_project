from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print("you are :", request.session.get('email'))
        return render(request, 'index.html', data)


    def post(self, request):
        product_id = request.POST.get('product_id')
        minus = request.POST.get('minus')
        cart =request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if minus:
                    if quantity <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity - 1
                else:
                    cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] =1

        request.session['cart'] = cart
        print("cart :", request.session['cart'])
        return redirect('homepage')



