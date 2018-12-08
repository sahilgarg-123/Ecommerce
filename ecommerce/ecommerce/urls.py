"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from products.views import ProductListView, ProductDetailView, ProductCreateView,\
                            ProductUpdateView, ProductDeleteView, ProductSearchView
from accounts.views import SignupView
from ecommerce.views import HomePageView
from orders.views import add_to_cart, delete_from_cart, order_details, order_checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    path('products/search/', ProductSearchView.as_view(), name='search-product'),
    path('products/add/', ProductCreateView.as_view(), name='create-product'),
    path('products/list/', ProductListView.as_view(), name='list-product'),
    path('products/<pk>/', ProductDetailView.as_view(), name='detail-product'),
    path('products/<pk>/update/', ProductUpdateView.as_view(), name='update-product'),
    path('products/<pk>/delete/', ProductDeleteView.as_view(), name='delete-product'),

    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('delete-from-cart/<pk>/', delete_from_cart, name='delete-from-cart'),
    path('order-details/', order_details, name='order-details'),
    path('order-checkout/', order_checkout, name='order-checkout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
