from django.urls import path
from django.contrib import admin

from mainapp import views as mainapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp_views.main),
    path('products/', mainapp_views.products),
]
