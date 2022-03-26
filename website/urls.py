from django.urls import path

from website import views

app_name = 'website'

urlpatterns = [
    path('say-hi/<str:name>/', views.say_hi, name='say-hi'),
    path('', views.index, name='index'),
]
