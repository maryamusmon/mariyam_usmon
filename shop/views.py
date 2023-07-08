from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView

from shop.forms import UserRegisterForm
from django.views.generic.edit import CreateView

from shop.models import Product, Cart, Category


def index_view(request):
    return render(request, 'index.html')


class SignUpView(CreateView):
    template_name = 'auth/register.html'
    model = User
    success_url = reverse_lazy('login_view')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"


def about_view(request):
    return render(request, 'auth/about.html')


def contact_view(request):
    return render(request, 'auth/contact.html')


def shop_single_view(request):
    return render(request, 'auth/shop-single.html')


class ProductListView(ListView):
    model = Product
    template_name = 'auth/shop.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(object_list=object_list, **kwargs)
        contex['categories'] = Category.objects.all
        return contex


def add_to_cart(request, pk):
    cart = Cart.objects.filter(user=request.user, product_id=pk)
    if not cart:
        try:
            product = Product.objects.get(pk=pk)
            new_cart = Cart.objects.create(
                user=request.user, product_id=product.id, price=product.price
            )
            new_cart.save()
            return redirect('shop_view')

        except ObjectDoesNotExist:
            pass

    return redirect('index_view')
    # else:
    #     try:
    #         cart = Cart.objects.get(user=request.user, active=True)
    #     except ObjectDoesNotExist:
    #         cart = Cart.objects.create(user=request.user)
    #         cart.save()
    #         cart.add_to_cart(pk)
    #         return redirect('cart')
    #     else:
    #         return redirect('index_view')


def remove_from_cart(request, book_id):
    if request.user.is_authenticated():
        try:
            book = Product.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
        else:
            cart = Cart.objects.get(user=request.user, active=True)
            cart.remove_from_cart(book_id)
        return redirect('cart')
    else:
        return redirect('index_view')


class SearchView(ListView):
    model = Product
    template_name = "auth/shop.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(object_list=object_list, **kwargs)
        contex['categories'] = Category.objects.all
        contex['products'] = self.model.objects.filter(title__icontains=self.request.GET.get('q'))
        return contex


class CategoryListView(ListView):
    model = Product
    template_name = 'auth/shop.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(object_list=object_list, **kwargs)
        contex['categories'] = Category.objects.all
        contex['products'] = self.model.objects.filter(category_id=self.request.resolver_match.kwargs.get('pk'))
        return contex


class ProductDetailView(DetailView):
    model = Product
    template_name = "auth/shop-single.html"
    context_object_name = "product"
