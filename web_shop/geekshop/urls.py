from django.urls import path
from django.contrib import admin
from mainapp import views as mainapp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp_views.main, name="index"),
    path('products/', mainapp_views.products, name='products'),
    path('context/', mainapp_views.test_context),
    path('temp/', mainapp_views.temp)
]

if settings.DEBUG:
    print("Helelo")
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
