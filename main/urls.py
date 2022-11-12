from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', include(('shop.urls', 'shop'), namespace='shop')),
    path('auth/', include('authentication.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
