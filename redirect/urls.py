from django.urls import path
from . import views
app_name='redirect'
urlpatterns=[
	path('/facebook',views.facebook,name='facebook')]