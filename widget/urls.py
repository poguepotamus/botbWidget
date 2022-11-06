from django.urls import path

from . import views

urlpatterns = [
	path('widget/', views.widget, name='widget')
]
