from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, Contact
from django.shortcuts import render
from .models import Order, Contact

def index(request):
    # This will render your main HTML page
    return render(request, 'tweet/index.html')
@csrf_exempt
def order_flavor(request):
    if request.method == "POST":
        flavor = request.POST.get("flavor")
        if flavor:
            Order.objects.create(flavor=flavor)
            return JsonResponse({"status": "success", "message": f"Order for {flavor} saved!"})
    return JsonResponse({"status": "error", "message": "Invalid request"})

@csrf_exempt
def contact_message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            return JsonResponse({"status": "success", "message": "Message sent successfully!"})
    return JsonResponse({"status": "error", "message": "Invalid request"})
