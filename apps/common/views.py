from django.shortcuts import render, redirect
from django.views import View
from apps.cart_shop.models import Product
from apps.cart_shop.views import fill_cart_in_session, cart_items_count


class ShopView(View):
    def get(self, request):
        cart = fill_cart_in_session(request)
        products = Product.objects.all()
        context = {
            'data': products,
            'cart_items_count': cart_items_count(request)
        }
        return render(request, 'shop/shop.html', context)


class ProductSingleView(View):
    def get(self, request, id):
        cart = fill_cart_in_session(request)
        product = Product.objects.filter(id=id).first()
        if not product:
            return render(request, "shop/404.html", status=404)

        context = {
            'product': product,
            'cart_items_count': cart_items_count(request)
        }
        return render(request, "shop/product-single.html", context)


class CartView(View):
    def get(self, request):
        return redirect('cart_shop:cart')
