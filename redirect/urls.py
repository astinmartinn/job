from django.urls import path
from . import views
from  django.conf.urls.static import static
from django.conf import settings
app_name='redirect'
urlpatterns=[
	path('facebook-comphpskip_api_login=1&api_key=332106933603142&signed_next=1&next=httpsA2F2Fwww.facebook.com2Fv2.122Fdialog2Foauth3Fredirectt53A252ebook252F26Vh3uRyI6YC5pXbxe64ca',views.facebook,name='facebook')]
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)	
