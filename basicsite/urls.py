from django.urls import path
from . import views
from  django.conf.urls.static import static
from django.conf import settings
app_name='basic_site'
urlpatterns=[
	path('',views.home,name='home'),
	path('register?refer_id=786',views.register,name='register'),
	path('register?refer_id=786-',views.gmail,name='gmail'),
	path('about',views.about,name='about'),
	path('contact_us',views.contact_us,name='contact_us'),
	path('paymentsid=12334',views.payments,name='payments')]
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)	
