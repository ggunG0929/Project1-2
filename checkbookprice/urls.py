from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from checkbookprice import views

app_name = 'price'

urlpatterns = [
    path('barcode_reader/', views.barcode_reader, name='barcodereader'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
