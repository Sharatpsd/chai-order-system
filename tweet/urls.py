# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('order/', views.order_flavor, name='order_flavor'),
# ]
from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.index, name='about'),  # same page, anchor use করবি
]
