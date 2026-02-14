# chaiheadq/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tweet.views import stripe_webhook

urlpatterns = [
    path('admin/', admin.site.urls),

    # Tweet app
    path('', include('tweet.urls', namespace='tweet')),

    # Allauth (Google login, signup, logout etc.)
    path('accounts/', include('allauth.urls')),

   path('stripe/webhook/', stripe_webhook, name='stripe_webhook'),

]

# Development-এ media files serve করার জন্য
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)