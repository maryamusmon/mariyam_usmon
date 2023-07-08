from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetCompleteView, \
    PasswordResetView, PasswordResetDoneView
from django.template.defaulttags import url
from django.urls import path

from shop.views import index_view, SignUpView, about_view, contact_view, shop_single_view, ProductListView, add_to_cart, \
    SearchView, CategoryListView, ProductDetailView


class TestView:
    pass


urlpatterns = [
    path('', index_view, name='index_view'),
    path('register/', SignUpView.as_view(), name='register_view'),

    path('login/', LoginView.as_view(
        template_name='auth/login.html',
        redirect_authenticated_user=True,
        next_page='index_view'
    ), name='login_view'),

    path('logut/', LogoutView.as_view(next_page='login_view'), name='logout'),
    path('about/', about_view, name='about_view'),
    path('contact/', contact_view, name='contact_view'),
    path('detail/', shop_single_view, name='detail'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail_view'),
    # password reset urls
    path('reset-password/',
         PasswordResetView.as_view(
             template_name='auth/password_reset.html'
         ),
         name='reset_password'),
    path('reset-password-done/',
         PasswordResetDoneView.as_view(
             template_name='auth/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('reset-password/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(
             template_name='auth/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('reset-password-complete/',
         PasswordResetCompleteView.as_view(
             template_name='auth/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('products/', ProductListView.as_view(), name='shop_view'),
    path('cart_add/<int:pk>/', add_to_cart, name='cart'),
    path('search/', SearchView.as_view(), name='search'),
    path('category_product_list/<int:pk>/', CategoryListView.as_view(), name='category_product_list'),



]