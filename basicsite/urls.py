from django.urls import path
from . import views
from  django.conf.urls.static import static
from django.conf import settings
app_name='basic_site'
urlpatterns=[
	path('',views.home,name='home'),
	path('register',views.register,name='register'),
	path('about',views.about,name='about'),
	path('contact_us',views.contact_us,name='contact_us'),]
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document=settings.MEDIA_ROOT)	