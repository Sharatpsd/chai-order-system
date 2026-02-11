# tweet/urls.py
from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
    # Home & Main pages
    path('', views.index, name='home'),

    # Separate pages (এখন anchor এর বদলে আলাদা URL)
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),              # flavors list দেখাবে
    path('testimonials/', views.testimonials, name='testimonials'),

    # Order & Payment Flow
   path('order/create/', views.create_order, name='create_order'),
 
    path('checkout/<int:order_id>/', views.checkout, name='checkout'),
    path('order-success/<int:order_id>/', views.order_success, name='order_success'),

    # Contact
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', views.contact_message, name='contact_submit'),  # AJAX submit

]