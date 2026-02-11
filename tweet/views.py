from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
import stripe

from .models import Order, Flavor, Contact
from .forms import ContactForm

# Stripe setup
stripe.api_key = settings.STRIPE_SECRET_KEY


# -----------------------
# Basic Pages
# -----------------------

def index(request):
    flavors = Flavor.objects.filter(is_active=True)
    return render(request, 'tweet/index.html', {'flavors': flavors})


def about(request):
    return render(request, 'tweet/about.html')


def menu(request):
    flavors = Flavor.objects.filter(is_active=True)
    return render(request, 'tweet/menu.html', {'flavors': flavors})


def testimonials(request):
    return render(request, 'tweet/testimonials.html')


def contact(request):
    form = ContactForm()
    return render(request, 'tweet/contact.html', {'form': form})


# -----------------------
# Order Creation
# -----------------------

@require_POST
@login_required
def create_order(request):
    flavor_id = request.POST.get('flavor_id')
    quantity = int(request.POST.get('quantity', 1))

    if not flavor_id:
        return JsonResponse({'status': 'error', 'message': 'Flavor ID required'}, status=400)

    flavor = get_object_or_404(Flavor, id=flavor_id, is_active=True)

    total_price = flavor.display_price * quantity

    order = Order.objects.create(
        user=request.user,
        flavor=flavor,
        quantity=quantity,
        total_price=total_price,
        status='pending',
        is_paid=False
    )

    return JsonResponse({
        'status': 'success',
        'message': f'Order placed for {quantity}x {flavor.name}',
        'order_id': order.id
    })


# -----------------------
# Checkout Page
# -----------------------

@login_required
def checkout(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user, is_paid=False)

    context = {
        'order': order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }

    return render(request, 'tweet/checkout.html', context)


# -----------------------
# Stripe Payment Processing
# -----------------------

@require_POST
@login_required
def process_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user, is_paid=False)

    try:
        payment_method_id = request.POST.get('payment_method_id')

        if not payment_method_id:
            return JsonResponse({'success': False, 'error': 'Payment method required'}, status=400)

        intent = stripe.PaymentIntent.create(
            amount=int(order.total_price * 100),
            currency='bdt',
            payment_method=payment_method_id,
            confirmation_method='manual',
            confirm=True,
            description=f'Order #{order.id}',
            metadata={
                'order_id': order.id,
                'user_id': request.user.id
            }
        )

        if intent.status in ['succeeded', 'processing']:
            order.is_paid = True
            order.payment_id = intent.id
            order.status = 'paid' if intent.status == 'succeeded' else 'processing'
            order.save()

            return JsonResponse({
                'success': True,
                'redirect': reverse('tweet:order_success', args=[order.id])
            })

        return JsonResponse({
            'success': False,
            'error': 'Payment failed'
        }, status=400)

    except stripe.error.CardError as e:
        return JsonResponse({'success': False, 'error': e.user_message}, status=400)

    except stripe.error.StripeError:
        return JsonResponse({'success': False, 'error': 'Stripe error occurred'}, status=500)

    except Exception:
        return JsonResponse({'success': False, 'error': 'Server error'}, status=500)


# -----------------------
# Success Page
# -----------------------

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if not order.is_paid:
        messages.warning(request, "Your payment is processing.")

    return render(request, 'tweet/success.html', {'order': order})


# -----------------------
# Contact Form (AJAX)
# -----------------------

@require_POST
def contact_message(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        form.save()
        return JsonResponse({
            "status": "success",
            "message": "Message sent successfully!"
        })

    return JsonResponse({
        "status": "error",
        "errors": form.errors
    }, status=400)
